import streamlit as st
import pandas as pd
import pickle
import sklearn
from sklearn import preprocessing

loaded_model = pickle.load(open("sale-advertising-model.h5","rb")

                        


st.header("My first Streamlit App")

st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')
if show:
    st.write(pd.DataFrame({
    'Students': ['John', 'Lofa', 'Siti', 'Amy'],
    'Attendance Status': ['yes', 'yes', 'yes', 'no']
    }))
