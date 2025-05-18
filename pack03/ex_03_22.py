# 피보나치 수열 구하기
a = 0
b = 1

for n in range(0, 11):  # 11회 반복 수행
    print(a)
    temp = a
    a = b
    b = temp + b
