# n = 행 , m = 열 (열은 입력안받아도 됨)

# input 예시
# 3 4
# 0 1 0 0
# 0 0 0 0
# 0 0 1 0

n, m = map(int, input().split())

my_list = [list(map(int, input().split())) for _ in range(n)]

print(my_list)