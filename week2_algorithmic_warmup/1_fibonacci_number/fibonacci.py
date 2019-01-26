# Uses python3
def fibonacci_series(n):
    fibo_list = []
    fibo_list.append(0)
    fibo_list.append(1)
    for i in range(2,n+1):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return fibo_list[n]
n = int(input())
print(fibonacci_series(n))
