class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    # оценка лекции
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course] += [grade]
            else:
                lecturer.lectures_grades[course] = [grade]
        else:
            return 'Ошибка'

    # средняя оценка
    def mean_hw_grade(self):
        sum = count = 0
        for k,v in self.grades.items():
            for grade in v:
                sum += grade
                count += 1
        return sum / count

    # <
    def __lt__(self, other):
        return self.mean_hw_grade() < other.mean_hw_grade()

    # <=
    def __le__(self, other):
        return self.mean_hw_grade() <= other.mean_hw_grade()

    # >
    def __gt__(self, other):
        return self.mean_hw_grade() > other.mean_hw_grade()

    # >=
    def __ge__(self, other):
        return self.mean_hw_grade() >= other.mean_hw_grade()

    # ==
    def __eq__(self, other):
        return self.mean_hw_grade() == other.mean_hw_grade()

    # !=
    def __ne__(self, other):
        return self.mean_hw_grade() != other.mean_hw_grade()

    def __str__(self):
        info = 'Имя: ' + self.name
        info += '\nФамиилия: ' + self.surname
        info += '\nСредняя оценка за домашние задания: ' + str(self.mean_hw_grade())
        info += '\nКурсы в процессе изученя: ' + ", ".join(self.courses_in_progress)
        info += '\nЗавершенные курсы: ' + ", ".join(self.finished_courses)
        return info

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname) # вызов родительского конструктора
        self.lectures_grades = { } # словарь для оценок студентами

    # средняя оценка
    def mean_lect_grade(self):
        sum = count = 0
        for k, v in self.lectures_grades.items():
            for grade in v:
                sum += grade
                count += 1
        return sum / count

    def __str__(self):
        info = 'Имя: ' + self.name
        info += '\nФамиилия: ' + self.surname
        info += '\nСредняя оценка за лекции: ' + str(self.mean_lect_grade())
        return info

    # <
    def __lt__(self, other):
        return self.mean_lect_grade() < other.mean_lect_grade()
    # <=
    def __le__(self, other):
        return self.mean_lect_grade() <= other.mean_lect_grade()
    # >
    def __gt__(self, other):
        return self.mean_lect_grade() > other.mean_lect_grade()
    # >=
    def __ge__(self, other):
        return self.mean_lect_grade() >= other.mean_lect_grade()
    # ==
    def __eq__(self, other):
        return self.mean_lect_grade() == other.mean_lect_grade()
    # !=
    def __ne__(self, other):
        return self.mean_lect_grade() != other.mean_lect_grade()

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname) # вызов родительского конструктора

    def __str__(self):
        info = 'Имя: ' + self.name
        info += '\nФамиилия: ' + self.surname
        return info

# средняя оценка за дз для всех студентов по заданному курсу
def mean_course_hw_grade(students, course):
    sum = count = 0
    for s in students:
        if course in s.courses_in_progress:
            for k,v in s.grades.items():
                if k == course:
                    for grade in v:
                        sum += grade
                        count += 1
    if count != 0:
        return sum / count
    else:
        return 0

# средняя оценка за лекции по курсу
def mean_course_lecture_grade(lecturers, course):
    sum = count = 0
    for l in lecturers:
        if course in l.courses_attached:
            for k,v in l.lectures_grades.items():
                if k == course:
                    for grade in v:
                        sum += grade
                        count += 1
    if count != 0:
        return sum / count
    else:
        return 0

student1 = Student('Иван', 'Иванов', 'м')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Artificial Intelligence']

student2 = Student('Мария', 'Петрова', 'ж')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['OOP']

lecturer1 = Lecturer('Петр', 'Петров')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['OOP']

lecturer2 = Lecturer('Алексей', 'Алексеев')
lecturer2.courses_attached += ['Artificial Intelligence']

rewiewer1 = Reviewer('Анна', 'Анина')
rewiewer1.courses_attached += ['Python']
rewiewer1.courses_attached += ['OOP']

rewiewer2 = Reviewer('Борис', 'Борисов')
rewiewer2.courses_attached += ['Artificial Intelligence']

lecturer1.rate_hw(student1, 'Python', 10)
lecturer2.rate_hw(student1, 'Artificial Intelligence', 5)
rewiewer1.rate_hw(student1, 'Python', 9)
rewiewer1.rate_hw(student2, 'OOP', 8)
rewiewer2.rate_hw(student1, 'Artificial Intelligence', 7)

student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer2, 'Artificial Intelligence', 8)
student2.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer1, 'OOP', 10)

print(student1, '\n')
print(student2, '\n')
print(lecturer1, '\n')
print(lecturer2, '\n')
print(rewiewer1, '\n')
print(rewiewer2, '\n')

# проверки < >
print(student1 > student2)
print(student1 < student2)
print(lecturer1 < lecturer2)
print(lecturer2 < lecturer1)

# проверка средних оценок
mean_stud_python = mean_course_hw_grade([student1, student2], 'Python')
mean_lect_python = mean_course_lecture_grade([lecturer1, lecturer2], 'Python')
print('\nСредняя оценка студентов за ДЗ по курсу Python:', mean_stud_python)
print('Средняя оценка лекторов за лекции по курсу Python:', mean_lect_python)