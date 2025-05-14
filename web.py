import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my first todo app.")
st.write("This app will help you manage your tasks.")



for todo in todos:
    st.checkbox(todo)

st.text_input(label= "", placeholder= "Add new todo...")
st.button("Add todo)