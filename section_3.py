        # section 3
# user_prompt = "Enter a todo:"
#
# todos = []
#
# while True:
#     #todo = input(user_prompt)
#     print(todo.capitalize())
#     todos.append(todo)
#     print(todos)

#------------------------------------------------------------------------------------------

 # section 4

# todos = []
# while True:
#  user_action = input("Type add, show or exist: ").strip()
#
#  match user_action:
#   case 'add':
#    todo = input('Enter a todo:')
#    todos.append(todo)
#   case 'show':
#    for i in todos:
#     print(i)
#   case 'exist':
#    break
# print('BYE...')

#---------------------------------------------------------------------------------------------------------------------

# section 5 ( adding edit to todo)

# todos = []
# while True:
#  user_action = input("Type add, show, edit or exist: ").strip()
#
#  match user_action:
#   case 'add':
#    todo = input('Enter a todo:')
#    todos.append(todo)
#   case 'show':
#    for i in todos:
#     print(i)
#   case 'edit':
#       number = int(input('Number of todo to edit:'))
#       number = number-1
#       new_todo = input('Enter the new todo:')
#       todos[number] = new_todo
#   case 'exist':
#    break
# print('BYE...')

#---------------------------------------------------------------------------------------------------------------------

# section 6/7/8 (enumerate)
# we dlted the todos list.. because we need permenent storage of text
# while True:
#  user_action = input("Type add, show, edit, complete or exist: ").strip()
#
#  match user_action:
#   case 'add':
#    todo = input('Enter a todo:') + '\n' #\n because in txt file it have to show one by one in sep new line
#
#    file = open("todo.txt", 'r')# we are reading it because the previous entered item should be stroed
#
#    todos = file.readlines() # it will read nd store as list so, we dlted above todos list
#    file.close() # open file the close it
#    todos.append(todo) # adding each item into todos which stores in file as list
#
#    file = open("todo.txt",'w') # w = write , r = read # we using this beacuse the data are not stored to store data
#                                 # we create #todo txt file. to store every data it runs.
#
#
#
#    file.writelines(todos)  # after appending it will write everthing in txt file
#    file.close() # openned file then close it.
#   case 'show':
#
#    file  = open("todo.txt",'r')
#    todos = file.readlines()  # we creted it again beacuse each case are unique so, need to give acess to each case
#                                 # else it's through error as todos not found
#    file.close()
#
#    for index,i in enumerate(todos):  #to show index
#     i = i.strip('\n') # becasue in show has print funtion exceute one by one and above we are entering todo using \n so we striped
#     row = f"{index + 1}-{i}"          #+1 is to start index from 1
#     print(row)
#   case 'edit':
#       number = int(input('Number of todo to edit:'))
#       number = number-1
#       new_todo = input('Enter the new todo:')
#       todos[number] = new_todo
#   case "complete":
#       num = int(input('Number of todo to complete: '))
#       num = num - 1    # -1 is beacuse out index is starting from 0
#       todos.pop(num)
#   case 'exist':
#    break
# print('BYE...')

#---------------------------------------------------------------------------------------------------------------------

#section 9 (optimize)

# while True:
#  user_action = input("Type add, show, edit, complete or exist: ").strip()
#
#  match user_action:
#   case 'add':
#    todo = input('Enter a todo:') + '\n'
#
#    # file = open("todo.txt", 'r')
#    # todos = file.readlines()
#    # file.close()
#
#    # perviously we open nd read file the close it better way below shown
#
#    with open("todo.txt", 'r') as file:  # variable name as last
#        todos = file.readlines()            # reading and stroing in list into todos
#                                         # we don't need to close thats the benifit. of using with
#    todos.append(todo)
#
#    # file = open("todo.txt",'w')
#    # file.writelines(todos)
#    # file.close()
#    with open("todo.txt", 'w') as file:  # write
#         file.writelines(todos)
#   case 'show':
#
#    # file  = open("todo.txt",'r')
#    # todos = file.readlines()
#    # file.close()
#
#    with open("todo.txt",'r') as file:
#        todos = file.readlines()
#
#    for index,i in enumerate(todos):
#     i = i.strip('\n')
#     row = f"{index + 1}-{i}"
#     print(row)
#
#   case 'edit':
#       # below operation doesn't editing the text file beacuse not mentioned
#       # number = int(input('Number of todo to edit:'))
#       # number = number-1
#       # new_todo = input('Enter the new todo:')
#       # todos[number] = new_todo
#
#       # now we mention to edit in text file which stores all..
#     number = int(input('Number of todo to edit:'))
#     number = number-1
#     with open("todo.txt",'r') as file: #read the file to edit in text file
#           todos = file.readlines()
#     new_todo = input('Enter the new todo:')
#     todos[number] = new_todo + '\n' #while editing the \n line will disapire so, we adding it
#       # after edit write on file
#     with open("todo.txt", 'w') as file:
#           file.writelines(todos)
#
#   case "complete":
#       num = int(input('Number of todo to complete: '))
#       num = num - 1 # -1 is beacuse out index is starting from 0
#       with open("todo.txt", 'r') as file:  # read the file to edit in text file
#           todos = file.readlines()
#       todo_to_remove = todos[num].strip('\n')
#       todos.pop(num)
#       with open("todo.txt", 'w') as file:
#           file.writelines(todos)
#       message = f"Todo {todo_to_remove} was removed from the list"
#       print(message)
#   case 'exist':
#    break
# print('BYE...')

