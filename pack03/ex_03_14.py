while True:
    a = int(input("확인할 숫자 : "))

    if a == 0:
        print("프로그램을 종료합니다.")
        break
    elif a % 2 == 0:
        print("%d는 짝수 랍니다." % a)
    elif a % 2 == 1:
        print("%d는 홀수 랍니다." % a)
