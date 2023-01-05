import view
import phone_book as pb
import data_base as db
import logger as log

def main_menu(choice: int):
    match choice:
        case 1:
            db.load_data_base()
            view.load_success()
            log.write_logger_line('Телефонная книга загружена.')
        case 2:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            log.write_logger_line('Телефонная книга выведена на печать.')
        case 3:
            db.save_data_base()
            view.save_success()
            log.write_logger_line('Телефонная книга сохранена.')
        case 4:
            contact = view.input_new_contact()
            pb.add_contact(contact)
            log.write_logger_line(f'Добавлен новый контакт {contact}')
        case 5:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_change_contact()
            view.print_phone_book(pb.change_contact(id))
            log.write_logger_line(f'Добавлен новый контакт {phone_book[id - 1]}')
            db.save_data_base()
        case 6:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_remove_contact()
            if pb.remove_contact(id):
                view.remove_success()
                log.write_logger_line(f'Удален контакт {phone_book[id - 1]}')
        case 7:
            search_text = view.input_search_text()
            founding = pb.search_contact(search_text)
            view.print_search_phone_book(founding)
            log.write_logger_line(f'Выполнен поиск {search_text}\n Найдено {len(founding)} контактов')
        case 0:
            log.write_logger_line(f'Работа с телефонной книгой завершена!')
            return True

def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.logg_off()
            break