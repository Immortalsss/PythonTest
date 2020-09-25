class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel


    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.gender, self.tel)

