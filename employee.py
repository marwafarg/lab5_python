from person import *
from car import *


class Employee(person):
    employee_num = 0

    def __init__(self, id, car, email, salary, distanceToWork):
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        Employee.employee_num += 1


    def work(self, hours):
        if hours == 8:
            print("Happy!")
        elif hours > 8:
            print("Tired!")
        elif hours < 8:
            print("Lazy")
        else:
            print("else")

    def sendMail(self, to, receiverName, sub, msg):
        f = open("email.txt", "a")
        f.write("|".join([to, receiverName, sub, msg]))
        f.write('\n')
        f.close()

    def reful(self, gazAmount):
        car.fuelRate = gazAmount
        print("reful assign value success \n Done in reful() ")

    def drive(self, distance):
        print("drive call")
        self.drive_obj = car.run(self, velocity=3, distance=3)
        print("Done")
    @classmethod
    def CalcNumsEmp(cls):
        cls.employee_num += 1
        print(f" Employee_number are {cls.employee_num}")


employee = Employee(1, "f16", "mero@iti.com", 1000, 20)
print(employee)
employee2 = Employee(2, "f16", "mero@iti.com", 1000, 20)


employee.reful(0)

