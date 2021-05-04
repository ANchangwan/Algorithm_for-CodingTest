def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_team(check,a,b):
    a = find_parent(check,a)
    b = find_parent(check,b)
    if a < b:
        check[a] = b
    else:
        check[b] = a



n,m = map(int,input().split())
check = [0] * (n+1)

for i in range(0,n+1):
    check[i] = i

for _ in range(m):
    team_check, a, b = map(int,input().split())
    if team_check == 0:
        union_team(check,a,b)

    elif team_check == 1:
        if find_parent(check,a) == find_parent(check,b):
            print('YES')
        else:
            print('NO')





