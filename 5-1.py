# 把一个真分数表示成最少的埃及分数之和。埃及分数即分子为1的分数。
# 例如7/8=1/2+1/3+1/24。将77/108表示成最少的埃及分数之和，并打印输出。
if __name__ == '__main__':
    str_math = input()
    a, b = str_math.split('/')
    a = int(a)
    b = int(b)
    list_num = []
    while b % a != 0:
        q, r = b//a, b%a
        a -= r
        b *= (q+1)
        list_num.append(q+1)
    list_num.append(int(b/a))
    print(list_num)
