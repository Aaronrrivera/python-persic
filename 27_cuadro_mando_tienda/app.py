'''
*Al seleccionar una tienda se mostrará:
Una tabla con la información de la tienda.
-Debajo de esa tabla:
total de facturación
total de gastos del personal
mes con mayor facturación

*Al seleccionar un mes se mostrará:
Una tabla con los datos de ese mes.
-Debajo de esa tabla:
media de facturación de todas las tiendas
-Tienda con mayor gasto de personal
'''
import streamlit as st
import tiendas_repository as repo

tienda_sel=None
mes_sel=None

with st.sidebar:
    st.subheader("Filtro de datos")
    datos_tienda=st.selectbox("Seleccione tienda",repo.tiendas())
    datos_mes=st.selectbox("seleccione mes", repo.mes())





#--------------------------------------------------------
'''
df = repo.cargar_datos()

st.title(" Tiendas muy chulas y molonas")

tab1, tab2 = st.tabs(["Por tienda","Por mes"])




saludo=""
with st.sidebar:
    st.write("Menú navegación")
    st.text_input("Dato:")
    if st.button("pulsar"):
        st.write("ha pulsado")
        saludo="Estoy en navegación"
        
        
saludo=""
with st.sidebar:
    st.write("Menú navegación")
    st.text_input("Dato:")
    if st.button("pulsar"):
        st.write("ha pulsado")
        saludo="Estoy en navegación"
'''