N = 6
M = 3

dic = {}
for n in range(1, N + 1):
    dic[n] = 0

if M in dic:
    dic[M] += 1

print(dic)