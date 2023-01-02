import view as v
import working_file as work
import search as search
import adding as add

def button_click():
    file_path = v.input_file_path()
    work.set_file_path(file_path)
    file_info = work.read_in_file(work.get_file_path())
    work.set_info_in_file(file_info)
    step_of_work = work.working_with_info_in_file(work.get_info_in_file())
    work.set_info_in_file(step_of_work)
    # v.print_to_console(work.get_info_in_file())
    all_func_select()



def all_func_select():
    interact = v.selecting_func()
    if interact == 's':
        v.print_to_console('Вы выбрали функцию поиска')
        list_search = search.searching_in_reference(work.get_info_in_file())
        v.print_reference_to_console(list_search)
        all_func_select()
    elif interact == 'a':
        v.print_to_console('Вы добавляете новый контакт')
        new_reference = add.adding_new_contact(work.get_info_in_file())
        work.set_info_in_file(new_reference)
        all_func_select()
    elif interact == 'p':
        v.print_to_console('Справочник: ')
        v.print_reference_to_console(work.get_info_in_file())
        all_func_select()
    elif interact == 'q':
        v.print_to_console('До свидания!')
    else:
        v.print_to_console('Я не знаю такой команды! Выхожу из справочника.')

