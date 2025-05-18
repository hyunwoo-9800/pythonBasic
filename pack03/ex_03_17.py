datas = [1, 2, 3, 4, 5]

for i in datas:
    if i == 3: continue
    if i == 4: break
    print(i)

print()

jumsu = [95, 70, 60, 50, 100]
number = 0

for jum in jumsu:
    number += 1
    if jum < 70: continue
    print("%d번째 응시자는 합격" % number)
