colors = ['red', 'green', 'blue', 'yellow']
a = 0

while a < len(colors):
    print("colors = ", colors[a])
    a += 1

print("colors 크기 = ", len(colors))

print('')

while colors:
    print("colors = ", colors)
    colors.pop()
    print(colors.pop())

print("colors 크기 = ", len(colors))
