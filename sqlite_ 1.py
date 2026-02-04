import sqlite3


artist_id = int(input('Upisite ID izvodaca: '))
artist_id_end = int(input('Upisite ID izvodaca: '))


# 1. Konekcija
conn = sqlite3.connect('chinook.db')

# 2. Cursor
c = conn.cursor()

# 3. EXECUTE
    # -- SELECT * FROM albums
    # -- SELECT Title FROM albums
    # -- SELECT * FROM albums WHERE artistid = 20

    # -- SELECT * FROM albums WHERE artistid BETWEEN 10 AND 15
    # -- SELECT * FROM albums WHERE title like 'Bi%'
# c.execute('''SELECT * FROM albums''')
# c.execute('''SELECT Title FROM albums''')
# c.execute('''SELECT * FROM albums WHERE artistid = 20''')
# c.execute('''SELECT * FROM albums WHERE artistid = ?''', (artist_id,))
c.execute('''SELECT * FROM albums WHERE artistid BETWEEN ? AND ?''', (artist_id, artist_id_end))


# 3.1. dohvat -> FETCH
data_from_db = c.fetchall()
print(data_from_db)

# 3.2. promjena u bazi -> COMMIT
# Ako je SELECT ili dohvat, onda nema COMMIT jer ne radimo nikakve promjene

# 4. CLOSE
c.close()
conn.close()
