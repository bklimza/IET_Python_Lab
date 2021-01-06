class Individual:
    def __init__(self, email, name, surname):
        self.inbox = []
        self.email = email
        self.name = name
        self.surname = surname

    def send_message(self, text, sender):
        self.inbox.append((text, sender))


class Student(Individual):
    def __init__(self, index_number, email, name, surname, grades=None):
        self.index_number = index_number
        Individual.__init__(self, email, name, surname)
        if grades is None:
            self.grades = dict()
        else:
            self.grades = grades

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.email + ' ' + str(self.index_number) + ' ' + str(self.grades)

    def add_new_grade(self, subject, grade: float):
        if (subject not in self.grades.keys()) or (grade < 2.0) or (grade > 5.0):
            raise ValueError
        self.grades[subject] = grade


class UniversityEmployee(Individual):
    def __init__(self, email, name, surname, room_number):
        Individual.__init__(self, email, name, surname)
        self.room_number = room_number


class ResearchEmployee(UniversityEmployee):
    def __init__(self, email, name, surname, room_number, publications_list):
        UniversityEmployee.__init__(self, email, name, surname, room_number)
        self.publications_list = publications_list

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.email + ' ' + self.room_number + ' ' \
               + str(self.publications_list)

    def add_new_publication(self, title):
        self.publications_list.append(title)


class TeachingEmployee(UniversityEmployee):
    def __init__(self, email, name, surname, room_number, consultation_time, subjects_list):
        UniversityEmployee.__init__(self, email, name, surname, room_number)
        self.consultation_time = consultation_time
        self.subjects_list = subjects_list

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.email + ' ' + self.room_number + ' ' \
            + self.consultation_time + ' ' + str(self.subjects_list)


class TeachingAndResearchEmployee(TeachingEmployee, ResearchEmployee):
    def __init__(self, email, name, surname, room_number, consultation_time, publications_list, subjects_list):
        TeachingEmployee.__init__(self, email, name, surname, room_number, subjects_list, consultation_time)
        ResearchEmployee.__init__(self, email, name, surname, room_number, publications_list)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.email + ' ' + self.room_number + ' ' \
            + self.consultation_time + ' ' + str(self.subjects_list) + ' ' + str(self.publications_list)
