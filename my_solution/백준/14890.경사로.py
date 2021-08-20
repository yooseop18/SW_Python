N, L = map(int, input().split())

mylist = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

for i in range(N):

#print(len(mylist[0]))