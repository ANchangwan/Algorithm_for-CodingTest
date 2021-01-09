import sys

s = sys.stdin.readline().strip()
count_zero = 0
count_one = 0
result = 0
for i in range(len(s)):
    if s[i] == '0':
        count_zero += 1
    else:
        count_one += 1

if count_zero > count_one:
    result += 1
else:
    result += 1

print(result)