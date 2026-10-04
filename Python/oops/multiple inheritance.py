class parent1():
    def p1name(self):
        print("parent1 name")

class parent2():
    def p2name(self):
        print("parent2 name")

class child(parent1, parent2):
    def cname(self):
        print("child name")

c = child()
c.p1name()
c.p2name()
c.cname()