from library import *
import sys


def validate_login(given_login):
    for k in users_dict.keys():
        if k == given_login:
            return True


def get_login():
    x = input('Podaj swój login:\n')
    return x


def show_initial_menu():
    while True:
        x = input('1. Zaloguj się\n2. Zamknij\n')
        if x == '1':
            break
        elif x == '2':
            sys.exit(0)
        else:
            print('Błędnie wybrana opcja, spróbuj jeszcze raz')


def show_reader_menu(current_reader):
    while True:
        x = input('1. Przeszukaj katalog\n2. Wypożycz książkę\n3. Zakończ\n')
        if x == '1':
            phrase = input('Podaj tytuł lub autora książki: ')
            current_reader.search_catalog(phrase)
            break
        elif x == '2':
            book_id = input('Podaj id książki, którą chcesz wypożyczyć: ')
            current_reader.lend_book(book_id)
            break
        elif x == '3':
            sys.exit(0)
        else:
            print('Błędnie wybrana opcja, spróbuj jeszcze raz')


def show_worker_menu(current_worker):
    while True:
        x = input('1. Dodaj książkę\n2. Usuń książkę\n3. Dodaj czytelnika\n4. Przyjmij zwrot\n5. Zakończ\n')
        if x == '1':
            new_book = input('Podaj tytuł, autora, rok wydania i identyfikator (oddzielone przecinkami): ').split()
            current_worker.add_book(new_book[0], new_book[1], int(new_book[2]), new_book[3])
            break
        elif x == '2':
            removing_book = input('Podaj identyfikator książki, którą chcesz usunąć: ')
            current_worker.remove_book(removing_book)
            break
        elif x == '3':
            new_reader = input('Podaj login nowego czytelnika: ')
            current_worker.add_reader(new_reader)
            break
        elif x == '4':
            returning_book = input('Podaj identyfikator książki: ')
            current_worker.return_book(returning_book)
            break
        elif x == '5':
            sys.exit(0)
        else:
            print('Błędnie wybrana opcja, spróbuj jeszcze raz')


def get_login_and_show_menu():
    while True:
        given_login = get_login()
        validate_login(given_login)
        current_user = None
        if validate_login(given_login):
            if users_dict[given_login]['who'] == 'Reader':
                current_user = Reader(given_login)
            elif users_dict.copy()[given_login]['who'] == 'Worker':
                current_user = Worker(given_login)
            for k, v in users_dict.copy().items():
                if k == given_login:
                    if v['who'] == 'Worker':
                        show_worker_menu(current_user)
                    elif v['who'] == 'Reader':
                        show_reader_menu(current_user)
            break
        else:
            print('Podano nieprawidłowe dane, spróbuj jeszcze raz')


def update_json_files():
    with open('library_data.json', 'w') as file:
        json.dump(library_dict, file, ensure_ascii=False, indent=6)

    with open('users_data.json', 'w') as fil:
        json.dump(users_dict, fil, ensure_ascii=False, indent=6)


if __name__ == '__main__':
    while True:
        show_initial_menu()
        get_login_and_show_menu()
        update_json_files()
