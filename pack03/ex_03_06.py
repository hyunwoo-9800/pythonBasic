jumsu = 60

if 90 <= jumsu:
    print('우수')
else:
    if 70 <= jumsu:
        print('보통')
    else:
        print('저조')

if 90 <= jumsu:
    pass
else:
    if 70 <= jumsu:
        pass
    else:
        print('난 언제 처리될까')
