class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course):
        print("%s study %s" % (self.name, course))

    def watchMovie(self):
        if self.age < 18:
            print("%s can see Altman" % self.name)
        else:
            print("%s can see AV" % self.name)


if __name__ == '__main__':
    stu1 = Student('libin', 15)
    stu1.watchMovie()
    stu2 = Student('lili', 29)
    stu2.watchMovie()
