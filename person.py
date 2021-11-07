class person :
    def __init__(self,name,money,mood,healthrate):
        self.name=name
        self.money=money
        self.mood=mood
        self.healthrate=healthrate
    def sleep(self,hour):
        if hour==7:
            print("happy")
        elif hour<7:
            print("tired")
        elif hour>7:
            print("lazy")
        else:
            print("try again")



    def eat(self,meals):
        if meals == 3:
            print("100% hth")
        elif meals == 2:
            print("75% hth")
        elif meals == 1:
            print("50% hth")

    def buy(self,items):
        if items==1:
            self.money -= 10
            print(f"your money decreased 10L.E.money now {self.money} ")
        elif items==2:
            self.money -= 20
            print(f"your money decreased 10L.E.money now {self.money} ")

    def sendMail(self, to, receiverName, sub, msg):
        f = open("email.txt", "a")
        f.write("|".join([to, receiverName, sub, msg]))
        f.write('\n')
        f.close()

persons = person(name="marwa", money=1500, mood="happy", healthrate="fine")
print(persons)
print("sleep function")
persons.sleep(9)
print("eat function ")
persons.eat(2)
print("buy function ")
persons.buy(2)


print("email sent successfully see file  ")
persons.sendMail("FROM:- aliaa@gmai.com\n", "TO:- marwa@gmail.com\n", "Subject:- come to eat \n",
                   "Msg:- Hi,MohamedThis is an emailtamplate  thanks \n Regards :)")

