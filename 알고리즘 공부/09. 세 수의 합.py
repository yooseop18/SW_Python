def three_sum(nums: list[int]) -> list[int]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복값 건너뛰기기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 투 포인터로 간격 조사
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0 -> 정답
                results.append([nums[i], nums[left], nums[right]])

                # 같은 수가 있을 경우, 다음 숫자 확인
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # left, right 한칸 씩 넘김
                left += 1
                right -= 1

    return results


def main():
    input_ = [-1, 0, 1, 2, -1, -4]
    answer = three_sum(input_)

    print(answer)


main()

