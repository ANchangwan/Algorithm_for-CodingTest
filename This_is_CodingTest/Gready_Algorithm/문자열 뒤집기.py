import sys

s = sys.stdin.readline().strip()
count_zero = 0
count_one = 0
result = 0

if s[0] == '1':
    count_zero += 1
else:
    count_one += 1

for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count_zero +=1
        else:
            count_one += 1

result= min(count_zero,count_one)
print(result)