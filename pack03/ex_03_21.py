import re

ss = """파이썬[3]은 1991년 발표(發表)한 파이썬 프로그래밍 언어다. 파이썬은 파이썬 소프트웨어 재단이 관리한다,"""

ss1 = re.sub(r'[^가-힣\s]', '', ss)
print(ss1)

ss2 = ss1.split(" ")
print(ss2)

cou = {}  # 단어의 횟수 출력용 딕셔너리 형 변수
for i in ss2:
    if i in cou:
        cou[i] = cou[i] + 1
    else:
        cou[i] = 1

print(cou)
