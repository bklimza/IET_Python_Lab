import json


class Book:
    def __init__(self, title, author, year, book_id, is_borrowed=False):
        self.title = title
        self.author = author
        self.year = year
        self.book_id = book_id
        self.is_borrowed = is_borrowed

    def __str__(self):
        return self.title + ' ' + self.author + ' ' + self.year + ' ' + self.book_id

    def convert_to_dict(self):
        return {self.book_id: {'title': self.title, 'author': self.author, 'year': self.year}}


class Worker:
    def __init__(self, login):
        self.login = login

    def __str__(self):
        return self.login + ' - Worker'

    def add_book(self, title, author, year, book_id):
        global library_dict
        library_dict.update({book_id: {'title': title, 'author': author, 'year': year, 'is_borrowed': False}})
        print('Książka została dodana\n')

    def remove_book(self, book_id):
        global library_dict
        del library_dict[book_id]
        print('Książka została usunięta\n')

    def add_reader(self, login, who='Reader'):
        global users_dict
        users_dict.update({login: {'who': who}})
        print('Czytelnik został dodany\n')

    def return_book(self, book_id):
        global library_dict
        if book_id in library_dict.keys():
            for k in library_dict[book_id]:
                if k == 'is_borrowed':
                    if library_dict[book_id][k]:
                        library_dict[book_id][k] = False
                        print('Książka została zwrócona\n')
                    else:
                        print('Książka nie została wypożyczona\n')
        else:
            print('Nie ma takiej książki\n')



class Reader:
    def __init__(self, login):
        self.login = login

    def __str__(self):
        return self.login + ' - Reader'

    def search_catalog(self, phrase):
        global library_dict
        for k, v in library_dict.items():
            if (v['title'] == phrase) or (v['author'] == phrase):
                print('Znalezione książki:\n')
                print(k, v, '\n')

    def lend_book(self, book_id):
        global library_dict
        if book_id in library_dict.keys():
            for k in library_dict[book_id]:
                if k == 'is_borrowed':
                    if not library_dict[book_id][k]:
                        library_dict[book_id][k] = True
                        print('Wypożyczyłeś książkę\n')
                    else:
                        print('Książka została już wypożyczona\n')
        else:
            print('Nie ma takiej książki\n')

with open('library_data.json', 'r+') as f:
    library_dict = json.load(f)

with open('users_data.json', 'r+') as fi:
    users_dict = json.load(fi)
