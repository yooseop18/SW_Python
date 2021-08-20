import sys

mx = -sys.maxsize   # -922222213131... 이거보다 작은 숫자는 거의 없으니 초기값을 이것으로 설정하면 좋음
mn = sys.maxsize    # 마찬가지, 이거보다 큰 숫자 입력받을 일이 없으니 초기값으로 좋음

print(mx)
print(mn)

mx = float('-inf')  # 무한대로 지정하기도 있음. 만약 sys 모듈 사용 못하면 이렇게
mn = float('inf')

print(mx)
print(mn)