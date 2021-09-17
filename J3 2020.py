xlist = []
ylist = []

for i in range(int(input())):
    x, y = input().split(',')
    xlist.append(int(x))
    ylist.append(int(y))

print(f'{min(xlist)-1},{min(ylist)-1}')
print(f'{max(xlist)+1},{max(ylist)+1}')

'''
Top left (min(x), max(y))
Top right (max(x), max(y))
Bottom left (min(x), min(y))
Bottom right (max(x), min(y))

Order: bottom left, top right
'''

