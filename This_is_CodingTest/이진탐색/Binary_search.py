# 선형 탐색
def sequential_search(n, target, array):
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1


# 이진 탐색 소스코드 구현(재귀함수)
def binary_search(array,target,start,end):
    if start > end:
        return None

    mid = (start + end) // 2

    if target == array[mid]:
        return mid


    elif target > array[mid]:
        return binary_search(array,target,mid+1,end)

    else:
        return binary_search(array,target,start,mid-1)


# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start,end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            start = mid - 1

        else:
            end = mid + 1

    return None
