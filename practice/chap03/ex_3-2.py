# while문을 이용한 3의 배수이면서 2의 배수가 아닌 수 출력

i = 1  # 카운트용 변수
hap = 0  # 합계 저장용 변수

while i <= 100:
    i += 1
    if i % 3 == 0:
        if i % 2 == 0:
            continue
        print("i = ", i)
        hap += i
print("1 ~ 100 사이의 정수중 3의 배수이면서 2의 배수가 아닌 수의 합은? " + str(hap))