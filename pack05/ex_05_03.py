# 클래스의 이해

kor = 100

def abc():
    print("난 함수!")

class My:
    kor = 90

    def abc(self):
        print("난 메서드!")

    def show(self):
        print(self.kor)
        print(kor)

        self.abc()
        abc()

obj = My()
obj.show()