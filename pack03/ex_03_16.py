chars = []
sentence = '파이썬은 기능이 좋은 언어'

for k in sentence:
    chars.append(k)  # sentence 변수의 문자열이 한 글자씩 차례대로 리스트에 저장됨

print(chars)

for k in chars:
    if k != ' ':  # 공백을 제외한 문자 출력
        print(k, end='')
