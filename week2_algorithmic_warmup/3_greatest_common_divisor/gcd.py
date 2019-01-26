# Uses python3

def GCD(x,y):

    if y==0:
        return x
    else:
        return GCD(y,x%y)


x,y  = input().split()
x = int(x)
y = int(y)
print(GCD(x,y))
