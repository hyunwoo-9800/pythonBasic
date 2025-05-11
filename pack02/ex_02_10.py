aa = [1, 2, 3, 4, 5]
print('aa : ', aa[0:2])

aa = [1, 2, 3, ['a', 'b', 'c'], 4, 5]               # 중첩 리스트도 가능
aa[0] = 100                                         # 리스트는 요솟값 변경이 가능
aa[3][0] = 'good'
print('aa : ', aa)
print('aa[0] : ', aa[0], '\naa[3][0]: ', aa[3][0])
print('aa[3][:2] : ', aa[3][:2])
print('aa[3][2] : ', aa[3][2])

# 리스트 내의 요솟값을 삭제할 수 도 있다.
aa.remove(4)                                        # 값 4를 삭제
print('aa : ', aa)

del aa[4]                                           # 4번째 위치한 값을 삭제
print('aa : ', aa)

aa[3].remove('c')                                   # ['a', 'b', 'c']에서 'c'가 삭제
print('aa : ', aa)

del aa[3][0]                                        # ['a', 'b']에서 0번째 값 삭제
print('aa : ', aa)
