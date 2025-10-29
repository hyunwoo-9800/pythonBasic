# 메서드 오버라이드 1

class Parent:
    def printData(self):    # 부모 메서드(수행 내용 없음)
        pass
    
class Child1:
    def pirntData(self):
        print("자식1에서 오버라이드")

class Child2:
    def pirntData(self):
        print("자식2에서 오버라이딩")
        print("부모 메서드와 이름은 같으나 기능은 다름")

c1 = Child1()
c1.pirntData()
c2 = Child2()
c2.pirntData()

# 다형성 처리
par = c1
par.pirntData()

par = c2
par.pirntData()

plist = [c1, c2]    # 자식 개체 참조변수를 리스트에 저장

for item in plist:
    item.pirntData()