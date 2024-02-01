class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 16:
            print("%s age < 16" % self._name)
        else:
            print("%s age > 16" % self._name)


class Student(Person):

    def __init__(self, name, age, grade):
        super.__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print("%s grade %s is study %s" % (self._grade, self._name, course))


class Teacher(Person):

    def __init__(self, name, age, title):
        super.__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
