# Uses python3
import sys
from collections import Counter
def get_majority_element(a,n):
    flag = False
    count  = Counter(a).values()
    for i in count:
        if i > n//2:
            flag = True

    return flag




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a,n):
        print(1)
    else:
        print(0)

'''
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_elem = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    right_elem = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    lcount = 0
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1
'''
