class Individual:
    def __init__(self, email, name, surname):
        self.inbox = []
        self.email = email
        self.name = name
        self.surname = surname

    def send_message(self, text, sender):
        self.inbox.append((text, sender))

    def __str__(self):
        return self.email + ' , ' + self.name + ' , ' + self.surname


class Student(Individual):
    def __init__(self, id_number, email, name, surname, owned_grades=None):
        if owned_grades is None:
            self.owned_grades = dict()
        self.id_number = id_number
        super().__init__(email, name, surname)

    def __str__(self):
        return super().__str__() + ' , ' + str(self.owned_grades) + ' , ' + str(self.id_number)

    def add_new_grade(self, subject, grade: float):
        if (subject not in self.owned_grades.keys()) or (grade < 2.0) or (grade > 5.0):
            raise ValueError
        self.owned_grades[subject] = grade


class UniversityEmployee(Individual):
    def __init__(self, email, name, surname, room_number):
        super().__init__(email, name, surname)
        self.room_number = room_number

    def __str__(self):
        return super().__str__() + ' , ' + str(self.room_number)


class ResearchEmployee(UniversityEmployee):
    def __init__(self, email, name, surname, room_number, publications_list):
        super().__init__(email, name, surname, room_number)
        self.publications_list = publications_list

    def __str__(self):
        return super().__str__() + ' , ' + str(self.publications_list)

    def add_new_publication(self, title):
        self.publications_list.append(title)


class TeachingEmployee(UniversityEmployee):
    def __init__(self, email, name, surname, room_number, consultation_time, subjects_list):
        super().__init__(email, name, surname, room_number)
        self.consultation_time = consultation_time
        self.subjects_list = subjects_list

    def __str__(self):
        return super().__str__() + ' , ' + self.consultation_time + ' , ' + str(self.subjects_list)


class TeachingAndResearchEmployee(TeachingEmployee, ResearchEmployee):
    def __init__(self, email, name, surname, room_number, consultation_time, publications_list, subjects_list):
        TeachingEmployee.__init__(self, email, name, surname, room_number, subjects_list, consultation_time)
        ResearchEmployee.__init__(self, email, name, surname, room_number, publications_list)

    def __str__(self):
        return ResearchEmployee.__str__(self) + ' , ' + str(self.consultation_time) + ' , ' + str(self.subjects_list)
