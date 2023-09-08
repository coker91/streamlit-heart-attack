import pickle
import numpy as np
import streamlit as st

#load saved model
model = pickle.load(open('penyakit_jantung.sav','rb'))

#judul web
st.title('Prediksi Penyakit Jantung')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Umur')
    trestbps = st.number_input('Tekanan Darah')
    restecg = st.number_input('Hasil EKG')
    oldpeak = st.number_input('Depresi ST')
    thal = st.number_input('Nilai Thal')


with col2:
    sex = st.number_input('Jenis Kelamin')
    chol = st.number_input('Nilai Kolesterol')
    thalach = st.number_input('Detak Jantung Maksimal')
    slope = st.number_input('Slope')

with col3:
    cp = st.number_input('Tipe Nyeri Dada')
    fbs = st.number_input('Gula Darah')
    exang = st.number_input('Induksi Angina')
    ca = st.number_input('Nilai CA')

# code for prediction
heart_diagnosis = ''

#create button
if st.button('Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    if (heart_prediction[0] == 1):
        heart_diagnosis = 'Pasien mengidap penyakit jantung'
    else:
        heart_diagnosis = 'Pasien tidak mengidap penyakit jantung'

st.success(heart_diagnosis)








