import pandas as pd
import streamlit as st
st.title("Hello")
st.header("Analytics Team")
texted_value = st.text_input("Please input")
if texted_value == "":
    st.markdown("Please input something above")
else:
    st.markdown(f"Working with {texted_value}")

dummy_data = {"X1":[1,2,3],
              "X2":[2,3,0],
              "Y" :[1,0,1]}
data = pd.DataFrame(dummy_data)
data