import streamlit as st
import pandas as pd
from pickle import load
st.title('Diabetic Check Up')
st.write("Are you a diabetic ?")
def get_input():
    Pregnancy  = st.number_input('Enter the number of Pregnancy')
    Glucose = st.slider('Glucose Level',min_value=0, max_value=400 )
    BloodPressure = st.slider('BloodPressure',min_value=0, max_value=500 )
    SkinThickness = st.slider('SkinThickness',min_value=0, max_value=100 )
    Insulin = st.slider('Insulin',min_value=0, max_value=1000 )
    BMI = st.slider('BMI',min_value=0, max_value=100 )
    DiabetesPedigreeFunction = st.slider('DiabetesPedigreeFunction',min_value=0, max_value=1)
    Age = st.number_input('Enter Age')
    data = {
        'Pregnancies' : Pregnancy,
        'Glucose' :  Glucose,     
        'BloodPressure' :   BloodPressure,
        'SkinThickness' : SkinThickness,
        'Insulin' :   Insulin,
        'BMI' : BMI,
        'DiabetesPedigreeFunction' : DiabetesPedigreeFunction,
        'Age' : Age
    }
    input_df = pd.DataFrame(data , index=[0])
    return input_df

features = get_input()
loaded_model = load(open('model.pkl' ,'rb'))
if st.button('submit'):
    st.write(features)
    result = loaded_model.predict(features)
    if result == 0 :
        res = "No ! Patient is non-diabetic"
    else:
        res = "Yes ! Patient is diabetic"
    st.write(res)

    
    