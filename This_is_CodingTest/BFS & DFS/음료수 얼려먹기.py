n, m = map(int, input().split())

ice_cream = []
for _ in range(n + 1):
    ice_cream.append(list(map(int(input()))))


def dfs(x, y):
    if 1 <= x and x <= n and 1 <= y and y <= n:
        return False

    if ice_cream[x][y] == 0:
        ice_cream[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if ice_cream[i][j] == True:
            result += 1

print(result)

