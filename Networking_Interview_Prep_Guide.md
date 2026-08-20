# Networking Fundamentals — Interview Prep
### For: Inniti Network Solutions LLP walk-in, 21 Aug 2026

**Suggested study order tonight:** OSI/TCP-IP → IP addressing & subnetting → same/different network → ARP & MAC → switch vs router → VLAN/routing/OSPF → TCP vs UDP → DHCP → DNS → ping/traceroute → rapid-fire Q&A. Budget ~20-25 min per section, then skim the rapid-fire section right before you sleep and again in the morning.

---

## 1. OSI Model vs TCP/IP Model

### OSI Model — 7 layers
| # | Layer | Job | Examples | Unit (PDU) |
|---|-------|-----|----------|------------|
| 7 | Application | User-facing services | HTTP, FTP, SMTP, DNS | Data |
| 6 | Presentation | Format, encrypt, compress | SSL/TLS, JPEG | Data |
| 5 | Session | Open/manage/close sessions | NetBIOS, RPC | Data |
| 4 | Transport | End-to-end delivery, ports | TCP, UDP | Segment |
| 3 | Network | Logical (IP) addressing, routing | IP, ICMP, routers | Packet |
| 2 | Data Link | Physical (MAC) addressing, framing | Ethernet, switches | Frame |
| 1 | Physical | Raw bits, cables, signals | Cat6, fiber, hubs | Bits |

**Mnemonic (top→bottom):** *All People Seem To Need Data Processing*
**Mnemonic (bottom→top):** *Please Do Not Throw Sausage Pizza Away*

### TCP/IP Model — 4 layers (what's actually used in real networks)
| TCP/IP Layer | Maps to OSI layers |
|---|---|
| Application | 5, 6, 7 |
| Transport | 4 |
| Internet | 3 |
| Network Access (Link) | 1, 2 |

**Likely question:** *"Why two models?"* — OSI is the teaching/reference model; TCP/IP is what the actual internet runs on. Interviewers want to hear that distinction, not a memorized layer list.

---

## 2. IP Addressing & Subnetting

IPv4 = 32-bit address, written as 4 octets in dotted decimal (e.g. `192.168.1.10`).

### Classes
| Class | First octet range | Default mask | Use |
|---|---|---|---|
| A | 1–126 | /8 (255.0.0.0) | Huge networks |
| B | 128–191 | /16 (255.255.0.0) | Medium networks |
| C | 192–223 | /24 (255.255.255.0) | Small networks |
| D | 224–239 | — | Multicast |
| E | 240–255 | — | Experimental |

(127.x is loopback, not a usable class.)

### Private IP ranges — memorize these
- `10.0.0.0 – 10.255.255.255` (/8)
- `172.16.0.0 – 172.31.255.255` (/12)
- `192.168.0.0 – 192.168.255.255` (/16)

### CIDR quick reference
| CIDR | Subnet mask | Total addresses | Usable hosts |
|---|---|---|---|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 (point-to-point links) |

### Formulas
- Usable hosts = 2^h − 2 (h = host bits)
- Number of subnets = 2^s (s = borrowed bits)

### Fast subnetting trick — the "magic number"
Magic number = 256 − (mask value in the interesting octet). Subnets start at multiples of that number.

**Worked example:** `192.168.10.0/26`
- /26 → 6 host bits → hosts = 2⁶ − 2 = **62 usable hosts**
- Mask = 255.255.255.**192** → magic number = 256 − 192 = **64**
- Subnets: `.0`, `.64`, `.128`, `.192`
- First subnet range: `192.168.10.1 – 192.168.10.62` (broadcast = `.63`)

Practice 2–3 of these tonight (/27, /28, /29) until it's automatic — this is the single most common "prove you can do it live" question for freshers.

---

## 3. How Two PCs Communicate — Same Network vs Different Network

*(See the diagram above — this is the logic behind it.)*

