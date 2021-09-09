def test3(Ai, Bj):
    max_result = 0
    # 각 자리 수 만큼 연산, 길이가 같아질때 까지 짧은 행렬 앞에 0을 추가
    while True:
        # 더 짧은 행렬 수를 찾음
        if len(Ai) <= len(Bj):
            iter_v = len(Ai)
        else:
            iter_v = len(Bj)

        result = 0
        for i in range(iter_v):
            result += Ai[i] * Bj[i]
        # 찾은 값이 max 값이면, 갱신
        if result > max_result:
            max_result = result
        # 두 배열의 길이가 같아지면 종료, 그외에는 짧은 배열에 0 삽입
        if len(Ai) == len(Bj):
            break
        else:
            if len(Ai) <= len(Bj):
                Ai.insert(0, 0)
            else:
                Bj.insert(0, 0)


    return max_result


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        # 입력은 받지만, 쓰지는 않음 (배열 길이는 len() 으로 활용)
        N, M = map(int, input().split())

        Ai = [int(x) for x in input().split()]
        Bj = [int(y) for y in input().split()]

        answer = test3(Ai, Bj)

        print(f'#{test_case} {answer}')


if __name__ == '__main__':
    main()
