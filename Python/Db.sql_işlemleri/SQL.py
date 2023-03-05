import sqlite3 as sql


# For ile Veri ekleme
"""
conn = sql.connect("Dersler.db")

cursor = conn.cursor()

datas = [("Fizik", "Tarih", "Edebiyat"), ("Kimya", "Kimya",
                                          "İngilizce"), ("Biyoloji", "Biyoloji", "Tarih")]

command = "INSERT INTO LESSONS VALUES {}"
for data in datas:
    cursor.execute(command.format(data))
    print("Veri başarıyla eklendi....")


conn.commit()
conn.close()

print("oldu")

"""

# Fonksiyon ile Veri ekleme
"""
def Insert(sayisal, tm, sozel):
    conn = sql.connect("Dersler.db")
    cursor = conn.cursor()
    command = "INSERT INTO LESSONS VALUES {}"

    data = (sayisal, tm, sozel)
    cursor.execute(command.format(data))
    conn.commit()
    conn.close()


Insert("Edebiyat", "İngilizce", "Felsefe")
"""


# Fonksiyon ile veri silme
"""
def Delete(sayisal):
    conn = sql.connect("Dersler.db")
    cursor = conn.cursor()
    delete_command = "DELETE from LESSONS WHERE sayisal = '{}' "

    cursor.execute(delete_command.format(sayisal))
    conn.commit()
    conn.close()


Delete("Fizik")

"""

# Fonksiyon ile veriyi terminale yazdırma
"""
def veri_yazma():
    conn = sql.connect("Dersler.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * from LESSONS  ")
    list_all = cursor.fetchall()

    for satır in list_all:
        print(satır)

    conn.commit()
    conn.close()


veri_yazma()

"""
