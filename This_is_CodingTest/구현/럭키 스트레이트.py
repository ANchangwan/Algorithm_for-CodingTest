import sys
#1
n = sys.stdin.readline().split()

count = len(n) // 2

result1 = 0
result2 = 0
for i in range(len(n)):
    if i < count:
        result1 += int(n[i])
    else:
        result2 += int(n[i])

if result1 == result2:
    print("Lucky")
else:
    print("READY")

#2
n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(lengh // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0 :
    print("LUCKY")
else:
    print("READY")

#3
n = input()
length = (len(n)//2)
first = n[0:length]
second = n[length:]

first_sum = []
for i in first:
    first_sum.append(int(i))

second_sum = []
for i in second:
    second_sum.append(int(i))


if sum(first_sum) == sum(second_sum):
    print("LUCKY")
else:
    print("READY")