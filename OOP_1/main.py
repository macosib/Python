class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_rating(self):
        if len(self.grades) > 0:
            all_grades = [grades_courses for grades in self.grades.values() for grades_courses in grades]
            result = round(sum(all_grades) / len(all_grades), 2)
        else:
            result = 'у студента еще нет оценок за домашние задания!'
        return result

    def __str__(self):
        courses_in_progress_for_print = ", ".join([course for course in self.courses_in_progress]) if len(
            self.courses_in_progress) > 0 else "Курсов в процессе изучения нет!"
        finished_courses_for_print = ", ".join([course for course in self.finished_courses]) if len(
            self.finished_courses) > 0 else "Завершенных курсов нет!"
        result = f'Имя: {self.name}\nФамилия: {self.surname}' \
                 f'\nСредняя оценка за лекции: {self.__average_rating()}' \
                 f'\nКурсы в процессе изучения: {courses_in_progress_for_print}' \
                 f'\nЗавершенные курсы: {finished_courses_for_print}'
        return result

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__average_rating() == other.__average_rating()

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.__average_rating() < other.__average_rating()

    def __le__(self, other):
        if isinstance(other, Student):
            return self.__average_rating() <= other.__average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_rating(self):
        if len(self.grades) > 0:
            all_grades = [grades_courses for grades in self.grades.values() for grades_courses in grades]
            result = round(sum(all_grades) / len(all_grades), 2)
        else:
            result = 'у лектора еще нет оценок!'
        return result

    def __str__(self):
        result = f'Имя: {self.name}' \
                 f'\nФамилия: {self.surname}' \
                 f'\nСредняя оценка за лекции: {self.__average_rating():}'
        return result

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.__average_rating() == other.__average_rating()

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.__average_rating() < other.__average_rating()

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.__average_rating() <= other.__average_rating()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):

        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}' \
                 f'\nФамилия: {self.surname}'
        return result


# Задание 4. Функции.
# Можно было бы объединить в одну функцию.

def average_course_student(students, course_name):
    # total = []
    # for student in students:
    #     if course_name in student.grades:
    #         for grade in student.grades[course_name]:
    #             total.append(grade)
    total = [grade for student in students if isinstance(student, Student) and course_name in student.grades
             for grade in student.grades[course_name]]
    if len(total) > 0:
        return f'Средняя оценка за д/з по курсу {course_name} составляет {round(sum(total) / len(total), 2)}'
    else:
        return f'По курсу {course_name} оценок нет'


def average_course_lecturer(lecturers, course_name):
    # total = []
    # for lecturer in lecturers:
    #     if course_name in lecturer.grades:
    #         for grade in lecturer.grades[course_name]:
    #             total.append(grade)
    total = [grade for lecturer in lecturers if isinstance(lecturer, Lecturer) and course_name in lecturer.grades
             for grade in lecturer.grades[course_name]]
    if len(total) > 0:
        return f'Средняя оценка за лекции по курсу {course_name} составляет {round(sum(total) / len(total), 2)}'
    else:
        return f'По курсу {course_name} оценок нет'


# Задание 4:
students_list = []
lecturer_list = []
reviewer_list = []
print('Добавляем студентов:')
# Студент 1
denis_sav = Student('Denis', 'Savoskin', 'man')
denis_sav.courses_in_progress += ['Python', 'JavaScript']
denis_sav.finished_courses += ['HTML', 'Git']
students_list.append(denis_sav)
print(f'Добавлен студент {denis_sav.name} {denis_sav.surname}.')
# Студент 2
alex_shir = Student('Alex', 'Shirokih', 'man')
alex_shir.courses_in_progress += ['Python', 'Ruby', 'JavaScript']
alex_shir.finished_courses += ['Введение в программирование', 'HTML ', 'Java']
students_list.append(alex_shir)
print(f'Добавлен студент {alex_shir.name} {alex_shir.surname}.')
# Студент 3
olga_akk = Student('Olga', 'Akimutina', 'woman')
olga_akk.courses_in_progress += ['Java', 'Git', 'Введение в программирование']
olga_akk.finished_courses += []
students_list.append(olga_akk)
print(f'Добавлен студент {olga_akk.name} {olga_akk.surname}.')
# Студент 4
alex_ovch = Student('Alex', 'Ovchinnikov', 'woman')
alex_ovch.courses_in_progress += ['Java', 'Git']
alex_ovch.finished_courses += []
students_list.append(alex_ovch)
print(f'Добавлен студент {alex_ovch.name} {alex_ovch.surname}.')
print(f'Список студентов: {", ".join([student.name + " " + student.surname for student in students_list])}')
print()
# Лектор 1
print('Добавляем лекторов:')
ivan_petr = Lecturer('Ivan', 'Petrov')
ivan_petr.courses_attached += ['Python', 'Ruby', 'JavaScript', 'HTML']
lecturer_list.append(ivan_petr)
print(f'Добавлен лектор {ivan_petr.name} {ivan_petr.surname}.')
# Лектор 2
semen_buk = Lecturer('Semen', 'Bukov')
semen_buk.courses_attached += ['Git', 'Java', 'JavaScript', 'HTML', 'Введение в программирование']
lecturer_list.append(semen_buk)
print(f'Добавлен лектор {semen_buk.name} {semen_buk.surname}.')
print(f'Список лекторов: {", ".join([lecturer.name + " " + lecturer.surname for lecturer in lecturer_list])}')
print()

