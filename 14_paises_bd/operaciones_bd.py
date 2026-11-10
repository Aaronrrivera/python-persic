import mysql.connector as con
def crear_conexion():
    return con.connect(t(host="localhost",
               user="root",
               password="root",
               port="3306",
               database="mundo"))
    
def borrar_tablas():
    db=crear_conexion
    cursor=db.cursor()
    cursor.execute("delete from continentes")
    cursor.execute("delete from paises")
    db.commit()
    db.close()
def crear_continentes(continentes):
    sql_insert="insert into continentes(continente)(%s)"
    db=crear_conexion
    cursor=db.cursor()
    listado=[(c,) for c in continentes]
    cursor.executemany(sql_insert,listado)
    db.commit()
    db.close()
def devolver_continentes():
    sql="select * from continentes"
    db=crear_conexion
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql)
    resultado = cursor.fetchall()
    db.close()
    return resultado 
def crear_paises(paises): #[{"pais":"pais1","poblacion":333,"bandera":"jadask","idcontinente":2},]
    db=crear_conexion
    cursor=db.cursor()
    sql_insert="insert into paises(pais,poblacion,bandera,ideContinente) value(%s,%s,%s,%s)"
    lista_tuplas=[tuple(p.values()) for p in paises]
    cursor.executemany(sql_insert,lista_tuplas)
    db.commit()
    db.close()
def paises_por_continente(id_continente):
    sql="select ] from paises where idContinentes=%s"
    db=crear_conexion
    cursor=db.cursor(dictionary=True)
    cursor.execute(sql)
    resultado=cursor.fetchall()
    
    db.close()
    return resultado