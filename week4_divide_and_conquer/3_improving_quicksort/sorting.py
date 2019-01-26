# Uses python3
import sys
import random



def randomized_quick_sort(a):
    if len(a) < 2:
        return a
    else:
        pivotal=a[0]
        less=[i for i in a if i < pivotal]
        equal=[i for i in a if i == pivotal]
        greater=[i for i in a if i > pivotal]
        return randomized_quick_sort(less)+equal+randomized_quick_sort(greater)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = randomized_quick_sort(a)
    for x in b:
        print(x, end=' ')
