import view
import phone_book as pb
import data_base as db

def main_menu(choice: int):
    match choice:
        case 1:
            db.load_data_base()
            view.load_success()
        case 2:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
        case 3:
            db.save_data_base()
            view.save_success()
        case 4:
            contact = view.input_new_contact()
            pb.add_contact(contact)
        case 5:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_change_contact()
            view.print_phone_book(pb.change_contact(id))
            db.save_data_base()
        case 6:
            phone_book = pb.get_phone_book()
            view.print_phone_book(phone_book)
            id = view.input_remove_contact()
            if pb.remove_contact(id):
                view.remove_success()
        case 7:
            search_text = view.input_search_text()
            founding = pb.search_contact(search_text)
            view.print_search_phone_book(founding)
        case 0:
            return True

def start():
    while True:
        choice = view.main_menu()
        if main_menu(choice):
            view.logg_off()
            break