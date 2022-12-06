import pickle
import streamlit as st

heart_model = pickle.load(open('heart_model.sav', 'rb'))

st.title('Prediksi Penyakit Jantung ')

col1, col2, col3 = st.columns(3)

with col1 :
    age = st.text_input ('Input Nilai age')
with col2 :
    sex = st.text_input ('Input Nilai clump sex')
with col3 :
    cp = st.text_input ('Input Nilai size cp')
with col1 :
    trestbps = st.text_input ('Input Nilai shape trestbps')
with col2 :
    chol = st.text_input ('Input Nilai marginal chol')
with col3 :
    fbs = st.text_input ('Input Nilai epithelial fbs')
with col1 :
    restecg = st.text_input ('Input Nilai bare restecg')
with col2 :
    thalach = st.text_input ('Input Nilai bland thalach')
with col3 :
    exang = st.text_input ('Input Nilai exang')
with col1 :
    oldpeak = st.text_input ('Input Nilai oldpeak')
with col2 :
    slope = st.text_input ('Input Nilai bland slope')
with col3 :
    ca = st.text_input ('Input Nilai ca')
with col1 :
    thal = st.text_input ('Input Nilai thal')

heart_diagnosis = ''

if st.button('Test Prediksi Penyakit Jantung') :
    heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, ]])

    if (heart_prediction[0] == 0):
        heart_diagnosis = 'Tidak terkena penyakit'
    else : heart_diagnosis = 'Terkena penyakit'
st.success(heart_diagnosis)