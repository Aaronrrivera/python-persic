import polars as pl

datos = [ 
    {"nombre": "Ana", "edad": 25, "salario": 25000,"departamento":"ventas"}, 
    {"nombre": "Luis", "edad": 32, "salario": 32000,"departamento":"informática"}, 
    {"nombre": "Marta", "edad": 28, "salario": 28000,"departamento":"informática"}, 
    {"nombre": "Pedro", "edad": 41, "salario": 41000,"departamento":"ventas"} 
]
df = pl.DataFrame(datos) 
print(df)
#acseso a filas y columnas
print(df["edad"].to_list()) #columna en lista de valores
print(df.row(0,named=True)) #dicccionario con los datos de la lista
print(df.to_dicts())#Convierte todo el dataframe en una lista de diccionarios
#filtrado
print(df.filter(pl.col("salario")>30000))
print(df.filter((pl.col("salario")>30000)&(pl.col("edad")<50)))

#ordenacion
print(df.sort(by="edad",descending=False))
print(df.sort("salario",descending=True)#ordena descendente en salario
      .row(0)[0])#se queda con la primera fila, y de esta, con el primer elemento

#funciones calculos: min(), max(), mean(), count(), unique()

#seleccion
resultado=df.select(pl.col("salario").mean().alias("salrio medio"), pl.col("edad").mean().alias("media edad"))
print(resultado)

print(df["departamento"].unique().to_list())#muestra lista de departamentos sin duplicados

#agrupacio de un frame

df.group_by("departamento").agg(pl.col("salario").mean().alias("salario medio"), 
                                pl.col("nombre").count().alias("total empleados"))

#recorrido de un dataframe
for element in df.iter_rows(named=True):#como diccionarios
    print(element)