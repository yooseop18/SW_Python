# n = 행 , m = 열 (열은 입력안받아도 됨)

# input 예시
# 3 4
# 0 1 0 0
# 0 0 0 0
# 0 0 1 0

n, m = map(int, input().split())

my_list = [list(map(int, input().split())) for _ in range(n)]

print(my_list)

#####################
# 단순 행, 열만 입력 받으려면 이게 제일 간단함
# 이게 제일 간단함

matrix = [[0 for i in range(3)] for j in range(4)]

