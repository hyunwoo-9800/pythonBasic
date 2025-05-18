# while문을 이용한 숫자 맞추기
import random

num = random.randint(1,10)
print("num = %d" % num)

while True:
    user = int(input("1 - 10사이의 숫자를 입력해 주세요 : "))
    if user != num:
        print("틀렸습니다.")
        continue
    else :
        print("컴퓨터 숫자는 %d" % num + " 맞췄습니다.")
        break