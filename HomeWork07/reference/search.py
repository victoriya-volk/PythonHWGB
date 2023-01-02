def searching_in_reference(list_reference):
    user_search = input('Введите данные для поиска: ')
    list_of_finding = []
    for item in list_reference:
        i = 0
        while i < len(item):
            if user_search in item[i]:
                list_of_finding.append(item)
                break
            else:
                i += 1
    return list_of_finding