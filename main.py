from functions import get_todos, write_todos
while True:
    userAction = input("Type add, show, edit, complete, or exit: ")
    userAction = userAction.strip()  # Return a copy of the string with leading and trailing whitespace removed.

    if userAction.startswith("add"):
        todo = userAction[4:]  # list slicing. cut out the first 4 characters ->'add '

        todos = get_todos()

        todo = todo + "\n"
        todos.append(todo)  # .append allows the user to add an unspecified amount of items to the array

        write_todos(todos)
        '''with open("todos.txt", 'w') as file:
            file.writelines(todos)'''

    elif userAction.startswith("show"):  # the | is the OR operator

        todos = get_todos()

        # The following code removes the double break lines
        # newTodos = [item.strip('\n') for item in todos]

        for i, item in enumerate(todos):   # enumerate adds a number list to (todos)
            item = item.strip('\n')  # remove the builtin break line
            row = f"{i + 1}-{item}"
            print(row)  # print and a break line
            # print(i, '-', item)  # print(todos) = show user the list of task so far

    elif userAction.startswith("edit"):
        try:
            number = int(userAction[5:])
            number = number - 1

            todos = get_todos()

            newTodo = input("Enter a replace todo. ")
            todos[number] = newTodo + '\n'

            write_todos(todos)  # write_todos can be written as write_todos(todos) since todo_file is default

        except ValueError:
            print("Your command is not valid.")
            continue  # continue will ignore the rest of the code and loop back to line 2

    elif userAction.startswith("complete"):
        try:
            number = int(userAction[9:])

            todos = get_todos()

            index = number - 1
            removedTodo = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"you removed {removedTodo}"
            print(message)

        except IndexError:  # IndexError is for when the user enters an Index that is out of range in the list.
            print("There is no item with that number")
            continue  # continue will ignore the rest of the code and loop back to line 2

    elif userAction.startswith("exit"):
        break

    # if _:  # convention it's a catch-all if the user inputs the incorrect command. _ is just a var that's all
    else:
        print("Invalid command. ")

print("Bye")
