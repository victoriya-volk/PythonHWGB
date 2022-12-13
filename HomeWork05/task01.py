# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string = 'Я люблю Джавуабв абви Питон'
print(string)
string = string.split()

string = list(filter(lambda e: 'абв' not in e, string))

string = ' '.join(string)
print(string)
