# 함수 장식자 1
def make2(make1fn):
    # make1이 실행된 "안녕 반가워 홍길동"을 반환하는 람다 함수의 주소를 반환
    return lambda : "안녕 " + make1fn()

def make1(hellofn):
    # hello가 실행된 "반가워 홍길동"을 반환하는 람다 함수의 주소를 반환
    return lambda : "반가워 " + hellofn()

def hello():
    return "홍길동"

hi = make2(make1(hello))        # 일반적인 함수 처리 방법
print('hi = ', hi())

@make2                          # 함수 장식자 처리 방법
@make1
def hello2():
    return '신기해'

hi2 = hello2()
print('hi2 = ', hi2)