# packing 연산
v1, *v2 = 1, 2, 3, 4, 5
print(v1)
print(v2)

print("\n")

# packing을 위한 변수 위치 변경
*v1, v2 = 1, 2, 3, 4, 5
print(v1)
print(v2)

print("\n")

# 변수 1만 packing 처리
*v1, v2, v3 = 1, 2, 3, 4, 5
print(v1)
print(v2)
print(v3)

print("\n")

# 변수 2만 packing 처리
v1, *v2, v3 = 1, 2, 3, 4, 5
print(v1)
print(v2)
print(v3)