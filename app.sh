import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Addition of Two Given Numbers

This app returns the sum of two given numbers
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    number1 = st.number_input("NUMBER_1")
    number2 = st.number_input("NUMBER_2")
   
    data = {'NUMBER_1': number1,
            'NUMBER_2': number2
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

add = df['NUMBER_1'] + df['NUMBER_2']

st.subheader('Sum of the two given numbers')
st.write(add[0])
