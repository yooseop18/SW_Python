def test3(arr):
    # 최대, 최소값 빼기
    arr.remove(max(arr))
    arr.remove(min(arr))
    result = 0
    for i in arr:
        result += i
    # 평균값 1의자리 반올림 출력
    return round(result / len(arr))


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        arr = [int(x) for x in input().split()]
        answer = test3(arr)
        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()