# Ревьюер 1
print('Добавляем ревьюеров')
ivan_dmitr = Reviewer('Ivan', 'Dmitriev')
ivan_dmitr.courses_attached += ['Python', 'Ruby', 'JavaScript', 'HTML']
print(f'Добавлен ревьюер {ivan_dmitr.name} {ivan_dmitr.surname}.')
reviewer_list.append(ivan_dmitr)
# Ревьюер 2
petr_sah = Reviewer('Peter', 'Saharov')
petr_sah.courses_attached += ['Git', 'Java', 'HTML', 'Введение в программирование', 'JavaScript', ]
reviewer_list.append(petr_sah)
print(f'Добавлен ревьюер {petr_sah.name} {petr_sah.surname}.')
print(f'Список ревьюеров: {", ".join([reviewer.name + " " + reviewer.surname for reviewer in reviewer_list])}')
print()

# Студенты выставляют оценки:

print('До выставления оценок студентами:')
print(ivan_petr)
print()
print(semen_buk)
print()

denis_sav.rate_lec(ivan_petr, 'Ruby', 8)
denis_sav.rate_lec(ivan_petr, 'JavaScript', 10)
denis_sav.rate_lec(ivan_petr, 'Ruby', 9)
denis_sav.rate_lec(ivan_petr, 'Python', 10)

alex_shir.rate_lec(ivan_petr, 'Python', 7)
alex_shir.rate_lec(ivan_petr, 'JavaScript', 9)
alex_shir.rate_lec(ivan_petr, 'JavaScript', 7)
alex_shir.rate_lec(ivan_petr, 'Python', 7)

olga_akk.rate_lec(semen_buk, 'Git', 10)
olga_akk.rate_lec(semen_buk, 'Java', 9)
olga_akk.rate_lec(semen_buk, 'Java', 7)
olga_akk.rate_lec(semen_buk, 'Введение в программирование', 6)

alex_ovch.rate_lec(semen_buk, 'Git', 10)
alex_ovch.rate_lec(semen_buk, 'Java', 9)
alex_ovch.rate_lec(semen_buk, 'Java', 7)
alex_ovch.rate_lec(semen_buk, 'Java', 10)
print('Студенты выставляют оценки:')
print(ivan_petr)
print()
print(semen_buk)
print()
# Ревьюеры выставляют оценки:
print('До выставления оценок ревьюерами:')
print(denis_sav)
print()
print(alex_shir)
print()
print(olga_akk)
print()
print(alex_ovch)
print()
ivan_dmitr.rate_hw(denis_sav, 'Python', 6)
ivan_dmitr.rate_hw(denis_sav, 'Python', 7)
ivan_dmitr.rate_hw(denis_sav, 'Javascript', 5)
ivan_dmitr.rate_hw(denis_sav, 'Javascript', 8)
ivan_dmitr.rate_hw(denis_sav, 'Python', 9)
ivan_dmitr.rate_hw(denis_sav, 'Javascript', 5)

ivan_dmitr.rate_hw(alex_shir, 'Python', 9)
ivan_dmitr.rate_hw(alex_shir, 'Ruby', 4)
ivan_dmitr.rate_hw(alex_shir, 'Javascript', 9)
ivan_dmitr.rate_hw(alex_shir, 'Ruby', 8)
ivan_dmitr.rate_hw(alex_shir, 'Python', 9)
ivan_dmitr.rate_hw(alex_shir, 'Javascript', 5)

petr_sah.rate_hw(olga_akk, 'Git', 5)
petr_sah.rate_hw(olga_akk, 'Git', 6)
petr_sah.rate_hw(olga_akk, 'Java', 4)
petr_sah.rate_hw(olga_akk, 'Java', 8)
petr_sah.rate_hw(olga_akk, 'Введение в программирование', 8)
petr_sah.rate_hw(olga_akk, 'Java', 8)

petr_sah.rate_hw(alex_ovch, 'Git', 7)
petr_sah.rate_hw(alex_ovch, 'Git', 6)
petr_sah.rate_hw(alex_ovch, 'Java', 7)
petr_sah.rate_hw(alex_ovch, 'Java', 8)
petr_sah.rate_hw(alex_ovch, 'Git', 5)
petr_sah.rate_hw(alex_ovch, 'Java', 7)

print('Ревьюеры выставляют оценки:')
print()
print(denis_sav)
print()
print(alex_shir)
print()
print(olga_akk)
print()
print(alex_ovch)
print()
# Сравнение студентов:

print(f'Студент {denis_sav.name} {denis_sav.surname} учится лучше чем {alex_shir.name} {alex_shir.surname}? -',
      ('Нет', 'Да')[denis_sav > alex_shir])

print(f'Студент {alex_ovch.name} {alex_ovch.surname} учится лучше чем {olga_akk.name} {olga_akk.surname}? -',
      ('Нет', 'Да')[alex_ovch > olga_akk])

# Сравнение лекторов:
print()
print(f'У лектора {ivan_petr.name} {ivan_petr.surname} оценка выше чем {semen_buk.name} {semen_buk.surname}? -',
      ('Нет', 'Да')[ivan_petr > semen_buk])
print(f'У лектора {semen_buk.name} {semen_buk.surname} оценка выше чем {ivan_petr.name} {ivan_petr.surname}? -',
      ('Нет', 'Да')[semen_buk > ivan_petr])

print()
print(average_course_student(students_list, 'Java'))
print(average_course_lecturer(lecturer_list, 'Python'))
