class grandparent:
    def gpname(self):
        print("grandparent")

class parent(grandparent):
    def pname(self):
        print("parent")

class child(parent):
    def cname(self):
        print("child")

k = child()
k.gpname()
k.pname()
k.cname()