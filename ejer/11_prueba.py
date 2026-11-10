import streamlit as st
nombre=st.text_input("nombre:")
edad=st.number_input("edad")
afiliado=st.checkbox("afiliado")
curso=st.radio("elige curso:",["python","c++","java"])
centro=st.selectboxbox("elige centro",["leganes","getafe","alcobendas","sanblas"])
if st.button("pulsar"):
    st.success(f"te llamas{nombre}, tienes{edad} años, has elegido el curso {curso} en el centro{centro}")
    
    aula=[
    {},
    {},
    {}
]
    st.stable(aula)