class Car:
    def canStart(self):
        print("car can start")

class Brand(Car):
    def canStop(self):
        print("car can stop")

c1 = Brand()
c1.canStart()
c1.canStop()