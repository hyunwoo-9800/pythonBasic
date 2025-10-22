# 클래스의 포함관계 2

class Fridge:
    isOpened = False    # 냉장고 문 개폐 여부 확인용 변수
    foods = []          # FoodData 타입 자료 저장용 변수
    
    # 냉장고 문열기용 메서드
    def open(self):
        self.isOpened = True
        print("냉장고 문을 열었습니다.\n")
        
    # 냉장고 음식물 넣기 메서드
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)    # 클래스의 포함
            print("냉장고에 음식물이 들어갔습니다.")
            self.list()
        else:
            print("냉장고 문이 닫혀 있습니다.")
            
    # 냉장고 문닫기 메서드
    def close(self):
        self.isOpened = False
        print("냉장고 문을 닫았습니다.\n")

    # 냉장고 속 음식물 확인용 메서드
    def list(self):
        for f in self.foods:
            print("-", f.irum, f.expiry_data)
        print()

# FoodData 클래스는 Fridge의 포함 대상으로 쓰인다.
class FoodData:
    def __init__(self, irum, expiry_data):
        self.irum = irum    # 생성된 객체의 고유 멤버변수에 값 기억
        self.expiry_data = expiry_data

f = Fridge()    # Fridge 클래스 타입의 객체 생성

apple = FoodData("사과", "2025-10-31")    # FoodData 객체 생성
f.open()
f.put(apple)
f.close()

cola = FoodData("콜라", "2027-10-31")    # FoodData 객체 생성
f.open()
f.put(cola)
f.close()