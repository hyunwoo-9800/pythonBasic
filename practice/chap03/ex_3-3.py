# while문을 이용한 * 찍기
i = 0

while i <= 5:
    j = 0
    while j <= 5:
        if j < i:
            print("*", end="")
        j = j + 1
    i = i + 1
    print()
