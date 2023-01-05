phone_book = []

def get_phone_book():
    global phone_book
    return phone_book

def set_phone_book(new_phone_book):
    global phone_book
    phone_book = new_phone_book

def add_contact(contact: list):
    global phone_book
    phone_book.append(contact)

def remove_contact(id):
    global phone_book
    name = phone_book[id - 1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (y/n)')
    if confirm.lower() == 'y':
        phone_book.pop(id - 1)
        return True
    return False

def search_contact(search_text: str):
    global phone_book
    founding = []
    for contact in phone_book:
        if search_text in contact[0]:
            founding.append(contact)
    return founding

def change_contact(id):
    global phone_book
    contact = phone_book[id - 1]
    i = 0
    while i < len(contact):
        new_data = input(f'Как вы хотите изменить {contact[i]}? ')
        if new_data:
            contact[i] = new_data
        i += 1
    return phone_book