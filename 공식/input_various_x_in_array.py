# 한칸 띄어진 채로 input 값 넣기
# ex> 1 2 3 4 5

num_ = [int(x) for x in input().split()]

# map 함수로 입력받기 ; 변수 하나씩 입력받을 때 편리
a, b, c, d, e = map(int, input().split())

print(num_)
print(f'{a} {b}')
