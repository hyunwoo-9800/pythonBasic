# 재귀 함수 2
def tot(n):
    print(n)                        # 지금 몇 번째인지 보여주기 (진행상황)
    if n == 1:                      # n이 1이면 여기서 끝
        print("탈출!")
        #return True                 # True는 파이썬에서 숫자 1처럼 동작
        return 1
    return n + tot(n - 1)           # n -1까지 합을 구해와서 n을 더함(재귀처리)

re = tot(10)
print('10까지의 합은', re, '\n')

# 위 함수의 수식 전개 과정
def tot_expr(n):
    if n == 1:
        return "1", 1           # 식은 "1", 값은 1
    expr_tail, val_tail = tot_expr(n - 1)
    expr = f"{n} + ({expr_tail})"   # 수식 누적
    return expr, n + val_tail

expr, val = tot_expr(10)
print("tot(10)")
print("=", expr)
print("=", val, '\n')

# 괄호 없는 버전
def tot_expr2(n):
    numbers = [str(i) for i in range(n, 0, -1)]
    expr = " + ".join(numbers)
    return expr, sum(range(1, n+1))

expr, val = tot_expr2(10)
print("tot(10)")
print("=", expr)
print("=", val)