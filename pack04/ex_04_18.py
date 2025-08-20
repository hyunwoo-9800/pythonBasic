# 팩토리얼 계산
def factorial(n):
    if n == 0:
        return 1
    print(n)
    return n * factorial(n - 1)

print('5!은?', factorial(5), '\n')

# 위 함수의 수식 전개 과정
def factorial_expr(n):
    if n == 0:
        return "1", 1                # 0! = 1
    if n == 1:
        return "1", 1                # 1! = 1
    expr_tail, val_tail = factorial_expr(n - 1)
    expr = f"{n} * ({expr_tail})"    # 문자열 전개
    return expr, n * val_tail

expr, val = factorial_expr(5)
print("5! 전개:")
print("=", expr)
print("=", val, '\n')

# 괄호 없는 버전
def factorial_expr2(n):
    numbers = [str(i) for i in range(n, 0, -1)]
    expr = " * ".join(numbers)
    return expr, eval(expr)

expr, val = factorial_expr2(5)
print("5! 전개:")
print("=", expr)
print("=", val)
