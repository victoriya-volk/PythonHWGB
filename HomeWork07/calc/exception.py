exception = ''
express_list = []
result = 0
def except_parce(exception: str): # преобразование строки в массив, разделение по ' '
    global express_list
    express_list = exception.split()
    for i in range(len(express_list)):
        if express_list[i].isdigit():
            express_list[i] = int(express_list[i])
    return express_list

def set_exception_str(value): # сохранение строки в глобальную переменную
    global exception
    exception = value

def get_exception_str(): # получение значения пременной хранящей строку
    global exception
    return exception
def get_express_list(): # получение списка из составляющих выражения
    global express_list
    return express_list

def get_exception_result(): # получение значения переменной хранящей результат
    global result
    return result

def do_calculation_exception(except_list: list): # вычисление выражения
    i = 0
    while ('*' in except_list or '/' in except_list) and i < len(except_list):
        if except_list[i] == '*':
            action = except_list[i - 1] * except_list[i + 1]
            except_list.pop(i)
            except_list.pop(i)
            except_list[i - 1] = action
        elif except_list[i] == '/':
            action = except_list[i - 1] / except_list[i + 1]
            except_list.pop(i)
            except_list.pop(i)
            except_list[i - 1] = action
        else:
            i += 1
    while ('+' in except_list or '-' in except_list) and i < len(except_list):
        if except_list[i] == '+':
            action = except_list[i-1] + except_list[i + 1]
            except_list.pop(i)
            except_list.pop(i)
            except_list[i - 1] = action
        elif except_list[i] == '-':
            action = except_list[i-1] - except_list[i + 1]
            except_list.pop(i)
            except_list.pop(i)
            except_list[i - 1] = action
        else:
            i += 1
    global result
    result = except_list[0]
    return result