T = int(input())
# 조건문 덕지덕지 붙이는 것 보다 내장함수 사용하는 것이 실행속도가 훨씬 빠름
# 내장함수 사용에 익숙해지자.
result = []
for _ in range(T):
    a, b, c, d = map(int, input().split())
    start = max(a, c)
    end = min(b, d)
    result.append(max(0, end - start))

for test_case in range(1, T + 1):
    print(f'#{test_case} {result[test_case - 1]}')