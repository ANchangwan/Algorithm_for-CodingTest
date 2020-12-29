change_type = [500,100,50,10]
count = 0
N = 1260

for x in change_type:
    count += N // x
    N %= x

print(count)
