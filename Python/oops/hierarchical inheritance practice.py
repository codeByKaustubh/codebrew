class a:
    def fun1(self):
        print("class a")

class b(a):
    def fun2(self):
        print("class b")

class c(a):
    def fun3(self):
        print("class c")

object1 = b()
object1.fun1()
object1.fun2()

object2 = c()
object2.fun1()
object2.fun3()