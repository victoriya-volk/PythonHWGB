import phone_book as pb

path = 'phone_book.csv'

def load_data_base():
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book = file.readlines()
        pb.set_phone_book(strs_to_list(phone_book))

def strs_to_list(phone_book: list):
    new_phone_book = []
    for contact in phone_book:
        new_phone_book.append(contact.strip().split(';'))
    return new_phone_book

def save_data_base():
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(list_to_strs())

def list_to_strs():
    phone_book = pb.get_phone_book()
    new_phone_book = []
    for contact in phone_book:
        new_phone_book.append(';'.join(contact) + '\n')
    new_phone_book[-1] = new_phone_book[-1][:-1]
    return ''.join(new_phone_book)