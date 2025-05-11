# 스택 구현
print('리스트로 stack(Lifo) 처리')
sbs = [10, 20, 30]

sbs.append(40)                      # 요소 추가
print('sbs : ', sbs)

sbs.pop()                           # 마지막 요소 제거
print('sbs : ', sbs)

sbs.pop()                           # 마지막 요소 제거
print('sbs : ', sbs)

# 큐 구현
print('리스트로 queue(Fifo) 처리')
sbs = [10, 20, 30]

sbs.append(40)                      # 요소 추가
print('sbs : ', sbs)

sbs.pop(0)                          # 첫 번째 요소 제거
print('sbs : ', sbs)

sbs.pop(0)                          # 첫 번째 요소 제거
print('sbs : ', sbs)
