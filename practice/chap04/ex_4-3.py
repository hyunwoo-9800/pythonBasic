# 재귀함수로 구구단 3단 출력
def gugu(n, i = 1):
    if 9 < i:              # 9단까지 끝나면 종료
        return
    print(f"{n} x {i} = {n*i}")
    gugu(n, i+1)           # 다음 곱으로 재귀 호출

# 실행
gugu(3)
