aa = [3, 1, 5, 2, 4]

# 오름차순 정렬
aa.sort();
print('오름차순 정렬 : ', aa)

# 내림차순 정렬
aa.sort(reverse=True)
print('내림차순 정렬 : ', aa)

# 문자열 정렬
aa2 = ['123', '34', '234']

print('정렬 전 aa2 : ', aa2)

aa2.sort()  # 사전순 정렬
print('사전순 정렬 : ', aa2)

aa2.sort(key=int)  # 문자열이지만 숫자형으로 정렬
print('숫자형 정렬 : ', aa2)

aa2 = [3, 1, 2]
aa3 = sorted(aa2)
print('aa2의 값 : ', aa2)
print('정렬된 aa3 : ', aa3)
