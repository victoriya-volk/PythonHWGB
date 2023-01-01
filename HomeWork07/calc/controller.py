import view as v
import model as m

def input_numX():
    number = v.input_number()
    m.set_numX(number)

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

def start():
    input_numX()
    while True:
        input_action()
        if m.get_action() == '=':
            v.log_off()
            break
        input_numY()
        solution()
