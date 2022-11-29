import streamlit as st
import pandas as pd

st.write("""
# Addition of Two Given Numbers

This app returns the sum of two given numbers
""")
#Get Input

st.header('User Input Parameters')
number1 = st.number_input("NUMBER_1")
number2 = st.number_input("NUMBER_2")

add = number1 + number2

st.header('Sum of the two given numbers')
st.write(add)
