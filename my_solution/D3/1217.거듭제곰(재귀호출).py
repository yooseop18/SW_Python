def test3(N, M):
    # 재귀호출을 이용한 구현, 재귀호출 아니면 개 쉬움
    # 2**5 = 2 * 2 * 2 * 2 * 2
    result = N
    if M == 1:
        # M = 1 이 되면 곱해야 하는 수 반환(N)
        return N
    # 제곱해야 하는 수만큼 재귀호출로 찾기
    result *= test3(N, M - 1)
    return result


def main():
    for _ in range(1, 11):
        test_case = int(input())
        N, M = map(int, input().split())
        answer = test3(N, M)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
