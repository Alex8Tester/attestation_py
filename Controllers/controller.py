import Controllers.commands as com
import UI.menu as ui
def start():
    while True:
        ui.menu()
        user_input = input()
        if user_input == '1':
            com.show("all")
        elif user_input == '2':
            com.show("ID")
        elif user_input == '3':
            com.show("date")
        elif user_input == '4':
            com.show("all")
            com.change_note()
        elif user_input == '5':
            com.add_note()
        elif user_input == '6':
            com.show("all")
            com.del_notes()
        else:
            print("Программа Журнал заметок завершена")
            break