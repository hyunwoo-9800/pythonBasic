price = {'사과': 2000, '감': 500, '바나나': 1000}
my = {'사과': 2, '감': 3}
imsi = (f for f in my)  # generator 객체(iterator)

for i in imsi:
    print("키 : ", i)
    print("값 : price는 {}, my는 {} ".format(price[i], my[i]))

bill = sum([price[i] * my[i] for i in my])
print("구매한 과일 값은 {}원".format(bill))
