# 가변 인수 처리
def func1(*ar):
    print(ar)
    for i in ar:
        print('음식: ' + i)

func1('공기밥')
func1('비빔밥', '김밥')

def funt2(a, *ar):
    print(a)
    print(ar)
    for i in ar:
        print('배고플 때: ' + i)
        
funt2('비빔밥', '김밥', '볶음밥')
funt2('짜장', '짬뽕')