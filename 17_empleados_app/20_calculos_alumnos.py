"""
a partit del documento alumnos.json, calcula la nota media global
muestra nota alta de cada curso y el total de alumnos de cada curso

"""
import pandas as pd
df=pd.read_json("alumnos.csv", encoding="UTF-8")
print(f"Nota media global: {df["nota"].mean():.2f}")
grupo=df.groupby("curso").agg(nota_mayor=("nota","max"),total_alumnos=("nombre","count"))
print(grupo)
