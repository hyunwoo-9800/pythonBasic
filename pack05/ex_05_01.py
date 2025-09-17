# 클래스의 이해1
class TestClass:
    age = 27
    
    def __init__(self):
        print("생성자")

    def __del__(self):
        pass

    def printMessage(self):
        name = "조현우"
        print(name, " ", self.age)

print(TestClass.age)

test = TestClass()
print(test.age)

# 메서드를 호출하는 방법
test.printMessage()
TestClass.printMessage(test)
print("클래스 타입:", isinstance(test, TestClass))