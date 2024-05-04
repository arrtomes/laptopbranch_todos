import functions
import PySimpleGUI as sg
from time import strftime, localtime

sg.theme("DarkTeal 7")
clock = sg.Text('', key='TIME')
label = sg.Text("Type in a to-do. ")  # just a text prompt

input_box = sg.InputText(tooltip="Enter todo", key="todo_input_box")  # user enters a todo here
add_button = sg.Button("Add", size=15)

list_box = sg.Listbox(values=functions.get_todos(), key='todos_listbox',
                      enable_events=True, size=(45, 10))  # this shows the todos list from the todo.txt file

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[label, clock],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 14))
while True:
    event, values = window.read(timeout=1000)  # timeout means refresh. the 1000 means every 1 second ie 2000 mean 2 sec
    current_time = strftime("%a, %d %b %Y %H:%M:%S", localtime())
    window['TIME'].update(current_time)
    print(1, event)  # what did the user click? "Add button?, Edit button?" this shows what they clicked
    print(2, values)    # This shows the values being transformed or added to the todolist
    # remember the values are a dictionary. so the first part 'name' is the key. next part is the data. 'key': datatype
    print(3, values['todos_listbox'])
    # print(4, values['todos_listbox'][0])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo_input_box'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_listbox'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos_listbox'][0]  # get the todo to change
                new_todo = values['todo_input_box']  # get the replacement todo
                # print(values['todos_listbox'][0])
                # print(values['todo_input_box'])

                todos = functions.get_todos()  # get the todolist
                index = todos.index(todo_to_edit)  # finds the todo in the list and returns the index
                todos[index] = new_todo  # replace the old todo with the new
                functions.write_todos(todos)  # write to the todo.txt file

                window['todos_listbox'].update(values=todos)  # this updates the listbox to reflect the changes
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 14))

        case "Complete":
            try:
                todo_to_complete = values['todos_listbox'][0]  # extracting str from list
                todos = functions.get_todos()  # Get the todo list from txt.
                todos.remove(todo_to_complete)  # remove method requires data not list type so use extracted str
                functions.write_todos(todos)   # rewrite after removing todo because it wont keep the update.
                window['todos_listbox'].update(values=todos)  # show removal of todo in real time.
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 14))

        case 'todos_listbox':  # this places the listbox todo value selected by the user in the input box
            window['todo_input_box'].update(value=values['todos_listbox'][0])

        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
print("Bye")
window.close()
