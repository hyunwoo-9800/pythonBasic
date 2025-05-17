no = 10

# 일반적인 if문
if 5 < no:
    re = no * 2
else:
    re = no + 2
print("re =", str(re))

# 삼항연산자 사용
re = no * 2 if 5 < no else no + 2
print("re =", str(re))

a = "kbs"
b = 9 if a == "kbs" else 11
print("b =", b)
