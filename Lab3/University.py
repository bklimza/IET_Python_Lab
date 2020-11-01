class Student:
    def __init__(self, first_name, last_name, email, index, grades=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.index = index
        self.inbox = []
        if grades is None:
            self.grades = dict()
        else:
            self.grades = grades

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.index) + ' ' + str(self.grades)

    def add_grade(self, subject, grade: float):
        self.grades[subject] = grade

    def send_email(self, text):
        self.inbox.append(text)


class TeachingWorker:
    def __init__(self, first_name, last_name, email, room, subjects, consultation):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.room = room
        self.subjects = subjects
        self.consultation = consultation
        self.inbox = []

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email + ' ' + self.room + ' '\
               + str(self.subjects) + ' ' + self.consultation

    def send_email(self, text):
        self.inbox.append(text)


class ResearchWorker:
    def __init__(self, first_name, last_name, email, room, publications):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.room = room
        self.publications = publications
        self.inbox = []

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email + ' ' + self.room + ' '\
               + str(self.publications)

    def send_email(self, text):
        self.inbox.append(text)

    def add_publications(self, publication):
        self.publications.append(publication)


class TeachingAndResearchWorker:
    def __init__(self, first_name, last_name, email, room, publications, subjects, consultation):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.room = room
        self.publications = publications
        self.subjects = subjects
        self.consultation = consultation
        self.inbox = []

    def send_email(self, text):
        self.inbox.append(text)

    def add_publications(self, publication):
        self.publications.append(publication)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email + ' ' + self.room + ' '\
               + str(self.subjects) + ' ' + self.consultation + ' ' + str(self.publications)
