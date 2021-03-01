n = int(input())

score = []
for _ in range(n):
    input_data = input().split()
    score.append((input_data[0],input_data[1]))


result = sorted(score, key=lambda student:student[1])

for hi in result:
    print(hi[0],end = " ")

