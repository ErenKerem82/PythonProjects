class calisan:
    zam_orani = 1.1

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.gmail.com"

    def bilgilerini_goster(self):
        return "İsim :{}\n Soyisim :{}\n  Maaş :{}\n  Email :{}\n".format(self.isim, self.soyisim, self.maas, self.email)


calisan1 = calisan("Mustafa", "Eren", 10.000,)
calisan2 = calisan("Yusuf", "Eren", 8.000,)


class yazilimci(calisan):
    def __init__(self, isim, soyisim, maas, bildigi_dil):
        super().__init__(isim, soyisim, maas)
        self.bildigi_dil = bildigi_dil

    zam_orani = 1.2

    def bilgilerini_goster(self):
        return "İsim :{}\nSoyisim :{}\nMaaş :{}\nEmail :{}\nBidiği Dil :{}\n".format(self.isim, self.soyisim, self.maas, self.email, self.bildigi_dil)


yazilimci1 = yazilimci("Kerem", "Eren", 10000, "Python")
yazilimci2 = yazilimci("Elon", "Musk", 4500, "html , Css")

print(yazilimci2.bilgilerini_goster())
print(yazilimci1.bilgilerini_goster())
