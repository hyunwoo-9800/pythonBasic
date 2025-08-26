# 리스트에서 특정 숫자를 찾는 함수 작성 후 특정 숫자의 포함 여부 확인하는 예제
datas = [1, 3, 5, 7, 3, 9, 2, 4, 6]

def checkfunc(x, i):
    if i in x:
        return print(i, ": 있어요")
    else:
        return print(i, ": 없어요")

checkfunc(datas, 2)
checkfunc(datas, 8)
checkfunc(datas, 1)
checkfunc(datas, 10)