# nonlocal global 사용 예제

# 전역변수
a = 10
b = 20
c = 30
print("함수 수행 전 a: {}, b: {}, c: {}".format(a, b, c))


def foo():
    # 지역변수
    a = 40
    b = 50

    def bar():
        # b = 60
        # c = 70
        nonlocal b
        global c

        print("bar에서 출력1 a: {}, b: {}, c: {}".format(a, b, c))

        b = 80

        print("bar에서 출력2 a: {}, b: {}, c: {}".format(a, b, c))

        c = 90

        print("bar에서 출력3 a: {}, b: {}, c: {}".format(a, b, c))

    bar()

    print("foo에서 출력 a: {}, b: {}, c: {}".format(a, b, c))


foo()
print("함수 수행 후 a: {}, b: {}, c: {}".format(a, b, c))
