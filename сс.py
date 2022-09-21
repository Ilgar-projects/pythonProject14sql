import sqlite3


with sqlite3.connect("netflix.db") as connectiom:
    cursor = connectiom.cursor()
    cursor.execute(f'''SELECT title, country, release_year, listed_in, description 
                      FROM netflix
                      WHERE country !=''
                      ORDER BY release_year DESC
                      limit 5



                   ''')

# s = []
# print(cursor.fetchall())
for row in cursor.fetchall():
    #    s.append(row[0][0])
    print(row)

