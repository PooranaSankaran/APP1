import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

#step 1
st.title("My Todo App")
st.subheader('This is my todo app')
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key = todo) # add list to the pervious checkbox
                   #key = todo1 beacuse if we select the todo1 which alrdy present to be deleted
    if checkbox:  #checkbox works if the user selected the checkbox we can see True in console if user selected any checkbox
        todos.pop(index)#if user select the checkbox it will be deleted in UI in web
        functions.write_todos(todos)
        del st.session_state[todos] # dlt from sesion state showing in ui
        st.experimental_rerun() # or rerun #after dlt rerun it
st.text_input(label=" ", placeholder='Add new todo..')
