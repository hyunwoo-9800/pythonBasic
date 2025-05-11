s = 'sequence'

print('길이(크기) : ', len(s))
print('포함 횟수 : ', s.count('e'))
print('검색 위치 : ', s.find('e'), s.find('e', 3), s.rfind('e'))
print('첫 글자 유무 : ', s.startswith('s'), s.startswith('a'))
print('해당 요솟값 유무 : ', 'e' in s)

# 인덱싱과 슬라이싱 처리
print('s[0], s[7] : ', s[0], '', s[7])
print('s[1:], s[1::2] : ', s[1:], '', s[1::2])  # s[1::2] = 1번째 인덱스 부터 2씩 증가하면서 출력
print('s[:3], s[3:] : ', s[:3], '', s[3:])
print('s[-1], s[-8]' , s[-1], '', s[-8])
print('s[-4:], s[::3] : ', s[-4:], '', s[::3])
print('s[1:7:1], s[1:7] : ', s[1:7:1], '', s[1:7])

print('값 변경 전 : ', id(s))
s = 'fre' + s[2:]
print(s)
print('값 변경 후 : ', id(s))
