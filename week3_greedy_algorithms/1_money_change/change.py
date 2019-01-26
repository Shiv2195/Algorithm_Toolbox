# Uses python3
import sys

def get_change(m):
    #write your code here
    change = 0
    if m < 10 and m < 5:
        return (m)
    elif m < 10 and m > 5:
        mid = m%5
        return (1+mid)
    else:
        ten_coin = m//10
        mid = m%10
        if mid < 5:
            return (ten_coin+mid)
        else:
            return (ten_coin+mid-4)





if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
