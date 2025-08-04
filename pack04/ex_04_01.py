print(sum([3, 5, 7]))  # 리스트 요소의 합

print(int(1.7))  # 실수를 정수화
print(float(3))  # 정수를 실수화

print(str(5) + '숫자 오')  # 숫자를 문자화

a = 10
print('eval 결과 :', eval('a + 5'))  # 수식 모양의 문자열을 수식화
print(round(1.2), round(1.6))  # 반올림한 결과를 반환

b_list = [True, 1, False]
print(all(b_list))  # 리스트 요소 모두가 참이면 참
print(any(b_list))  # 리스트 요소중 하나라도 참이면 참

b_list2 = [1, 3, 2, 5, 7, 6]
print('모든 숫자가 10 미만인가?', all(a < 10 for a in b_list2))
print('숫자중 3 미만이 있나?', any(a < 3 for a in b_list2))

# x와 y 두 개의 리스트에 zip()을 사용하여 튜플 작성
x = [10, 20, 30]
y = ['a', 'b']
for i in zip(x, y):  # 30은 대응되는 짝이 없어 제외된다.
    print(i)
