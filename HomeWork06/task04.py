# Написать программу, которая будет ввыводит в консоль заданный текст
# (Python - один из самых популярных языков программирования в мире),
# затем принимать из консоли шаблон подстроки и удалять в задданом тексте
# все слова в которых присутствует введенный шаблон
# Пример:
# Python - один из самых популярных языков программирования в мире
# Введите подстроку: ам
# Python - один из популярных языков в мире
text = 'Python - один из самых популярных языков программирования в мире'

def deleted_part_text( string):
    print(string)
    temp = input('Введите нежелательное сочетание букв: ')
    string = string.split(' ')
    # index = 0
    # while index < len(string):
    #     if temp in string[index]:
    #         del string[index]
    #     index += 1
    string = list(filter(lambda e: temp not in e, string))

    print(" ".join(string))

deleted_part_text(text)
