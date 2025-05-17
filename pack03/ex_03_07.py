jumsu = int(input('점수 입력 : '))  # 값을 입력받고, 형변환

if 90 <= jumsu <= 100:
    result = "A"
    score = 1
elif 80 <= jumsu <= 90:
    result = "B"
    score = 2
else:
    result = "C"
    score = 3

print("result = ", result)
print("score = ", str(score))  # 문자열로 변환
