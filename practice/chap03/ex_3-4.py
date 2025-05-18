# while문을 이용한 * 찍기
i = 2

while i <= 3:
    j = 1
    while j <= 9:
        print('{0} * {1} = {2}'.format(i, j, i * j))
        j = j + 1
    i = i + 1
    print()