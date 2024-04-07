def get_todos(filepath="todos.txt"):   # default argument =todos.txt
    with open(filepath, 'r') as file_local:  # we need to open the file first
        todos_local = file_local.readlines()  # returns a list/array string data type such as todos = []
    return todos_local


def write_todos(todos_local, filepath="todos.txt"):  # argument placement matters especially default args
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)


print(__name__)

if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())