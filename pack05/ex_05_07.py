# 클래스의 상속관계 1

class Animal:
    def move(self):
        print("움직이는 생물")

class Dog(Animal):              # Animal 클래스 상속
    def my(self):               # Dog 클래스의 고유 메서드
        print("나는 강아지")

dog1 = Dog()
dog1.my()
dog1.move()

class Horse(Animal):              # Animal 클래스 상속
    pass                          # Horse 클래스는 자체 멤버가 없는 클래스가 된다.

horse1 = Horse()
horse1.move()