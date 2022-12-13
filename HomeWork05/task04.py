# Pеализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

start_path = r'start.txt'
result_path = r'result.txt'

with open(start_path, 'w') as start_rle:
    start_rle.write('gggddddkkkmmb')
    start_rle.close()

with open(start_path, 'r') as start_rle:
    string = start_rle.read()
    start_rle.close()
# print(string)

def generate_rle_dict(string: str) -> dict:
    new_dict = dict()
    i = 0
    while i < len(string):
        if string[i] not in new_dict.keys():
            count = 1
            new_dict[string[i]] = count
            i += 1
        else:
            new_dict[string[i]] += 1
            i += 1
    return new_dict

def write_rle_string(path: str, dictionary: dict):
    with open(path, 'w') as result_rle:
        for dict_key in dictionary:
            result_rle.write(f'{dict_key}{dictionary[dict_key]}')
write_rle_string(result_path, generate_rle_dict(string))

def restoration_text(path_rest: str, path_save):
    with open(path_rest, 'r') as text_for_restore:
        string = text_for_restore.read()
        text_for_restore.close()
        string = list((string[i], string[i+1]) for i in range(0, len(string), 2))
        new_string = ''.join(list(sign[0] * int(sign[1]) for sign in string))
    with open(path_save, 'a') as saving_text:
        saving_text.writelines(f' {new_string}')
        saving_text.close()

restoration_text(result_path, start_path)

