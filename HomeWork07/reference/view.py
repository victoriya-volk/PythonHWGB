
def input_file_path():
    file_path = input('Введите путь к файлу: ')
    for format in ['.txt', 'csv']:
        if format in file_path:
            return file_path
    else:
        print('Это не путь к файлу. Попробуйте еще раз.')
        return input_file_path()

def print_to_console(value):
    print(value)

def selecting_func():
    user_select = input('Чтобы выбрать функцию введите с клавиатуры: <s> - поиск, '
                        '<a> - добавить контакт, <p> - показать весь справочник, <q> - выход.'
                        'Что выбираете? ')
    return user_select

def print_reference_to_console(list_reference: [list]):
    name = 0
    familyname = 1
    phone = 2
    for item in list_reference:
        print(f'{item[name]} {item[familyname]} {item[phone]}')

