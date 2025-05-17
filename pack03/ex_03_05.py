money = 1000
age = 23

if 500 <= money:
    item = 'apple'

    if age <= 30:
        msg = 'young'
    else:
        msg = 'old'

else:
    item = '사과'

    if 20 <= age:
        msg = '어른'
    else:
        msg = '아이'

print(item, msg)
