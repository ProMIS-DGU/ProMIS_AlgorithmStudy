import sys
sys.setrecursionlimit(10**6) #dfs 사용할 때 붙여야 함.
input = sys.stdin.readline


def dfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]

    graph[x][y] = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:

    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    result=0
    graph =[]


    for _ in range(h):
        hello = list(map(int, input().split()))
        graph.append(hello)

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1

    print(result)

