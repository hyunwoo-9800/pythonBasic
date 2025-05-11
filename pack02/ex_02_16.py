a = {1, 2, 3, 1}
print('set(a) : ', a)
print('tuple(a) : ', tuple(a))
print('list(a) : ', list(a), '\n')

li = [1, 2, 2, 3, 1]

print('리스트 li : ', li, '\n')

s = set(li)  # 세트로 형변환하면 중복된 자료가 없어진다
print('s : ', s, '\n')

li = list(s)
print('변환 후 li : ', li)
