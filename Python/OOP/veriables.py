class calisan:
    zam_orani = 1.1

    def __init__(self, isim, maas):
        self.isim = isim
        self.maas = maas


calisan1 = calisan("Kerem Kenan Eren", 10.000)
calisan2 = calisan("Yusuf Eren", 10.000)

calisan2.zam_orani = 1.8


print(calisan2.zam_orani)

print(calisan1.__dict__)
print(calisan2.__dict__)
