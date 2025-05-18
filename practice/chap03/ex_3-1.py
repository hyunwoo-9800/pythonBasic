# while문을 이용한 3의 배수 합 구하기

i = 1  # 카운트용 변수
hap = 0  # 합계 저장용 변수

while i <= 100:
    i += 1
    if i % 3 == 0:
        print("test", i)
        hap += i
print("1 ~ 100 사이의 정수중 3의 배수의 합은? " + str(hap))
