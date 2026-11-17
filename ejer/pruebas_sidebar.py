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

saludo=""
with st.sidebar:
    st.write("Menú navegación")
    st.text_input("Dato:")
    if st.button("pulsar"):
        st.write("ha pulsado")
        saludo="Estoy en navegación"