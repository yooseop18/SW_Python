# Q: n개의 페어를 이용한 min(a,b)의 합으로 가장 큰 수를 출력

def array_pair_sum(nums: list[int]) -> int:
    nums.sort()
    pair = []
    sum_ = 0

    # 무조건 2개의 페어로 잡고, 탐색하면 최대값 출력 가능
    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum_ += min(pair)
            pair = []

    return sum_


    # 파이썬 다운 코드
def python_(nums: list[int]) -> int:
    return sum(sorted(nums)[::2])   # 어차피 2개씩 묶어서 비교하니까, 소팅하고 짝수 번쨰 숫자만 합하기


def main():
    input_ = [1, 4, 3, 2]
    answer = array_pair_sum(input_)

    print(answer)


main()
