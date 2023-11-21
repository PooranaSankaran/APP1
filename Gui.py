import functions
import PySimpleGUI as sg
import time

sg.theme('DarkPurple4')

clock = sg.Text('',key='clock')
lable = sg.Text('Type in a to-do') #lable to add fo 1st dialog box
input_box = sg.InputText(tooltip='Enter todo',key='todo') #before adding key it 0 is the key for 1st added word now todo
add_button = sg.Button('Add')  #button to add in app

#step 2 need to add edit button and list of item to show
list_box = sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events=True, size=[45, 10])
# we need to add button to show in app
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('exit')

window = sg.Window('My To-Do App', # title of the app
                   layout = [[clock],[lable], [input_box,add_button],[list_box,edit_button,complete_button],
                             [exit_button]],
                   font = {'Helvetice',20})

while True: # we after one iter it will stop we no need to stop that's why while  = True until it's break by user
    event , values = window.read() #even is add and values is adding input eg; hi retun {todo:hi}
    window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todos = values['todo'] + '\n'
            todos.append(new_todos)
            functions.write_todos(todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values = todos) # window is mother contains all in it. to show user immediate responds we updating windows with new todos
            except IndexError:
                sg.popup('Please select an item first',font = {'Helvetice',20})
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = '')
            except IndexError:
                sg.popup('Please select an item first', font={'Helvetice', 20})

        case 'exit':
            break

        case sg.WIN_CLOSED: # when we close the app this exists from the loop
            break
window.close()