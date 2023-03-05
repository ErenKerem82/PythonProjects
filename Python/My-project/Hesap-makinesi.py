# basic calculator
from math import sqrt, factorial


def topla(num1, num2):
    return num1 + num2


def cikar(num1, num2):
    return num1 - num2


def carp(num1, num2):
    return num1 * num2


def bol(num1, num2):
    return num1 / num2


def kok_al(kok):
    return sqrt(kok)


def faktoriel(faktor):
    return factorial(faktor)


print("1 = Toplama\n2 = Çıkartma\n3 = çarpma\n4 = Bölme\n5 = Kök alma\n6 = Faktoriyyel alma")
sor = int(input("Yapmak İstediğiniz İşlem (1,2,3,4,5,6) şeklinde giriniz : "))
num1 = int(input("Birinici Sayı : "))
num2 = int(input("İkinci Sayı : "))
kok = int(input("Kök Almak istediğiniz Sayı : "))
faktor = int(input("Faktoriyelini almak istediğiniz sayı : "))

if sor == 1:
    print(num1, "+", num2, "=", topla(num1, num2))

elif sor == 2:
    print(num1, "-", num2, "=", cikar(num1, num2))

elif sor == 3:
    print(num1, "*", num2, "=", carp(num1, num2))

elif sor == 4:
    print(num1, "/", num2, "=", bol(num1, num2))

elif sor == 5:
    print(kok, "=", kok_al(kok))

elif sor == 6:
    print(faktor, "=", faktoriel(faktor))
else:
    print("Sadece yapmak istediğin işleme bir sayı belirt ! ")
