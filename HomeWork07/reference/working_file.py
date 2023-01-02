file_path = ''
info_in_file = []

def set_file_path(value):
    global file_path
    file_path = value

def set_info_in_file(value):
    global info_in_file
    info_in_file = value

def get_file_path():
    global file_path
    return file_path

def get_info_in_file():
    global info_in_file
    return info_in_file

def read_in_file(value):
    global info_in_file
    with open(value, 'r') as user_file:
        info_in_file = user_file.readlines()
    user_file.close()
    return info_in_file

def working_with_info_in_file(info: list[str]):
    new_step = []
    i = 0
    while i < len(info):
        new_step.append(info[i].split())
        i += 1
    return new_step
