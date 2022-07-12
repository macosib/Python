documents = [
    {
        "type": "passport",
        "number": "2207 876234",
        "name": "Василий Гупкин"
    },
    {
        "type": "invoice",
        "number": "11-2",
        "name": "Геннадий Покемонов"
    },
    {
        "type": "insurance",
        "number": "10006",
        "name": "Аристарх Павлов"
    }
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def _check_doc_in_documents(number):
    for doc in documents:
        if doc['number'] == number:
            return True
    return False

def _shelf_doc_in_directories(number):
    print(documents)
    for shelve in directories.keys():
        if number == shelve:
            return True
    return False


def find_people(doc_number=None):
    if doc_number is None:
        doc_number = input('Введите номер документа: ')
    if _check_doc_in_documents(doc_number):
        for doc in documents:
            if doc_number == doc['number']:
                print(f"Владелец документа: {doc['name']}")
                return doc['name']
    print(f'Документа нет в списке.')


def find_shelf():
    doc_number = input('Введите номер документа: ')
    if _check_doc_in_documents(doc_number):
        for shelve, doc_list in directories.items():
            if doc_number in doc_list:
                print(f'Документ находится на полке номер: {shelve}.')
                return shelve
    print(f'Запрашиваемый документ отсутствует.')

def doc_info(document):
    return f"{document['type']} {document['number']} {document['name']}"


def show_all_documents():
    docs = [doc_info(doc) for doc in documents]
    print(*docs, sep='\n')
    return docs

def add_people_doc():
    number = input('Введите номер документа: ')
    type_doc = input('Введите тип документа: ')
    name = input('Введите имя владельца документа: ')
    shelf = input('Введите номер полки, куда необходимо поместить документ: ')
    documents.append({"type": type_doc, "number": number, "name": name})
    directories[add_shelf(shelf)].append(number)
    print(f'Документ добавлен на полку {shelf}')
    return shelf


def delete_doc():
    doc_number = input('Введите номер документа: ')
    if _check_doc_in_documents(doc_number):
        for doc in documents:
            if doc['number'] == doc_number:
                documents.remove(doc)
                print('Указанный документ из списка.')
                break
        for shelf, docs in directories.items():
            if doc_number in docs:
                directories[shelf].remove(doc_number)
                print('Указанный документ удален с полки.')
                return doc_number
    print('Запрашиваемый документ отсутствует.')

def move_doc():
    doc_number = input('Введите номер документа: ')
    shelf = input('Введите номер полки, куда необходимо поместить документ: ')
    if _check_doc_in_documents(doc_number):
        for doc_list in directories.values():
            if doc_number in doc_list:
                doc_list.remove(doc_number)
                break
        directories[add_shelf(shelf)].append(doc_number)
        print(shelf)
        print(f'Документ успешно перемещен на полку {shelf}.')
        return shelf
    print('Такой документ не существует.')


def add_shelf(shelf=None):
    if shelf is None:
        shelf = input('Введите номер новой полки: ')
    if not _shelf_doc_in_directories(shelf):
        directories[shelf] = []
        print(f'Полка {shelf} добавлена')
        return shelf
    return shelf


def input_data():
    print('В documents содержатся следующие данные:')
    for data in documents:
        print(data)
    print()
    print()
    print('В directories содержатся следующие данные:')
    for key, value in directories.items():
        print(key, value)


def info_function():
    print("""
        info - Описание всех команд.
        data - Список всех документов и полок.
        p – Узнать кому принадлежит документ.
        s – Узнать на какой полке лежит документ.
        l – Вывести список всех документов.
        a – Добавить новый документ в каталог и на полку.
        d – Удалить документ с каталога и полки.
        m – Переместить документ на другую полку.
        as – Добавить новую полку.
        """)


command_dict = {
    'p': find_people,
    's': find_shelf,
    'l': show_all_documents,
    'a': add_people_doc,
    'd': delete_doc,
    'm': move_doc,
    'as': add_shelf,
    'data': input_data,
    'info': info_function,
}


def main():
    print('''
    Главное меню:
    Вы можете ввести следующие команды: p, s, l, a, d, m, as, data, info. 
    Для завершения работы программы введите "q".
    ''')
    print()
    while True:
        command = input("Введите команду: ").lower()
        if command == "quit":
            break
        elif command not in command_dict:
            print('Такая команда не существует, повторите ввод.')
            continue
        else:
            command_dict[command]()


if __name__ == '__main__':
    main()