#--------------------------------------------------------------------------------------------------------------------------------

#section 10-.. (match case doesn't work in some case and we need to optimize it using if statement)
# we are writing if i give "add work" it should add "work"

# we have repeted code so use user diff funtion for optimize

# def get_todos(file_path):
#     with open(file_path, 'r') as file:  # variable name as last
#         todos = file.readlines()
#     return todos
#
# def write_todos(file_path,todo_arg):
#     with open(file_path, 'w') as file:  # variable name as last
#         file.writelines(todo_arg)
#
#
# while True:
#     user_action = input("Type add, show, edit, complete or exist: ").strip()
#
#
#     if user_action.startswith('add'):
#
#         todo = user_action[4:] #beacuase 1st 4 letters will we add and one space eg: "add work" it should add only "work
#
#         todos = get_todos('todo.txt')
#         todos.append(todo + '\n')
#         write_todos(file_path='todo.txt',todo_arg=todos)
#
#     elif user_action.startswith('show'):
#
#
#         todos = get_todos('todo.txt')
#
#         for index,i in enumerate(todos):
#                 i = i.strip('\n')
#                 row = f"{index + 1}-{i}"
#                 print(row)
#
#     elif user_action.startswith('edit'):
#         try:
#             number = int(user_action[5:])
#             number = number-1
#             todos = get_todos('todo.txt')
#             new_todo = input('Enter the new todo:')
#             todos[number] = new_todo + '\n' #while editing the \n line will disapire so, we adding it
#               # after edit write on file
#             write_todos(file_path='todo.txt',todo_arg=todos)
#         except ValueError:
#             print('Your comment is not valid')
#             continue  # it will print and go back to top skip this again wrong skip nd go back to top.
#             # because while loop is true untill it breaks it will run
#
#     elif user_action.startswith('complete'):
#         try:
#             num = int(user_action[9:])
#             num = num - 1 # -1 is beacuse out index is starting from 0
#             todos = get_todos('todo.txt')
#             todo_to_remove = todos[num].strip('\n')
#             todos.pop(num)
#             write_todos(file_path='todo.txt',todo_arg=todos)
#             message = f"Todo {todo_to_remove} was removed from the list"
#             print(message)
#         except IndexError:
#             print('There is no item with that number')
#             continue
#
#     elif user_action.startswith('exit'):
#         break
#     else:
#         print('comment in valid')
# print('BYE...')

#-----------------------

# Moving the created funtion to anthoer pyfile name as funtion.py
# we can assces that from there in our code

import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It's", now)

while True:
    user_action = input("Type add, show, edit, complete or exist: ").strip()


    if user_action.startswith('add'):

        todo = user_action[4:] #beacuase 1st 4 letters will we add and one space eg: "add work" it should add only "work

        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todo_arg=todos)

    elif user_action.startswith('show'):


        todos = functions.get_todos()

        for index,i in enumerate(todos):
                i = i.strip('\n')
                row = f"{index + 1}-{i}"
                print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number-1
            todos = functions.get_todos()
            new_todo = input('Enter the new todo:')
            todos[number] = new_todo + '\n' #while editing the \n line will disapire so, we adding it
              # after edit write on file
            functions.write_todos(todo_arg=todos)
        except ValueError:
            print('Your comment is not valid')
            continue  # it will print and go back to top skip this again wrong skip nd go back to top.
            # because while loop is true untill it breaks it will run

    elif user_action.startswith('complete'):
        try:
            num = int(user_action[9:])
            num = num - 1 # -1 is beacuse out index is starting from 0
            todos = functions.get_todos()
            todo_to_remove = todos[num].strip('\n')
            todos.pop(num)
            functions.write_todos(todo_arg=todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('comment in valid')
print('BYE...')






































