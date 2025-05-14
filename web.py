import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'].strip()
    if todo:
        todos.append(todo + "\n")
        functions.write_todos(todos)
        st.session_state['new_todo'] = ''


st.markdown("<h1 style='color:  blue;'>My Todo App</h1>", unsafe_allow_html=True)
st.subheader("This is my first todo app.")
st.write("This app will help you manage your tasks.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
st.button("Add", on_click=add_todo)
