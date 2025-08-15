# 일반적인 함수 형태
def hap(x, y):
    return x + y;


print('일반 함수 hap = ', hap(1, 2))

# 위 코드를 람다로 표현하기
print('람다 함수 = ', (lambda x, y: x + y)(1, 2))

aaa = lambda x, y: x + y  # 람다 함수객체를 변수에 치환
print('람다 aaa = ', aaa(3, 4))  # 람다 함수를 실행

# 람다도 인수에 초긱삽 지정이 가능하다.
bbb = lambda a, su=10: a + su
print('bbb1 = ', bbb(5))
print('bbb2 = ', bbb(5, 6))

# 람다도 가변인수 지정이 가능하다.
ccc = lambda a, *tu, **di: print('ccc = ', a, tu, di)
ccc(1, 2, 3, m=4, n=5)

# 다른 함수에(filter())에서 람다 함수 사용하기
result = list(filter(lambda a: a < 5, range(10)))
print('result = ', result)

# 홀수 출력
print('홀수 = ', list(filter(lambda a: a % 2, range(10))))
