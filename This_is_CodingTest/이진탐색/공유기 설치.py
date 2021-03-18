n,c = list(map(int,input().split(' ')))

# 전체 집의 좌표 정보를 입력받기
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while(start <= end):
    mid =(start + end) // 2
    value = array[0]
    count  = 1
    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1,n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
