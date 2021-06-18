n, m = 5,5 # 데이터의 갯수 n, 수열의 합
data = [1,2,3,4,5]
result = 0
summary = 0
end = 0

for start in range(n):
    while summary < m and end < n:
        summary += data[end]
        end+= 1

    if summary == m:
        result += 1

    summary -= data[start]