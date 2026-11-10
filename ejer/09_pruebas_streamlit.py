import streamlit as st 
import time
st.success("todo bien")
mensaje_error=st.error("no bien")
time.sleep(3)
st.empty(mensaje_error)
st.toast("mensaje flotante",duration=)