def combination_sum(candidate: list[int], target: int) -> list[list[int]]:
    result = []

    # csum = target 값을 찾기 위한 갱신 값. 초기값 = target 설정 뒤 숫자를 빼는 형식
    # index = 순서
    # path = 지금까지의 탐색 경로

    def dfs(csum, index, path):
        # 목표값을 초과한 경우. 탐색종료
        if csum < 0:
            return
        # 목표값을 찾은 경우. result 에 추가하고 탐색 종료
        if csum == 0:
            result.append(path)
            return

        for i in range(index, len(candidate)):
            dfs(csum - candidate[i], i, path + [candidate[i]])


    dfs(target, 0, [])

    return result


def main():
    candidate = [2, 3, 6, 7]
    target = 7

    print(f'{combination_sum(candidate, target)}')


if __name__ == '__main__':
    main()
