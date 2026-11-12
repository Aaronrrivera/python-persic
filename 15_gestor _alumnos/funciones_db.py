'''
Proyecto gestión de alumnos:

-Alta de alumnos: A través de una ventana, se solicitan los datos de un
nuevo alumno y se guardan en la base de datos. No se admiten dnis duplicados
si se proporciona un dni que ya existe, el alumno no se añade
y se avisa mediante un mensaje al usuario

-Busqueda de alumnos por curso. Se selecciona un curso en un combo
y debajo se muestra una tabla con los datos de todos los alumnos
de ese curso. En cada fila, aparecerá un botón para borrar a ese alumno

-Busqueda de alumno por dni. Se introduce el dni de un alumno
y se muestran todos sus datos, si no existe, mensaje de advertencia.
'''
import mysql.connector as con
"""
def conectar():
    return con.connect (host="localhost",
                        user="root",
                        password="root"
                        port=3306,
                        database="universidad")

def buscar_alumno(dni):
    sql="select * from alumnos where dni=%s"
    cursor=crear_conexion().curosr(dictionary=True)
    cursor.execute(sql,((dni,)))
    resultado=cursor.fetchone() #devuelve al alumno con ese dni, sino devuelve non
    db.close()
    return resultado
    
def buscar_alumnos_curso(curso):
    sql="select * from alumnos where curso=%s"
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(sql(curso,))
    resultado=cursor.fetchone()
    db.close()
    return resultado
        
    

def alta_alumno(dni,nombre,email,cursos,nota):
    conexion = conectar()
    cursor = conexion.cursor()

def eliminar_alumno(dni):
    conexion = conectar()
    cursor = conexion.cursor()

def cursos():
"""
import mysql.connector as con
def crear_conexion():
    return con.connect(host="localhost",
               user="root",
               password="root",
               port=3306,
               database="universidad")
    
def buscar_alumno(dni):
    sql="select * from alumnos where dni=%s"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql,(dni,))
    resultado= cursor.fetchone() #Devuelve el alumno con ese dni. Si no existe devuelve None
    db.close()
    return resultado
def buscar_alumnos_curso(curso):
    sql="select * from alumnos where curso=%s"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql,(curso,))
    resultado=cursor.fetchall()
    db.close()
    return resultado
def alta_alumno(dni,nombre,email,curso,nota):
    sql="insert alumnos(dni,nombre,email,curso,nota) values(%s,%s,%s,%s,%s)"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(dni,nombre,email,curso,nota))
    db.commit()
    db.close()
def eliminar_alumno(dni):
    sql="delete from alumnos where dni=%s"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(dni,))  
    db.commit()
    db.close()  
def cursos():
    sql="select distinct(curso) from alumnos"
    db=crear_conexion()
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql)
    resultado=cursor.fetchall() #[{"curso":"Python","curso":"Java"}]
    resultado=[c["curso"] for c in resultado]
    db.close()
    return resultado
def actualizar(dni,nombre,email,curso,nota):
    sql="update alumnos set nombre=%s, email=%s, curso=%s, nota=%s where dni=%s"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(nombre,email,curso,nota,dni))
    db.commit()
    db.close()