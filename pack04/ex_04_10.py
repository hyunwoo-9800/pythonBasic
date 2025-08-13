# 클로저의 이해 1
def outer():
    count = 0

    def inner():  # 내부함수
        nonlocal count
        count += 1
        return count

    return inner  # 이 부분이 클로저 내부 함수의 주소를 반환한다.


# 함수 내부의 count 값 확인하기
var1 = outer()
print("var1 = ", var1())  # 변숫값이 유지된다.
print("var1 = ", var1())  # 변숫값이 계속 유지된다.
print("var1 = ", var1())  # 변숫값이 계속 유지된다.
print("var1 = ", var1())  # 변숫값이 계속 유지된다.
print("var1 = ", var1())  # 변숫값이 계속 유지된다.
print("var1 = ", var1(), '\n')  # 변숫값이 계속 유지된다.


var2 = outer()
print("var2 = ", var2())
