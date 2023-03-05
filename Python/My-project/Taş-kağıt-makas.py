#taş - kağıt - makas
import random

secenekler = ["Taş", "Kağıt", "Makas"]

sor = input("      Taş - Kağıt - Makas ? :")

x = random.choice(secenekler)

if x == "Taş":
    if sor == "Taş":
        print("Berabere")
    elif sor == "Kağıt":
        print("Kazandınız")
    elif sor == "Makas":
        print("Kaybettiniz")

if x == "Kağıt":
    if sor == "Taş":
        print("Kaybettiniz")
    elif sor == "Kağıt":
        print("Berabere")
    elif sor == "Makas":
        print("Kazandınız")

if x == "Makas":
    if sor == "Taş":
        print("Kazandınız")
    elif sor == "Kağıt":
        print("Kaybettiniz")
    elif sor == "Makas":
        print("Berabere")
