for i in [1, 2, 3, 4, 5]:
    print(i, end=" ")
print()

for c in ['red', 'green', 'blue']:
    print(c, end=" ")
print()

for n in {'one', 'two', 'three'}:
    print(n, end=" ")
print()

for t in ('house', 'mouse', 'horse'):
    print(t, end=" ")
print()

soft = {'java': '웹용', 'python': '만능', 'oracle': 'db'}

for i in soft.items():
    print(i[0] + ', ' + i[1])
print()

for v in soft.values():
    print(v, end=" ")
