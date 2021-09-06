def subsets(arr: list[int]) -> list[list[int]]:
    result = []

    def dfs(index, path):
        if len(path) != 0:
            result.append(path)

        for i in range(index, len(arr)):
            dfs(i + 1, path + [arr[i]])


    dfs(0, [])
    return result


def main():
    arr = [1, 2, 3]

    print(f'{subsets(arr)}')


if __name__ == '__main__':
    main()

