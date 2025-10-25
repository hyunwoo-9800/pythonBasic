# 클래스의 상속관계 2

class Person:
    say = "난 사람~"
    nai = 20

    def __init__(self, nai):
        print("Person 생성자")
        self.nai = nai

    def printInfo(self):
        print("say : {}, nai : {}".format(self.say, self.nai))

person = Person("22")
person.printInfo()

print("Employee 클래스 처리 ---")
class Employee(Person):
    say = "일하는 동물"
    subject = "근로자"

    def __init__(self):
        print("Employee 생성자")

    def eprintInfo(self):
        self.printInfo()
        super().printInfo()
        print(self.say)
        print(super().say)

    def printInfo(self):
        print("오바라이딩 : 부모와 같은 이름의 메서드를 자식에서도 선언")

empl = Employee()
print(empl.say, empl.nai, empl.subject)
empl.eprintInfo()

print("Worker 클래스 처리 ---")
class Worker(Person):

    def __init__(self, nai):
        print("Worker 생성자")
        super().__init__(nai)

    def wprintInfo(self):
        self.printInfo()

work = Worker("31")
print(work.say, work.nai)
work.wprintInfo()

print("Programmer 클래스 처리 ---")
class Programmer(Worker):

    def __init__(self, nai):
        print("Programmer 생성자")
        # super().__init__(nai)
        Worker.__init__(self, nai)

    def pprintInfo(self):
        self.printInfo()
        super().printInfo()

pr = Programmer("33")
print(pr.say, pr.nai)
pr.pprintInfo()