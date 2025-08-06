# 함수 선언 시 파라미터에 초기값 설정
def showplus(start, end=5):
    print(start + end)

showplus(2, 3)  # 각각의 파라미터에 값 대입
showplus(3)  # start에만 3, end는 초기값 5
showplus(start=2, end=3)  # 각각의 이름에 맞는 값이 대입
showplus(end=4, start=3)  # 각각의 이름에 맞는 값이 대입
showplus(2, end=3)  # start에는 2 end에는 3이 대입

# 아래와 같은 경우 에러 발생
# showplus(start=2, 3)  # 두 번째 인자가 상수이면 안된다.
# showplus(end=4, 3)  # 두 번째 인자가 상수이면 안된다.
