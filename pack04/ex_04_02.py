# 매개변수가 없는 함수
# 함수가 호출되어야 실행
def dofunc1():
    print('dofunc1 호출')


# 매개변수가 있는 함수
# return을 생략해도 None 반환
def dofunc2(name):
    print('안녕', name)


def dofunc3(arg1, arg2):
    res = arg1 + arg2
    return res


# 함수 호출
dofunc1()
print('다른 거 하다가...')
dofunc1()
print(dofunc1)  # 함수명은 객체 주소를 기억
other = dofunc1  # 함수 주소를 치환
other()

print(dofunc2('한국인'))

print(dofunc3(10, 20))
print(dofunc3('파이썬', '만세'))