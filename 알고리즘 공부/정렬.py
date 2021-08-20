import heapq


def selection_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_idx = arr.index(max(arr[:i]))
        if arr[i] > arr[max_idx]:
            pass
        else:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
    print(arr)


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    print(arr)


def merge_sort(arr):
    # print(merged_sort)하면 오류남 ... 왜그러지?
    # 아 ㅅㅂ 재귀함수라서 그렇구나 무조건 return 값이 있어야함
    if len(arr) < 2:
        return arr

    # split 부분, 배열 길이가 1이 될 때 까지 low_, high_ 로 나눔
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    #    print("low {}".format(low_arr))
    #    print("high {}".format(high_arr))

    # merge 부분, 작은 수를 merged_ 에 넣고, 나머지를 뒤에 삽입
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        #            print("merged_l {}".format(merged_arr))
        else:
            merged_arr.append(high_arr[h])
            h += 1
    #           print("merged_h {}".format(merged_arr))

    # list += 할 때, null 값일 때 그냥 아무일도 안일어남!
    # append() 사용 시, [] 가 삽입됨

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    #    print("merged {}".format(merged_arr))
    #    print()
    return merged_arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


def heap_sort(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    print(heap)

    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums


def main():
    # arr = [int(x) for x in input().split()]
    arr = [6, 5, 3, 1, 8, 7, 2, 4]

    # selectionSort(arr)

    # bubbleSort(arr)

    # insertionSort(arr)

    print(heap_sort(arr))


main()
