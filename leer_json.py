import json
#ARMAR UNA ESTRUCTURA
posicion = 0
with open("books_to_clean.json",encoding="utf-8") as j:
    data= json.load(j)

json=''''

'''

for x in range(0,45640):
    json += '''
    {
    "model":"blog.Libros",
    "fields":{
        "title": data[x]["title"],
        "authors": data[x]["authors"],
        "average_rating": data[x]["average_rating"],
        "isbn": data[x]["isbn"],
        "isbn13": data[x]["isbn13"],
        "language_code": data[x]["language_code"],
        "num_pages": data[x]["num_pages"],
        "ratings_count": data[x]["ratings_count"],
        "text_reviews_count": data[x]["text_reviews_count"],
        "publication_date": data[x]["publication_date"],
        "publisher": data[x]["publisher"],
        
    }
}

    '''

print(json)



