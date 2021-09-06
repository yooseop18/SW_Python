def test2(arr, target):
    result = []

    # path = 지금까지의 경로 : list
    def dfs(csum, index, path):
        if csum < 0:
            return

        if csum == 0:
            result.append(path)
            return

        for i in range(index, len(arr)):
            dfs(csum - arr[i], i, path + [arr[i]])

    dfs(target, 0, [])

    return result


def main():
    candidate = [2, 3, 6, 7]
    target = 7

    print(f'{test2(candidate, target)}')


if __name__ == '__main__':
    main()
