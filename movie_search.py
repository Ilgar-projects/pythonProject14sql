import sqlite3

title = input('Ведите название фильма ')
def search_results(title):

    with sqlite3.connect("netflix.db") as connectiom:
        cursor = connectiom.cursor()
        cursor.execute(f'''SELECT title, country, release_year, listed_in, description 
                          FROM netflix
                          WHERE title='{title}' and country !=''
                          ORDER BY release_year DESC
                          limit 1 ''')

    sql_result = cursor.fetchall()[0]
    info = {
    		"title": sql_result[0],
    		"country": sql_result[1],
    		"release_year": sql_result[2],
    		"genre": sql_result[3],
    		"description": sql_result[4]
     }
    print(info)

result = search_results(title)
print(result) # Disenchantment

