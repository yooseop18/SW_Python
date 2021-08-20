def binarySearch(arr):
    arr.sort()
    target = int(input())
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] is target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def binarySearch_rec(arr, target=None, start=None, end=None):
    arr.sort()

    target, start, end = target or int(input()), start or 0, end or len(arr) - 1

    if start > end:
        return - 1
    mid = (start + end) // 2
    if arr[mid] > target:
        return binarySearch_rec(arr, target, start, mid)
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binarySearch_rec(arr, target, mid + 1, end)


def main():
    arr = [6, 5, 3, 1, 8, 7, 2, 4]

    idx = binarySearch(arr)

    if idx == -1:
        print("Not in array")
    else:
        print(arr[idx])


if __name__ == "__main__":
    main()
