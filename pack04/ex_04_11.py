# 클로저의 이해 2
def outer2(tax):  # 매개변수 tax는 outer2의 지역변수
    def inner2(su, dan):
        amount = su * dan * tax  # 수량 * 단가 * 세금
        return amount  # inner2 함수는 amount를 반환

    return inner2  # outer2는 inner2 함수의 주소를 반환(클로저)


# 1분기에는 수량 * 단가에 tax를 0.1 부과
q1 = outer2(0.1)
print('result1 = ', q1(5, 10000))
print('result2 = ', q1(10, 20000), '\n')

# 2분기에는 수량 * 단가에 tax를 0.05 부과
q2 = outer2(0.05)
print('result3 = ', q2(5, 10000))
print('result4 = ', q2(10, 20000))
