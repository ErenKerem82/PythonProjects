# DOSYA İŞLEMLERİ

# eğer dosya içinde birşey yazılıysa onu ""silip""
# kendisi yazar


dosya = open("yazmak.txt", "w", encoding="utf-8")

dosya.write("*  Dosya içine Yazı yazmak \n")
dosya.write("Bu şekilde \n")

dosya.close()  # KAPATMAK ÇOK ÖNEMLİ !
