import streamlit as st
libros=[]

tab_nuevo,tab_todos,tab_buscar,tab_precios=st.tabs(["Nuevo libro","Mostrar todos","Buscar por título","Libros por precio máximo"])
with tab_nuevo:
    titulo=st.text_input("Introduce título:")
    autor=st.text_input("Introduce autor:")
    precio=st.number_input("Introduce precio:")
    if st.button("Guardar libro"):
        libros.append({"titulo": titulo, "autor": autor, "precio": precio})
with tab_buscar:
    titulo=st.text_input("Introduce el título del libro a buscar: ")
    if st.button("Buscar", key="boton1"):
        libs=list(filter(lambda lib:lib["titulo"].lower()==titulo.lower(),libros))
        if libs:
            st.success(f"Titulo: {libs[0]["titulo"]}, Autor: {libs[0]["autor"]}, Precio: {libs[0]["precio"]}")
        else:
            st.error("Libro no encontrado")
with tab_todos:
    st.title("Listado de libros")
    st.table(libros)
with tab_precios:
    precio_max=st.text_input("Introduce precio máximo")
    if st.button("Buscar",key="boton2"):
        st.table(list(filter(lambda lib:lib["precio"]<=float(precio_max),libros)))
with tab_tienda:
    col_tienda,col_direccion,col_imagen=st.columns(3)
    col_tienda.write("**Nombre tienda**")
    col_direccion.write("**Dirección tienda**")
    col_imagen.write("**Foto**")
    tiendas=[{"nombre":"tienda 1","direccion":"dir1","foto":"tienda.jpg"},
             {"nombre":"tienda 2","direccion":"dir2","foto":"tienda.jpg"},
             {"nombre":"tienda 3","direccion":"dir3","foto":"tienda.jpg"}]
    for tienda in tiendas:
        col_tienda,col_direccion,col_imagen=st.columns(3)
        col_tienda.write(tienda["nombre"])
        col_direccion.write(tienda["direccion"])
        col_imagen.image(tienda["foto"])