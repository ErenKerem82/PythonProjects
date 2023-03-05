import sqlite3 as sql


def veri_ekle(isim, yas, maas, Puan):
    conn = sql.connect("istatik.db")
    cursor = conn.cursor()
    command = "INSERT INTO istatik VALUES {}"

    data = (isim, yas, maas, Puan)
    cursor.execute(command.format(data))
    conn.commit()
    conn.close()


def veri_sil():
    conn = sql.connect("istatistik.db")
    cursor = conn.cursor()
    command = "DELETE from CALİSANLAR WHERE * = '{}' "

    cursor.execute(command.format())
    conn.commit()
    conn.close()


# db = sql.connect("istatik.db")
# db.cursor

# db.execute("""CREATE TABLE istatik(isim , yas , maas , Puan)""")

# db.commit()
# db.close()
