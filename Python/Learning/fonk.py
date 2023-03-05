# varsayılan fonk. değeri
def kuvvetAl(x, y=2):
    return y**x


print(kuvvetAl(3))

# Birden fazla parametre gerektiren fonk. " * " kullanırız. Değerleri List halinde saklar..


def topla(*sayilar):
    return sum(sayilar)
    # sum fonksiyonu : Dizi içerisindeki değerlerin toplamını alır.


print(topla(50, 50, 50, 40, 10, 20, 30))

# " ** " ise değerleri " key , value " halinde Saklar.(Yani dictionary objesi olarak..)


def kullanicilar(**karaktersayisi):
    for key, value in karaktersayisi.items():
        print(key, value)


print(kullanicilar(isim=": Kerem", yas=": 16", suanki_Mutlulu_kDurumu=": %81"))


# değişken kuralı

def bol(a, b):
    global c    # c değişkenini evrensel yaptı
    c = 10
    print((a/b)*c)


bol(10, 2)
print(c)
