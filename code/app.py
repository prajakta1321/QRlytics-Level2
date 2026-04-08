import streamlit as st 

from qr_generator import generate_qr

st.set_page_config(page_title = "SmartQR", page_icon = "")

st.title('SmartQR Web Version')
st.write('Generates QR codes instantly from text or urls')

data = st.text_input('enter text or url.')

if st.button('generate QR'):     # button to trigger qr generation
    if not data.strip():         # check if input is empty
        st.error('input cannot be empty.')
    else:
        try:
            filename = generate_qr(data)  # generatre qr and get the filename
            st.success('QR generated successfully:{filename}')
            st.image(filename, caption = 'Generated qr code')   # to show image preview

            with open(filename, 'rb') as file:
                st.download_button(
                    label = 'Download qr',
                    data = file,
                    file_name = filename,
                    mime = 'image/png'
                )
        except Exception as e:
            st.error(f'error:{e}')
