# Uses python3
def lcs2(a, b):
    m = len(a)
    n = len(b)
    L = [[0]*(n+1) for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]


m = int(input())
a = list(map(int, input().split()))
n = int(input())
b = list(map(int, input().split()))
print(lcs2(a, b))

