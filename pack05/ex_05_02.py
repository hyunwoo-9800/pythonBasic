# 클래스의 이해2

class Car:
    handle = 0
    speed = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def showData(self):
        km = "킬로미터"
        msg = "속도: " + str(self.speed) + km
        return msg

car1 = Car("홍길동", 10)
print("car1의 데이터:", car1.handle, car1.name, car1.speed)
car1.color = "검정"   # car1 객체에 color 변수 추가

car2 = Car("조현우", 20)
print("car2의 데이터:", car2.handle, car2.name, car2.speed)

print(id(Car), id(car1), id(car2))  # 주소 확인
print("car1", car1.showData())
print("car2", car2.showData())
car1.speed = 50
print("car1", car1.showData())

print("car1 속도: ", car1.speed)
print("car2 속도: ", car2.speed)