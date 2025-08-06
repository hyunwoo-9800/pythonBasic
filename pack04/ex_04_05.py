# 전역변수와 지역변수

player = '전국대표'  # 전역변수


def funcsoccer():
    name = '홍길동'
    player = '지역대표'  # 지역변수
    print(name, player)

# 지역변수의 우선순위가 높으므로 지역변수가 출려되는 것을 확인
funcsoccer()
