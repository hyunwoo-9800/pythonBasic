# 클래스의 포함관계1

class PohamHandle:
    quantity = 0;  # 회전량을 기억한다.

    def leftTurn(self, quantity):  # 좌회전일 때 수행
        self.quantity = quantity
        return "좌회전"

    def rightTurn(self, quantity):  # 우회전일 때 수행
        self.quantity = quantity
        return "우회전"


class PohamCar:
    turnShow = "정지"

    def __init__(self, ownerName):
        self.ownerName = ownerName  # 객체별로 ownerName 멤버를 기억
        self.handle = PohamHandle()  # 클래스의 포함관계가 된다.

    def turnHandle(self, q):  # q 값으로 회전 방향 결정
        if 0 < q:
            self.turnShow = self.handle.rightTurn(q)
        elif q < 0:
            self.turnShow = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShow = "직진"


tom = PohamCar("tom")  # PohamCar 객체를 tom이 참조
tom.turnHandle(10)  # tom이 우회전
print(tom.ownerName + "의 회전량은 " + tom.turnShow + str(tom.handle.quantity))

oscar = PohamCar("oscar")  # PohamCar 객체를 oscar가 참조
oscar.turnHandle(-25)  # oscar가 좌회전
print(oscar.ownerName + "의 회전량은 " + oscar.turnShow + str(oscar.handle.quantity))