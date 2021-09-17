T = input()
S = input()

for i in range(len(S)):
    S = S[1:] + S[0]
    if S in T:
        print('yes')
        quit()

print('no')
