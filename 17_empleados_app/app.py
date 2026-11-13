"""
-Alta de nuevos empleados
-Filtrar empleados: opcion por departamento o rango salarial.
Si se elige departamento, se muestra combo con departamentos y al
seleccionar uno muestra empleados. Si se elige rango salarial,
aparecen dos campos de textos (min y max) y un botón que al pulsarlo
muestra empleados
"""
import streamlit as st 
import empleados_repository as repo

tab_nuevo, tab_filtrar_empleados,tab_actualizar=st.tabs(["nuevo empleado","busqueda de empleados","actualizar datos"])

with tab_nuevo:
    empleado=st.text_input("Nomvre del empleado: ")
    edad=st.number_input("edad del empleado: ")
    salario=st.number_input("salario del empleado: ")
    departamento=st.text_input("departamento del empleado: ")
    if st.button("Alta empleado"):
       repo.nuevo_empleado(empleado,edad,salario,departamento)
       st.toast("empleado agregado") 

with tab_filtrar_empleados:
    opciones= st.selectbox("filtrar empleados por departamento: ","filtrar empleados por rango salarial")
    if opciones =="filtrar empleados por departamento: ":
        
#muestra la tabla con todos los empleados, permitiendo la modificacion de sus datos mediante un boton actualizar, se grabarán los cambios en la base de datos
resultado=st.data_editor(datos)
with tab_actualizar:
    resultado=st.data_editor(repo.empleados(),disabled=["_id"])
    if st.button("Actualizar")
    repo.actualizar