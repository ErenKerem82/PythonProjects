# 1.sınav notu - ve - 2.sınav notu ort hesaplama

# 1.sınav notunu alalım
bir_sınav = int(input("    1.yazılı Notu :"))

# 2.sınav notunu alalım
iki_sınav = int(input("\n    2.yazılı Notu :"))

sonuç = (bir_sınav + iki_sınav)/2
print("           ", sonuç)

"""
0-45 arası KALDINIZ

45-60 arası 2

60-70 arası 3

70-85 arası 4

85-100 arası 5

"""
if sonuç <= 45:
    print("-------BU DERSTEN KALDIN-------")

elif sonuç > 45 and sonuç < 60:
    print("-------2-------")

elif sonuç >= 60 and sonuç < 70:
    print("-------3-------")

elif sonuç >= 70 and sonuç < 85:
    print("-------4-------")

elif sonuç >= 85 and sonuç <= 100:
    print("-Tebrikler--5--")

else:
    print("Notlarınızı KOntrol ediniz !")
