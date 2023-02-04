import  random




class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 0
        self.progress = 0
        self.money = 0
        self.alive = True


    def to_work(self):
        print("I need money")
        self.progress += 0.2
        self.money += 1
        self.gladness -= 0.5

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 0.2

    def is_alive(self):
        if  self.progress < -0.5:
            print("Cast out")
            self.alive = False

        elif self.gladness <= 0.4:
            print("Depression...")
            self.alive = False

        elif self.progress > 5:
            print("Passed exams")
            self.alive = False

        elif self.money > 0.7:
            print("Poor")
            self.alive = False

    def day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {self.progress}")
        print(f"Money - {self.money}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " Life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()

        elif live_cube == 2:
            self.to_sleep()

        elif live_cube == 3:
            self.to_chill()

        elif live_cube == 4:
            self.to_work()

        self.day()
        self.is_alive()

roma = Student("Roma")

for day in range(1, 366):
    if roma.alive == False:
        break
    roma.live(day)