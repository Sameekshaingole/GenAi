import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello , Streamlit !")
st.write(":streamlit: This is your first streamlit app")
st.text("Let's get Started")

# condition logic 
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(f"Hello, {name}!")

# Disply Data and chart
df = pd.DataFrame(np.random.randn(10,2), columns =['A' , 'B'])
st.line_chart(df)
st.bar_chart(df)

#Media layout and advanced widget
st.sidebar.title("Navigation")
st.image("im.jpg", caption=" Sample image")
st.video("https://www.youtube.com/watch?v=K0S9xJwRohI")

upload_file = st.file_uploader("upload a file", type='csv')
if upload_file:
    df= pd.read_csv(upload_file)
    st.dataframe(df)

st.header("this is Header")
st.subheader("this is sub Header")
st.markdown("**Bold**, *Italic*, 'Code', [Link](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")
st.text_input("What's your name?")
st.text_area("Write Something....")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range",0,100 )
st.selectbox("Select a fruit",["Apple","Banana","Mango"])
st.multiselect("choose toppings",["Cheese", "Tomato", "Olives"])
st.radio("Pick one",["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("show Details"):
    st.info("Here are more Details....")

option = st.radio("Choose view", ["Show Chart","Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username = st.text_input("username")
    password = st.text_input("Password", type= "password")
    submitted = st.form_submit_button("Login")

if submitted:
    st.success(f"Welcome, {username}!")   