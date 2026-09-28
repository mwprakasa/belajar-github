import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


@st.cache_resource
def get_sheet():
    creds = Credentials.from_service_account_info(
        dict(st.secrets["gcp_service_account"]), scopes=SCOPES
    )
    client = gspread.authorize(creds)
    return client.open(st.secrets["sheet_name"]).sheet1


st.title("Form Input Kunjungan")
sheet = get_sheet()

with st.form("form_kunjungan", clear_on_submit=True):
    nama = st.text_input("Nama Sales")
    outlet = st.text_input("Nama Outlet")
    jumlah = st.number_input("Jumlah Order", min_value=0, step=1)
    catatan = st.text_area("Catatan")
    kirim = st.form_submit_button("Simpan")

if kirim:
    if not nama or not outlet:
        st.error("Nama sales dan nama outlet wajib diisi")
    else:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([waktu, nama, outlet, int(jumlah), catatan])
        st.success("Data tersimpan")

st.subheader("10 data terakhir")
rows = sheet.get_all_records()
if rows:
    st.dataframe(rows[-10:][::-1])
else:
    st.write("Belum ada data")
