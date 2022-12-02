import json
import datetime 

with open("books_to_clean.json",encoding="utf-8") as j:
    data= json.load(j)

dicc1={}
lista=[]

for x in range(0,11127):
    #m/d/y  -> m-d-y
    formato_fecha = data[x]["publication_date"].split('/') #divir cuando encuentre un / -> List()
    #print(formato_fecha)
    #print(data[x]["publication_date"])
    if len(formato_fecha) ==3: #valido que existan 3 numeros dentro de los 2 /   -> d/m/Y
    
        if(int(formato_fecha[1])>30): 
            #print(formato_fecha[1] ,'-mes:',formato_fecha[0])
            formato_fecha[1]="30"
            
        fecha = datetime.date(int(formato_fecha[2]),int(formato_fecha[0]),int(formato_fecha[1]))
        
        #if(int(formato_fecha[1])>30):
         #   print(formato_fecha[1] ,'-mes:',formato_fecha[0])
                 
    else:
        #No hay fechas correctas
        #print(data[x]["publication_date"]  ,"- Posicion -> ",data[x]["bookID"])
        #fechanormal= data[x]["publisher"]
        #publisher = data[x]["publication_date"]
        
        fecha =datetime.date(2022, 5, 17)  #Año - mes - dia

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
            "publication_date": str(fecha)  ,
            "publisher": data[x]["publisher"]    

            }
        }

    lista.append(dicc1)

#print(lista)


with open("nueva_data.json",'w') as n:  #crea un archivo json
    json.dump(lista,n)