# Uses python3

'''
With Repetitions allowed
def optimal_weight(W, w):
    value = [0] * W
    for i in range(1, W):
       for j in w:
            if j <= i:
                val = value[i-j]+j
                if val > value[i]:
                    value[i]=val
    print(value)
    return value[W-1]
'''
def optimal_weight(W,w):
    m = len(w)

    value = [[0]*(m+1) for i in range(W+1)]

    for i in range(1,m+1):
        for j in range(1,W+1):
            value[j][i] = value[j][i-1]
            if w[i-1] <= j:
                val = value[j-w[i-1]][i-1]+w[i-1]
                if value[j][i] < val:
                    value[j][i] = val
    #print(value)
    return value[W][m]





W,n = map(int,input().split())
w = list(map(int,input().split()))
print(optimal_weight(W,w))
