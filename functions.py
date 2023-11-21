FILE_PATH = 'todo.txt'
def get_todos(file_path=FILE_PATH):
    with open(file_path, 'r') as file:  # variable name as last
        todos = file.readlines()
    return todos

def write_todos(todo_arg, file_path=FILE_PATH):
    with open(file_path, 'w') as file:  # variable name as last
        file.writelines(todo_arg)