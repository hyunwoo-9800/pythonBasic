for i in range(6):
    print(i, end=" ")

print()
for _ in range(1, 3):  # range의 반환값을 사용하지 않을 떼 _ 사용
    print("안녕")

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11):
    tot += i
print("합은 : " + str(tot))

matrix = [[1, 2, 3], [4, 5, 6]]  # 중첩 리스트
for m in range(2):
    for n in range(3):
        print(matrix[m][n], end=" ")
    print()
