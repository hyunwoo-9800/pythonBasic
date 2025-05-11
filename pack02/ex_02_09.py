# a는 리스트 변수로 묶음 자료를 참조한다.
a = [1, 2, 3]
print('a : ', a)

# 리스트 자료형은 다양한 데이터를 기억할 수 있다.
b = [10, a, 20.5, True, '문자열']
print('b : ', b)
print('id(a) : ', id(a) ,'\nid(b) : ', id(b))

friends = ['오공', '팔계', '오정']
print('친구 목록 : ', friends)
print('친구 수 : ', len(friends))
print('세 번째 친구는 : ', friends[2])

friends.append('관우')
friends.remove('오공')
friends.insert(0, '관우')
friends.extend(['조조', '여포'])
friends += ['손권']
print('친구 목록 : ', friends)

print('저팔계는 몇 번째? ', friends.index('팔계'))
print('관우 있나? ', '관우' in friends)
print('동탁 있나? ', '동탁' in friends)
