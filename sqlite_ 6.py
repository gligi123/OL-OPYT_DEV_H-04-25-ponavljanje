import sqlite3


# 1. Konekcija
# conn = sqlite3.connect('chinook.db')
with sqlite3.connect('chinook.db') as conn:

    # 2. Cursor
    c = conn.cursor()

    # 3. EXECUTE
    #   UPDATE customers
    #   SET firstname = 'Ivo Ivan'
    #   WHERE customerid = 60
    c.execute('''
            UPDATE customers
                SET firstname = ?
                WHERE customerid = ?
        ''', ('Ivica', 62))


    # 3.1. dohvat -> FETCH - ako je INSERT, UPDATE i DELETE onda nema fetch*
    # data_from_db = c.fetchall()
    # print(data_from_db)

    # 3.2. promjena u bazi -> COMMIT
    # Ako je SELECT ili dohvat, onda nema COMMIT jer ne radimo nikakve promjene
    # conn.commit()

    # 4. CLOSE - NE TREBA JER KORISTIMO WITH
    # c.close()
    # conn.close()
