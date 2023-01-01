def input_number():
    while True:
        try:
            number = int(input('Введите целое число: '))
        except:
            print('Ошибка')
        return number

def input_action():
    while True:
        action = input('Введите операцию: ')
        if action in ['+', '-', '*', '/', '=']:
            return action
        else:
            print('Введите корректную операцию')

def print_to_console(value_text):
    print(value_text)

def log_off():
    print('До свидания!')

def print_divis_by_zero():
    print('На ноль делить нельзя!')
