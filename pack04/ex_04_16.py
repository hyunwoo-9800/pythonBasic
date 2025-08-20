# 재귀 함수 1
def countdown(n):
    if n == 0:                  # 멈춤 조건
        print('완료')
    else:                       # 재귀 케이스 : 더 작은 문제로 줄이기
        print(n ,end=' ')       # 줄바꿈 없이 숫자만 찍고
        countdown(n - 1)        # n을 1 줄여서 다시 호출(재귀 처리)
        
countdown(5)