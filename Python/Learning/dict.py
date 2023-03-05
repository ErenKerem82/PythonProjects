kerem = {
    "   isim : ": "Kerem Kenan",
    "   soyisim : ": "Eren",
    "   meslek : ": "AI Enginner"
}

yusuf = {
    "   isim : ": "Yusuf",
    "   Soyisim : ": "Eren",
    "   meslek : ": "Mekatronik Mühendisliği"
}

mustafa = {
    "   isim : ": "Mustafa",
    "   soyisim : ": "Eren",
    "   meslek : ": "Tekstil İşçisi"
}


sor = input("Kimi Almak istersiniz :")


if (sor == "Kerem"):
    for key, value in kerem.items():
        print(key, value)

elif (sor == "Yusuf"):
    for key, value in yusuf.items():
        print(key, value)

elif (sor == "Mustafa"):
    for key, value in mustafa.items():
        print(key, value)

else:
    print("  Aradığınız kişi bulunamadı :( ")
