# 일급 함수
def func1(a, b):
    return a + b


func2 = func1  # 함수의 수행 결과가 아닌 주소를 치환
print('func1 = ', func1(3, 4))
print('func2 = ', func2(3, 4), '\n')


def func3(func):  # 함수의 매개변수로 함수를 받는다.
    def func4():
        print('나는 내부 함수야~\n')

    func4()
    return func  # 함수의 반환값이 함수다.


mbc = func3(func1)  # 함수 호출 시에 인자로 함수를 전달한다.
print('mbc = ', mbc(3, 4))
