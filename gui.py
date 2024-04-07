import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do. ")  # just a text prompt

input_box = sg.InputText(tooltip="Enter todo", key="todo_input_box")  # user enters a todo here
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos_listbox',
                      enable_events=True, size=(45, 10))  # this shows the todos list from the todo.txt file

edit_button = sg.Button("Edit")

layout = [[label],
          [input_box, add_button],
          [list_box, edit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1, event)  # what did the user click? "Add button?, Edit button?" this shows what they clicked
    print(2, values)    # This shows the values being transformed or added to the todolist
    # remember the values are a dictionary. so the first part 'name' is the key. next part is the data. 'key': datatype
    print(3, values['todos_listbox'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo_input_box'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_listbox'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos_listbox'][0]  # get the todo to change
            new_todo = values['todo_input_box']  # get the replacement todo
            # print(values['todos_listbox'][0])
            # print(values['todo_input_box'])

            todos = functions.get_todos()  # get the todolist
            index = todos.index(todo_to_edit)  # finds the todo in the list and returns the index
            todos[index] = new_todo  # replace the old todo with the new
            functions.write_todos(todos)  # write to the todo.txt file

            window['todos_listbox'].update(values=todos)  # this updates the listbox to reflect the changes

        case 'todos_listbox':  # this places the listbox todo value selected by the user in the input box
            window['todo_input_box'].update(value=values['todos_listbox'][0])

        case sg.WIN_CLOSED:
            break

window.close()