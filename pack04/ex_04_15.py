# 함수 장식자 2
def outer(func):
    def inner(no1, no2):
        print('결과는 {0}'.format(func(no1, no2)))

    return inner  # 클로저


@outer  # func 함수를 감싼 구조가 된다.
def func(n1, n2):
    return n1 + n2


func(3, 4)
