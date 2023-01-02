def write_operation(value):
    with open('log.txt', 'a') as file:
        file.write(f'{value}\n')
        file.close()
