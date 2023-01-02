def adding_new_contact(list_reference: list):
    new_contact = input('Введите данные через пробел (Имя Фамилия Телефон): ').split()
    list_reference.append(new_contact)
    return list_reference
