import sys


def max_profit(nums: list[int]) -> int:
    max_price = 0
    min_price = sys.maxsize

    for i, price in enumerate(nums):
        min_price = min(price, min_price)
        max_price = max(price - min_price, max_price)
    return max_price


def main():
    input_ = [7, 1, 5, 3, 6, 4]
    answer = max_profit(input_)
    print(answer)


main()
