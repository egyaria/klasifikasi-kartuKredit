import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('peminjaman.sav', 'rb'))

st.title('Prediksi Approved Peminjaman Rumah')
c1, c2 = st.columns(2)

with c1:
    Dependents = st.number_input('Jumlah tanggungan')
    Self_Employed = st.number_input('Wiraswasta (0: No, 1: Yes)')
    CoapplicantIncome = st.number_input('Pendapatan peminjam bersama')
    Loan_Amount_Term = st.number_input('Tempo pinjaman (bulan)')
    Property_Area = st.number_input('Area properti yang diajukan')

with c2:
    Education = st.number_input('Pendidikan')
    ApplicantIncome = st.number_input('Pendapatan peminjam')
    LoanAmount = st.number_input('Jumlah pinjaman (ribu dollar)')
    Credit_History = st.number_input('Pernah melakukan pinjaman (0: No, 1: Yes)')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome,
                               LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]])

    if (prediksi [0] == 0):
        prediksi = ('Peminjaman yang diajukan tidak diterima')
    else:
        prediksi = ('Peminjaman yang diajukan diterima')
st.success(prediksi)