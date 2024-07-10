import Models.note
import Datastorage.loadFile as lf
import Datastorage.writeFile as wf
def add_note():
    title = input("Введите заголовок для заметки:\n")
    body = input("Введите описание для заметки:\n")
    note = Models.note.note(title=title, body=body)
    array_notes = lf.read_file()
    for i in array_notes:
        if Models.note.note.get_id(note) == Models.note.note.get_id(i):
            Models.note.note.set_id(note)
    array_notes.append(note)
    wf.write_file(array_notes, 'a')
    print("Заметка добавлена в журнал!")

def show(txt):
    array_notes = lf.read_file()

    if array_notes:
        if txt == "all":
            print("ЖУРНАЛ ЗАМЕТОК:")
            for i in array_notes:
                print(Models.note.note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Models.note.note.get_id(i))
            id = input("\n Введите ID заметки: ")
            flag = True
            for i in array_notes:
                if id == Models.note.note.get_id(i):
                    print(Models.note.note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого ID")

        elif txt == "date":
            date = input("Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for i in array_notes:
                date_note = str(Models.note.note.get_date(i))
                if date == date_note[:10]:
                    print(Models.note.note.map_note(i))
                    flag = False
            if flag:
                print("Некорректный формат даты")
        else:
            print("Журнал заметок не заполнен")


def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = lf.read_file()
    flag = False

    for i in array_notes:
        if id == Models.note.note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wf.write_file(array_notes, 'a')
        print("Заметка с ID: ", id, " успешно удалена!")
    else:
        print("Указанный ID не найден")


def change_note():
    id = input("Введите ID изменяемой заметки: ")
    array_notes = lf.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Models.note.note.get_id(i):
            i.title = input("Попробуйте изменить заголовок:\n")
            i.body = input("Попробуйте изменить описание:\n")
            Models.note.note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        wf.write_file(array_notes_new, 'a')
        print("Заметка с ID: ", id, " успешно изменена!")
    else:
        print("Нет такого ID")
