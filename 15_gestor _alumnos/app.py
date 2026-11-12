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
import streamlit as st 

import funciones_db as opbd 

tab_nuevo_alumno,tab_alumnos_cursos,tap_buscar_alumno,tab_actualizar=st.tabs(["Nuevo alumno","buscar por curso","buscar por DNI"])

with tab_nuevo_alumno:
    dni=st.text_input("DNI del alumno: ")
    nombre=st.text_input("Nombre del alumno: ")
    email=st.text_input("Email del alumno: ")
    curso=st.text_input("Curso del alumno: ")
    nota=st.text_input("Nota del alumno: ")
    if st.button("Alta de alumno"):
        if opbd.buscar_alumno(dni)==None:
            opbd.alta_alumno(dni,nombre,email,curso,nota)
        else:
            st.toast("DNI ya existente")

with tab_alumnos_cursos:
    st.selectbox("Selecciona curso",opbd.cursos())
    if curso:
            col_nombre,col_email,col_dni,col_nota,col_eliminar=st.colums([2,3,1,1,2])
            alumnos=opbd.buscar_alumnos_curso(curso)
            for a in alumnos:
                col_nombre.write(a["nombre"])
                col_email.write(a["email"])
                col_dni.write(a["dni"])
                col_nota.write(a["nota"])
                if col_eliminar.button("Eliminar",key=f"eliminar{a["dni"]}"):
                    opbd.eliminar_alumno(a["dni"])
                    st.rerun()

with tab_buscar_alumno:
    dni=st.text_input("Introduce el DNI: ")
    if st.button("Buscar alumno") or dni:
        alumno=opbd.buscar_alumno(dni)
        if alumno==None:
            st.toast("El dni no existe!!")
        else:
            nombre=st.text_input("Nombre :",value=alumno["nombre"])
            email=st.text_input("Email :",value=alumno["email"])
            curso=st.text_input("Curso :",value=alumno["curso"])
            nota=st.text_input("Nota :",value=alumno["nota"])
            if st.button("Actualizar"):
                opbd.actualizar(dni,nombre,email,curso,nota)
           
            

  