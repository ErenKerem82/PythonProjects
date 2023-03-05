# class öğrenimi üzerine bir proje

# Inheritance -kalıtım- alanı üzerine küçük bir hatırlatma çalışması
# bir şirketteki çalışanları ve üst düzey çalışanları gösteriyor

class calisanlar:
    def __init__(self, isim, soyisim, alan):
        self.isim = isim
        self.soyisim = soyisim
        self.alan = alan

    def bilgileri_goster(self):
        return "İsim :{}\nSoyisim :{}\nÇalıştığı Alan :{}".format(self.isim, self.soyisim, self.alan)


cayci = calisanlar("Ahmet", "arslan", "Çaycı")
temizlikci = calisanlar("Ayşe", "arslan", "Temizlik")
guvenlik = calisanlar("Fetullah", "Yaprak", "Güvenlik")
vale = calisanlar("Berkcan", "Ay", "Vale")
sekreter = calisanlar("Gamze", "Topoğlu", "Sekreter")


class developers(calisanlar):
    def __init__(self, isim, soyisim, alan, mertebe):
        super().__init__(isim, soyisim, alan)
        self.mertebe = mertebe

    def bilgileri_goster(self):
        return "İsim :{}\nSoyisim :{}\nÇalıştığı Alan :{}\nBulunduğu Mertebe :{}".format(self.isim, self.soyisim, self.alan, self.mertebe)


jr = developers("Serdar", "güneş", "Yapay Zeka", "Junior")
jr2 = developers("Taha", "Metin", "Oyun", "Junior")
medium = developers("Yusuf", "kılıçarslan", "Robotik", "Medium")
medium2 = developers("Elon", "Musk", "Robotik", "Medium")
senior = developers("Cihan", "tokgöz", "Yapay Zeka", "Senior")
pro = developers("Aziz", "yaz", "Yazılım", "Professional")


print(cayci.bilgileri_goster())
print("--------------------------------------------------------")
print(temizlikci.bilgileri_goster())
print("--------------------------------------------------------")
print(guvenlik.bilgileri_goster())
print("--------------------------------------------------------")
print(vale.bilgileri_goster())
print("--------------------------------------------------------")
print(sekreter.bilgileri_goster())
print("--------------------------------------------------------")
print("--------------------------------------------------------")
print(jr.bilgileri_goster())
print("--------------------------------------------------------")
print(jr2.bilgileri_goster())
print("--------------------------------------------------------")
print(medium.bilgileri_goster())
print("--------------------------------------------------------")
print(senior.bilgileri_goster())
print("--------------------------------------------------------")
print(pro.bilgileri_goster())
print("--------------------------------------------------------")
