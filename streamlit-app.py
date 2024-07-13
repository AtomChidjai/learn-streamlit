import streamlit as st
import pandas as pd
import numpy as np

st.title("🐳 This is for learning Streamlit")
st.write("Streamlit App")

placeholder = st.empty()

status = st.radio("Select an option : ", [1, 2])

if status == 1:
    placeholder.success("Success")
else:
    placeholder.warning("Failed")

## making a slider with st.slider

x = st.slider('Square Slider')

st.write(x, 'square : ', x * x)

## Using np and pd lib for making a random numbers chart (st.area_chart)

st.header("Random Number Chart")
my_chart = pd.DataFrame(np.random.randn(20,3), columns=["a", "b", "c"])
st.area_chart(my_chart)