**Same subnet (direct delivery):**
1. PC-A does a bitwise AND of its own IP+mask and the destination IP+mask.
2. If the network portion matches → same LAN.
3. PC-A checks its ARP cache for PC-B's MAC; if empty, it broadcasts an ARP request.
4. PC-B replies with its MAC address.
5. PC-A sends the frame directly addressed to PC-B's MAC — the switch forwards it using its MAC address table. No router involved.

**Different subnet (via gateway):**
1. Network portion doesn't match → different subnet.
2. PC-A sends the frame to its **default gateway** (ARPing for the gateway's MAC first, if unknown).
3. The router receives it, checks its routing table for the best path.
4. It forwards the packet out the correct interface (re-framing it, ARPing for the next hop if needed).
5. Repeats hop-by-hop until it reaches the router local to PC-B's network, which ARPs for PC-B and delivers the frame.

**Key line to say in the interview:** *"MAC addresses only matter within a LAN — routers are what let IP addresses cross network boundaries."*

---

## 4. ARP & MAC Address

- **MAC address:** 48-bit (12 hex digit) address burned into the NIC, format `AA:BB:CC:DD:EE:FF`. First 24 bits = OUI (vendor ID). Operates at Layer 2 — only meaningful within the same LAN/broadcast domain.
- **ARP (Address Resolution Protocol):** maps IP (Layer 3) → MAC (Layer 2).
  - **ARP Request** — broadcast (`FF:FF:FF:FF:FF:FF`): *"Who has this IP? Tell me."*
  - **ARP Reply** — unicast: *"I have that IP, here's my MAC."*
  - Result is cached in the ARP table (view with `arp -a`).

---

## 5. Switch vs Router & Default Gateway

| Switch | Router |
|---|---|
| Layer 2 device | Layer 3 device |
| Forwards by MAC address (CAM/MAC table) | Forwards by IP address (routing table) |
| Connects devices *within* a network | Connects *different* networks |
| One broadcast domain (per VLAN) | Each interface = its own broadcast domain |
| Doesn't need an IP to forward frames | Needs IP config, static/dynamic routes |

**Default gateway:** the router IP a host is configured to send traffic to whenever the destination isn't on its local subnet — usually the first or last usable address in the subnet (e.g. `192.168.1.1`).

---

## 6. VLAN, Routing & OSPF Basics

**VLAN (Virtual LAN):** logically splits one physical switch into multiple broadcast domains — isolates traffic (e.g. per department), reduces broadcast noise, improves security.
- **Access port** — carries traffic for ONE VLAN, connects end devices (PCs, printers).
- **Trunk port** — carries traffic for MULTIPLE VLANs using 802.1Q tagging, connects switch-to-switch or switch-to-router.
- VLANs are separate broadcast domains, so **inter-VLAN routing** (router-on-a-stick or an L3 switch) is needed for them to talk to each other.

**Routing:**
- **Static routing** — routes manually configured by an admin. Simple, no overhead, doesn't scale, no auto-failover.
- **Dynamic routing** — routers exchange routes automatically via a routing protocol. Scales, adapts to link failures, more overhead.

**OSPF (Open Shortest Path First):**
- Link-state **Interior Gateway Protocol** (runs within one autonomous system).
- Metric = **cost**, based on interface bandwidth (higher bandwidth = lower cost).
- Uses **Dijkstra's SPF algorithm** to compute the shortest path.
- Organizes the network into **Areas** — Area 0 is the mandatory backbone; every other area connects to it.
- On multi-access segments (like Ethernet), elects a **DR/BDR** (Designated/Backup Designated Router) to reduce flooding.
- Administrative distance = 110.

At fresher level, you mainly need to *define* OSPF and mention "link-state, cost metric, DR/BDR" — deep config is unlikely to come up.

---

## 7. TCP vs UDP

| TCP | UDP |
|---|---|
| Connection-oriented (3-way handshake) | Connectionless |
| Reliable — ACKs, retransmission | "Best effort" — unreliable |
| Ordered delivery | No ordering guarantee |
| Flow & congestion control | None |
| Header: 20 bytes | Header: 8 bytes |
| Slower, more overhead | Faster, lightweight |
| HTTP/HTTPS, FTP, email, SSH | DNS queries, DHCP, streaming, VoIP, gaming |

**3-way handshake:** `SYN → SYN/ACK → ACK` (then data flows). Connection close is a 4-way `FIN/ACK` exchange.

---

## 8. DHCP (Dynamic Host Configuration Protocol)

**Purpose:** auto-assigns IP address, subnet mask, default gateway, and DNS server — no manual config needed.

**DORA process:**
1. **D**iscover — client broadcasts "I need an IP"
2. **O**ffer — server offers an address
3. **R**equest — client broadcasts "I accept this offer"
4. **A**cknowledge — server confirms, lease timer starts

Ports: server = UDP 67, client = UDP 68.

---

## 9. DNS (Domain Name System)

**Purpose:** translates human-friendly names (`google.com`) → IP addresses.

**Hierarchy:** Root (`.`) → TLD (`.com`, `.in`, `.org`) → Authoritative name servers.

**Query types:**
- **Recursive** — the resolver does all the work and hands the client the final answer.
- **Iterative** — the server refers the client to the next server in the chain.

**Common record types:** A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail server), NS (nameserver), TXT.

