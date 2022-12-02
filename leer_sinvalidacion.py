import json


with open("books_to_clean.json",encoding="utf-8") as j:
    data= json.load(j)

dicc1={}
lista=[]

for x in range(0,11127):
    dicc1 ={

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
        "publisher": data[x]["publisher"]    

        }
    }

    lista.append(dicc1)

#print(lista)


with open("nueva_data.json",'w') as n:
    json.dump(lista,n)