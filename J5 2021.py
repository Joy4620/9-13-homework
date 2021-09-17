M = int(input())
N = int(input())
K = int(input())

orders = []
for i in range(K):
    orders.append(input())

canvas = []

for j in range(M):
    canvas.append([1 for i in range(N)])

for j in range(K):

    if (orders[j])[0] == 'R':
        for i in range(len(canvas[0])):
            canvas[int((orders[j])[2])-1][i] *= -1

    if (orders[j])[0] == 'C':
        for i in range(len(canvas)):
            canvas[i][int((orders[j])[2])-1] *= -1

count = 0
for i in range(len(canvas)):
    count += canvas[i].count(-1)
print(count)

# print(canvas)
# print(f'{canvas[0]}\n{canvas[1]}\n{canvas[2]}')

# 1 is black, -1 is gold
