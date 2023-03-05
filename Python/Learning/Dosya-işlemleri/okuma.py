# DOSYA İŞLEMLERİ

# utf-8 Türkçe dışı karakterleri düzeltir
dosya = open("Dosya-kipleri.txt", "r", encoding="utf-8")

print(dosya.read())

dosya.close()  # dosyayı kapatmak çok önemli

# yazmak için de "r" yerine "w" ve read yerine "write" yazmamız yeterli
