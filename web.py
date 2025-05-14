import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo + "\n")
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title("My Todo App")
st.subheader("This is my first todo app.")
st.write("This app will help you manage your tasks.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
st.button("Add todo", on_click=add_todo)

