import sys

s = sys.stdin.readline().strip() # 문자열 공백을 제거해야 하기 때문에 strip을 사용해서 제거
                                # strip을 사용하지않으면 ValueErrpr 발생
result = 1

print(type(s))
for x in s:         # 문자열을 인덱스 0부터 차례대로 불러온다.
    x = int(x)      # 문자열을 인덱스 0부터 차례대로 인트형으로 바꾼다.
    if x == 0:      # 만약 문자열이 0이면 모든 숫자가 0이 되기 때문에 1을 곱해준다.
        result *= 1
    else:
        result *= x # 그외 숫자는 모두 곱해준다. 그래야 최댓값을 얻을 수 있다.

print(result)