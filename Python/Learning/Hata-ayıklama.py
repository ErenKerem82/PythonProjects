try:
    a = 2
    b = 6
    if b == 0:
        raise ZeroDivisionError
        """
        istediğimiz except komutununu koşul ile
        sağlayabiliriz " raise "
        ve herhangi bir hata olmasınada gerek yok   
        b == 5 de diyebilirdim...    
        """
    c = a/b
    x = 4
    d = x
    isim = "ali"
    karakter = isim[2]

except ZeroDivisionError:
    print("Sıfır bölünemez !")

except NameError:
    print("Bu değişken daha önce tanımlanmamış !")

except IndexError:
    print("Böyle bir index bulunmuyor !")


# buradaki hataların dışına bir hata varsa exception uygula:
except Exception:
    print("Bilinmeyen bir hata oluştu")


# eğer hiç hata yoksa else bloğu çalışır
else:
    print("hatasız koddan zarar gelmez , except komutundan hayır gelmez")
