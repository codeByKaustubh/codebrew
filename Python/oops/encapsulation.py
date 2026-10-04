class car:
    def start(self):
        print("car start")

    def stop(self):
        print("car stop")

audi = car()
audi.start()
audi.stop()

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = employee("Josh", 100)
print(emp.name)
print(emp.salary)