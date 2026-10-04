class F():
    def fname(self):
        print("F name")

class B(F):
    def bname(self):
        print("B name")

class A(B):
    def aname(self):
        print("A name")

class C(B):
    def cname(self):
        print("C name")

class G():
    def gname(self):
        print("G name")

class E(G, F):
    def ename(self):
        print("E name")

print("class F")
f = F()
f.fname()

print()
print("class B")
b = B()
b.fname()
b.bname()

print()
print("class A")
a = A()
a.fname()
a.bname()
a.aname()

print()
print("class C")
c = C()
c.fname()
c.bname()
c.cname()

print()
print("class G")
g = G()
g.gname()

print()
print("class E")
e = E()
e.fname()
e.gname()
e.ename()