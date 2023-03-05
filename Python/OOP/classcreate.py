class calisan:
    def __init__(self, name, surname, age, job):
        self.name = name
        self.surname = surname
        self.age = age
        self.job = job

    def show_info(self):
        print(
            f"ad :{self.name}\nsoyisim :{self.surname}\nyas :{self.age}\nmeslek :{self.job}\n")


calisan1 = calisan("kerem kenan", "eren", 16, "AI enginner")
# print(calisan1.name, calisan1.surname, calisan1.age)

calisan2 = calisan("Yusuf", "Eren", 22, "Mekatronik Mühendisi")
# print(calisan2.name, calisan2.surname, calisan2.age)


calisan1.show_info()
calisan2.show_info()
