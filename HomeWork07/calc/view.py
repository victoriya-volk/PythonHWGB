def first_user_input(): # первый ввод юзера для определения с чем имеем дело
    while True:
        user_enter = input('Введите целое число или выражение: ')
        try:
            int(user_enter)
        except:
            for sign in user_enter:
                if not sign.isdigit() and sign not in ['+', '-', '/', '*', ' ']:
                    print('Ошибка!')
                    break
            # continue
        return user_enter

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
