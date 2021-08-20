import collections



def top_freq1(input_: list[int], k: int) -> list:
    dict_ = collections.defaultdict(int)
    arr: list[int] = []

    for num in input_:
        dict_[num] += 1
        if dict_[num] >= k and num not in arr:
            arr.append(num)

    return arr


# zip을 이용한 풀이
def top_freq2(input_, k):
    return list(zip(*collections.Counter(input_).most_common(k)))[0]


def main():
    input_ = [1, 1, 1, 2, 2, 3]
    k = 2
    answer = top_freq2(input_, k)
    print(answer)


main()
