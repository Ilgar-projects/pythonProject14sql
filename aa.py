import sqlite3

title = input('Ведите название фильма ')
def search_resuits(title):

    with sqlite3.connect("netflix.db") as connectiom:
        cursor = connectiom.cursor()
        cursor.execute(f'''SELECT title, country, release_year, listed_in, description 
                          FROM netflix
                          WHERE title='{title}' and country !=''
                          ORDER BY release_year DESC
                          limit 1 ''')
        # s = []
        # print(cursor.fetchall())
    for row in cursor.fetchall():
            #    s.append(row[0][0])
        print(row)
print(search_resuits(title))

