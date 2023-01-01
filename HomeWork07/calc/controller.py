import view as v
import model as m
import exception as ex

def input_numX():
    user_enter = v.first_user_input()
    if user_enter.isdigit():
        m.set_numX(int(user_enter))
        return True
    else:
        ex.set_exception_str(user_enter)
        return False

def input_numY():
    while True:
        number = v.input_number()
        if m.get_action() == '/' and number == 0:
            v.print_divis_by_zero()
        else:
            m.set_numY(number)
            break

def input_action():
    act = v.input_action()
    m.set_action(act)

def solution():
    act = m.get_action()
    if act == '+':
        m.sum()
    elif act == '-':
        m.diff()
    elif act == '*':
        m.multy()
    elif act == '/':
        m.divis()
    result_string = f'{m.get_numX()} {m.get_action()} {m.get_numY()} = {m.get_result()}'
    v.print_to_console(result_string)
    m.set_numX(m.get_result())

def solution_expression(): # обращения к функциям вычисляющим значение выражения
    ex.except_parce(ex.get_exception_str())
    ex.do_calculation_exception(ex.get_express_list())
    result_str = f'{ex.get_exception_str()} = {ex.do_calculation_exception(ex.get_express_list())}'
    v.print_to_console(result_str)
    m.set_numX(ex.get_exception_result())

def start():
    if input_numX():
        while True:
            input_action()
            if m.get_action() == '=':
                v.log_off()
                break
            input_numY()
            solution()
    else:
        solution_expression()
        while True: # вычисление не останавливается, а продолжается как с обычным числом
            input_action()
            if m.get_action() == '=':
                v.log_off()
                break
            input_numY()
            solution()