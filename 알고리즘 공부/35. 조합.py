import itertools


def combine(n: int, k: int) -> list[list[int]]:
    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    results = []

    dfs([], 1, k)
    return results


def main():
    n, k = 5, 2
    print(f"{combine(n ,k)}")
    print(f'{list(itertools.combinations(range(1, n + 1), k))}')


main()
