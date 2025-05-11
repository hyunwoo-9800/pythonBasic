s1 = 'kbs mbc'
s1 = ' ' + s1[:4] + 'sbs ' + s1[4:]
print(s1)

print('공백제거', s1.strip())
s2 = s1.split(sep=' ')
print(s2)
print('-'.join(s2))

ss = '대한민국 만세'
print(ss.replace('대한민국', '파이썬'))