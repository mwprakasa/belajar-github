import streamlit as st

st.title('Tes Pertama')
nama = st.text_input('Nama kamu')
if nama:
   st.write(f'Halo, {nama}!')
