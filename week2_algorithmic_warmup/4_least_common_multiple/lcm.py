# Uses python3
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b // gcd(a, b)

x,y = input().split()
x = int(x)
y = int(y)
print(lcm(x,y))
