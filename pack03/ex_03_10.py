a = 1
hap = 0

while a <= 10:
    print(a, end=" ")

    if a % 2 == 0:
        hap += a
    a += 1

print('\n짝수의 합은 ' + str(hap))
