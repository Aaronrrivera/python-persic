import pymongo as pm
url="mongodb://localhost:27017"
serv=pm.MongoClient(url)
col_libros=serv.libreria.libros
col_libros.insert_one({"isbn":"jh12","titulo":"cronicas de sidario","pafinas":250,"categoria":"cronica","precio":23})
col_libros.insert_one({'isbn': 'yu12', 'titulo': 'C++', 'paginas': 520, 'categoria': 'programación', 'precio': 40.7})
col_libros.update_one({"isbn":"yu12"},{"$inc":{"precio":20}})
libros=serv.libreria.libros.find({"categoria":"miedo"})
for lb in libros:
    print(lb)
serv.close()