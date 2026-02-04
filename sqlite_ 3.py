import sqlite3


# 1. Konekcija
# conn = sqlite3.connect('chinook.db')
with sqlite3.connect('chinook.db') as conn:

    # 2. Cursor
    c = conn.cursor()

    # 3. EXECUTE
        # INSERT INTO customers (firstname, lastname, address, city, country, postalcode, phone, email, supportrepid)
        #        VALUES('Zlatan', 'Stipisic', 'Neka ulica 1', 'Split', 'Hrvatska', '21000', '+385 21 1234 567', 'gibonni@gibo.hr', 5)
    c.execute('''
        INSERT INTO customers (firstname, lastname, address, city, country, postalcode, phone, email, supportrepid)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', ('Ivo', 'Robic', 'Slavonija', 'Rijeka', 'Hrvatska', '51000', '+385 51 9876 543', 'ivo@robic.hr', 4))


    # 3.1. dohvat -> FETCH - ako je INSERT, UPDATE i DELETE onda nema fetch*
    # data_from_db = c.fetchall()
    # print(data_from_db)

    # 3.2. promjena u bazi -> COMMIT
    # Ako je SELECT ili dohvat, onda nema COMMIT jer ne radimo nikakve promjene
    # conn.commit()

    # 4. CLOSE - NE TREBA JER KORISTIMO WITH
    # c.close()
    # conn.close()
