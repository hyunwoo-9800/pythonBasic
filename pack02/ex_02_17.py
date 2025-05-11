mydic = dict(k1=1, k2='abc', k3=3.4)
print('mydic : ', mydic, '\n')

coffee = {'mocha': '카페모카', 'latte': '라떼'}
print('coffee : ', coffee)
print('커피의 크기는? ', len(coffee))
print(coffee['mocha'], '\n')
# print(coffee['카페모카'])                                         값으로 조회하면 에러

print('커피의 키는 : ', coffee.keys())
print('커피의 값은 : ', coffee.values())
print('커피의 키와 값은 : ', coffee.items(), '\n')

print(list(coffee.keys()))                                      # key를 리스트 형태로 출력
print(list(coffee.values()), '\n')                              # values 리스트 형태로 출력

print(coffee.get('latte'), '\n')                                # key로 value 얻기

print('latte' in coffee, '\n')                                  # key의 유무를 판단

coffee['lungo'] = '룽고'                                         # 요소 추가
print('coffee : ', coffee)
del coffee['lungo']                                             # 요소 삭제
print('coffee : ', coffee)

drink = {'cola': '콜라'}                                         # 딕셔너리 형 자료
water = {**coffee, **drink}
print('water : ', water)
