import streamlit as st 

from qr_generator import generate_qr

st.set_page_config(page_title = "SmartQR", page_icon = "")

st.title('SmartQR Web Version')
st.write('Generates QR codes instantly from text or urls')

data = st.text_input('enter text or url.')

