t = ('a', 'b', 'c', 'd')
print('t : ', t)

print('크기는 ', len(t))
print('a 문자 값은 몇개? ', t.count('a'))
print('b 문자 검색 ', t.index('b'), '\n')

# 튜플 자료형의 데이터 변경 방법
p = (1, 2, 3)
# p[1] = 10                                 튜플 요소는 수정 불가
q = list(p)                                 # 튜플을 리스트로 형변환
print('q는 : ', q)
q[1] = 10
p = tuple(q)
print('p는 : ', p)
print(p[1:], '\n')                                # 튜플도 슬라이싱이 가능하다

print('요솟값 교환하기')
t1 = (10, 20)
print('t1 : ', t1)
a, b = t1
b, a = a, b
t1 = a, b
print('t1 : ', t1)
