# 상속

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "안녕하세요 저는 {}이고 학생입니다.".format(self.name)

class EStudent(Student): # Student 상속
    def __str__(self):
        return "안녕하세요 저는 {}이고 초등학생입니다.".format(self.name)
    
    def print_age(self):
        print('{}의 나이는 {}살입니다.'.format(self.name, self.age))

class MStudent(Student): # Student 상속
    def __str__(self):
        return "안녕하세요 저는 {}이고 중학생입니다.".format(self.name)

ho = Student('호', 4)
hy = EStudent('히', 1)
he = MStudent('헤', 5)

print(ho)
print(hy)
print(he)

hy.print_age()
# ho.print_age()
