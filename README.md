# belajar-github
Project latihan belajar Git dan GitHub
import streamlit as st
 
st.title('Tes Pertama')
nama = st.text_input('Maulana')
if nama:
    st.write(f'Halo, {nama}!')
