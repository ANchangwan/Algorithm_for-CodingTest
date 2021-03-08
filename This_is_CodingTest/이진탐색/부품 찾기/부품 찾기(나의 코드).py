import sys
n = sys.stdin.readline().rstrip()
part = list(map(int, input().split()))

m = sys.stdin.readline().rstrip()
customer_part = list(map(int,input().split()))

part.sort()
customer_part.sort()

def binary_search(have_part,customer_part,start,end):
    for target in customer_part:
        while start <= end:
            mid = (start + end) // 2

            if target == have_part[mid]:
                return True

            elif target > have_part[mid]:
                start = mid + 1

            else:
                end = mid - 1

    return False

if binary_search(part,customer_part,0,len(part)):
    print("yes")
else:
    print("No")