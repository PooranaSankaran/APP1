import functions
import PySimpleGUI as sg

lable = sg.Text('Type in a to-do') #lable to add fo 1st dialog box
input_box = sg.InputText(tooltip='Enter todo',key='todo') #before adding key it 0 is the key for 1st added word now todo
add_button = sg.Button('Add')  #button to add in app

window = sg.Window('My To-Do App', # title of the app
                   layout = [[lable], [input_box,add_button]],
                   font = {'Helvetice',20})

while True: # we after one iter it will stop we no need to stop that's why while  = True until it's break by user
    event , values = window.read()  #even is add and values is adding input eg; hi retun {todo:hi}
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todos = values['todo'] + '\n'
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WIN_CLOSED: # when we close the app this exists from the loop
            break
window.close()