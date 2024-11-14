import streamlit as st
import pandas as pd
import seaborn as sns
import pickle

st.write("Advertising-Sales App")  
st.write("This app predicts the **Sales** value!")

st.sidebar.header('User Input Parameters')

def user_input_features():  #This is user function
    tv = st.sidebar.slider('TV', 0.0, 400.0, 0.0)  #('lable name', min value, max value, default value)
    radio = st.sidebar.slider('Radio',0.0, 400.0, 0.0)
    newspaper = st.sidebar.slider('Newspaper', 0.0, 200.0, 0.0)
    data = {'TV': tv,  
            'Radio': radio,
            'Newspaper': newspaper}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

modelsales = pickle.load(open("modelsales.h5", "rb")) #rb: read binary
new_pred = modelsales.predict(df) # testing (examination)

st.subheader('Prediction')
st.write(new_pred)
