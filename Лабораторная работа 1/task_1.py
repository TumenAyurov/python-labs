# TODO: Подробно описать три произвольных класса

import doctest


# TODO: описать класс

class Cat:
    def __init__(self, name: str = None, age: int = None, breed: str = None):
        """
        Создание объекта класса "Cat":

        :param name: Имя кота (str)
        :param age: Возраст кота (int)
        :param breed: Порода кота (str)

        Примеры:
        >>> cat1 = Cat("Barsik", 3, "Britan")   # Инициализация объекта класса
        """
        self.add_data(name, age, breed)

    def add_data(self, name: str = None, age: int = None, breed: str = None):
        """
        Функция добавления данных в объект.

        :param name: Имя кота (str)
        :param age: Возраст кота (int)
        :param breed: Порода кота (str)
        """
        self.name = name
        if age is None or age >= 0:  # Возраст не может быть отрицательным
            self.age = age
        else:
            raise ValueError("Значение не может быть отрицательным")
        self.breed = breed

    def print_data(self):
        """Вывод данных о коте."""
        print(self.name, self.age, self.breed)


# TODO: описать ещё класс


class Student:
    def __init__(self, surname: str = None, add_sessions: int = 0, is_in_university: bool = False):
        """
        Создание объекта класса "Student":

        :param surname: Фамилия студента (str)
        :param add_sessions: Количество допсессий у студента (int)
        :param is_in_university: Учится ли студент в ВУЗе (bool)

        Примеры:
        >>> student1 = Student("Ivanov", 1, True)   # Инициализация объекта класса
        """
        self.add_data(surname, add_sessions, is_in_university)

    def add_data(self, surname: str = None, add_sessions: int = 0, is_in_university: bool = None):
        """
        Функция добавления данных о студенте.

        :param surname: Фамилия студента (str)
        :param add_sessions: Количество допсессий (int)
        :param is_in_university: Учится ли студент (bool)
        """
        self.surname = surname
        if add_sessions >= 0:  # Студент не может иметь отрицательное количество допсессий
            self.add_sessions = add_sessions
        else:
            raise ValueError("Значение не может быть отрицательным")
        self.is_in_university = is_in_university
        if self.add_sessions > 5:  # Если количество допсессий больше 5-ти, студент считается отчисленным
            self.is_in_university = False


# TODO: и ещё один


class Prepod:
    def __init__(self, surname: str = None, number_of_students_expelled: int = None):
        """
        Создание объекта класса "Prepod":

        :param surname: Фамилия преподавателя (str)
        :param number_of_students_expelled: Количество отчисленных студентов (int)

        Примеры:
        >>> prepod1 = Prepod("Zelikman", 18634)   # Инициализация объекта класса
        """
        self.add_data(surname, number_of_students_expelled)

    def add_data(self, surname: str = None, number_of_students_expelled: int = None):
        """
        Функция добавления данных о преподавателе.

        :param surname: Фамилия преподавателя (str)
        :param number_of_students_expelled: Количество отчисленных студентов (int)
        """
        self.surname = surname
        if number_of_students_expelled is None or number_of_students_expelled >= 0:
            self.number_of_students_expelled = number_of_students_expelled
        else:
            raise ValueError("Значение не может быть отрицательным")

    def print_data(self):
        """Вывод данных о преподавателе."""
        print(self.surname, self.number_of_students_expelled)
