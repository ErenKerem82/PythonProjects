class kisi:
    person = 0

    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        kisi.person += 1

    def bilgilerini_soyle(self):
        return f"isim :{self.isim}  yas :{self.yas}"

    @classmethod
    def ozel_eleman(cls, str_):
        isim, yas = str_.split("-")
        return cls(isim, yas)


kisi1 = kisi("kerem", "15")
kisi2 = kisi("yusuf", "20")
ozelkisi = kisi.ozel_eleman("Mustafa - 45")


print(kisi1.bilgilerini_soyle())
print(kisi2.bilgilerini_soyle())
print(ozelkisi.isim)

print("personel sayisi :", kisi.person)
