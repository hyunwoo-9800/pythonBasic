# 얕은 복사(같은 객체를 참조)
name1 = ['톰', '존']
name2 = name1

# name1, 2는 주소가 같다
print('name1 : ', name1, 'id(name1) : ', id(name1))
print('name2 : ', name2, 'id(name2) : ', id(name2))
name1[0] = '수잔'
print('name1 : ', name1, 'id(name1) : ', id(name1))
print('name2 : ', name2, 'id(name2) : ', id(name2))

# 깊은 복사
import copy

name3 = copy.deepcopy(name1)
name1[0] = '폴'
print('name1 : ', name1, 'id(name1) : ', id(name1))
print('name2 : ', name2, 'id(name2) : ', id(name2))
print('name3 : ', name3, 'id(name3) : ', id(name3))
