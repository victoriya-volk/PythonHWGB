def main_menu():
    print('\n1. Открыть файл телефонной книги')
    print('2. Показать телефонную книгу')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выход\n')
    return choice_item_menu()

def choice_item_menu():
    while True:
        try:
            choice = int(input('Введите номер команды из меню: '))
            if choice in range(0, 8):
                print()
                return choice
            else:
                print('Такого пункта нет, повторите попытку')
        except:
            print('Ошибка ввода! Некорректные данные!')

def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('Телефонная книга пуста или не загружена')

def logg_off():
    print('До свидания, до новых встреч!')

def load_success():
    print('Телефонная книга загружена!')

def save_success():
    print('Телефонна книга сохранена!')

def remove_success():
    print('Контакт удален!')

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    return [name, phone, comment]

def input_remove_contact():
    id = int(input('Введите ID контакта, который желаете удалить: '))
    return id

def input_search_text():
    search_text = input('Введите текст для поиска: ')
    return search_text

def print_search_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('\nНичего не найдено.')

def input_change_contact():
    id = int(input('Введите ID контакта, который желаете изменить: '))
    return id
