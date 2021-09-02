import itertools


# 재귀호출 형식. (DFS)
def permute(nums: list[int]) -> list[list[int]]:
    def dfs(elements):

        if len(elements) == 0:
            results.append(prev_elements[:])


        for i in elements:

            next_elements = elements[:]
            next_elements.remove(i)


            prev_elements.append(i)

            dfs(next_elements)
            prev_elements.pop()


    results = []
    prev_elements = []
    dfs(nums)
    return results


def main():
    nums = [1, 2, 3]
    answer1 = permute(nums)
    answer2 = list(itertools.permutations(nums))

    print(answer1)
    print(answer2)


main()