Port: 53 (UDP for lookups, TCP for zone transfers / large responses).

---

## 10. Ping & Traceroute

- **Ping:** sends an ICMP Echo Request, waits for an Echo Reply — tests reachability and measures round-trip time.
- **Traceroute / tracert:** sends packets with an incrementing TTL (1, 2, 3…). Each router along the path decrements TTL; when it hits 0, that router replies with "TTL Exceeded," revealing itself as a hop. Repeats until the destination is reached — used to map the path and spot where connectivity breaks.

---

## Quick Reference: Common Port Numbers
| Port | Protocol |
|---|---|
| 20/21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 67/68 | DHCP |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |

---

## Rapid-Fire Q&A

**Q: Difference between a hub and a switch?**
Hub = Layer 1, dumbly repeats to every port, single collision domain. Switch = Layer 2, intelligently forwards based on MAC address.

**Q: What happens when you type a URL into a browser?**
DNS resolution → TCP handshake → TLS handshake (if HTTPS) → HTTP request/response → page renders.

**Q: Broadcast domain vs collision domain?**
Broadcast domain = set of devices that receive each other's broadcasts (bounded by routers/VLANs). Collision domain = set of devices that could collide if transmitting simultaneously (each switch port is its own collision domain).

**Q: Why do we subnet?**
Efficient IP allocation, smaller broadcast domains, better organization and security.

**Q: Public IP vs private IP?**
Private IPs are for use inside a LAN only (not routable on the internet); public IPs are globally unique and routable on the internet.

**Q: What is NAT?**
Network Address Translation — translates private IP addresses to a public IP so internal devices can reach the internet.

---

## About the "Cisco Packet Tracer / CCNA / Networking Labs" Resume Tip

Quick talking points to have ready (see chat for the full explanation):
- You've completed **Computer Networks** coursework in your BSc.
- You're currently doing **"Introduction to Cybersecurity"** through **Cisco Networking Academy** — this is the same platform CCNA training runs on.
- Be upfront that you haven't done formal CCNA/Packet Tracer labs yet, but express genuine interest in pursuing CCNA — it directly matches what this role is asking for.

---

## Interview Day Checklist
- [ ] Carry your printed, updated resume
- [ ] Arrive by 9 AM to avoid the rush
- [ ] Skim this guide once more in the morning, focus on the rapid-fire section
- [ ] Be honest about what you know vs. are still learning — freshers aren't expected to be experts, just to have a solid grasp of fundamentals and a genuine willingness to learn
