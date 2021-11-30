import math

list_a = [0] * 20


def PrimeTest(x):
    n = int(math.sqrt(x))
    i = 2
    while i <= n:
        if x % i == 0:
            return 0
        i = i + 1
    return 1


def check(k):
    flag = 0
    for i in range(k):
        if list_a[i] == list_a[k]:
            return 0
    if flag == 1 & k == 19:
        flag = PrimeTest(list_a[k] + list_a[0])
    else:
        flag = PrimeTest(list_a[k] + list_a[k - 1])
    return flag


def PrimeCircle(n):
    list_a[0] = 1
    k = 1
    while k >= 1:
        print(list_a)
        list_a[k] = list_a[k] + 1
        while list_a[k] <= n:
            if check(k) == 1:
                break
            else:
                list_a[k] = list_a[k] + 1
        if list_a[k] <= n and k == n - 1:
            return
        if list_a[k] <= n and k < n - 1:
            k = k + 1
        else:
            list_a[k] = 0
            k = k - 1


if __name__ == '__main__':
    PrimeCircle(20)
    print(list_a)
