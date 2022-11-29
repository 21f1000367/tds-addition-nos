import streamlit as st
import pandas as pd
from sklearn import datasets

st.write("""
# Addition of Two Given Numbers

This app returns the sum of two given numbers
""")
#Get Input

st.header('User Input Parameters')
number1 = st.number_input("NUMBER_1")
number2 = st.number_input("NUMBER_2")
   
data = {'NUMBER_1': number1,
        'NUMBER_2': number2
        }

add = number1 + number2

st.subheader('Sum of the two given numbers')
st.write(add)
