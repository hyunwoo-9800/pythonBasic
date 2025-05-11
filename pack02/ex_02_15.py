a = {1, 2, 3, 1}
print('a : ', a)
print('a의 크기는 : ', len(a), '\n')

b = {3, 4}

print('a와 b의 합집합 : ', a.union(b))
print('a와 b의 교집합 : ', a.intersection(b))
print('a와 b의 차집합 : ', a.difference(b), '\n')

# 세트 자료형의 연산자로 처리
print('합집합(a | b) : %s ' % (a | b))
print('교집합(a & b) : %s ' % (a & b))
print('차집합(a - b) : %s ' % (a - b), '\n')

# print(b[0]) 세트는 인덱싱 불가
b.add(5)                                            # 요소 추가는 가능
print('요소를 추가한 후의 b는 ', b, '\n')

b.update({6, 7})
b.update([8, 9])                                    # 리스트 자료로도 갱신 가능
b.update((10, 11))                                  # 튜플의 자료로도 갱신 가능
print('요소를 추가한 후의 b는 ', b, '\n')

b.discard(7)                                        # 값 7을 삭제, 없으면 통과
b.remove(6)                                         # 값 6을 삭제, 없으면 에러
print('요소를 삭제한 후의 b는 ', b)
