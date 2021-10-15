# 利用欧几里得算法，将一个给定的真分数化简为最简分数形式。例如，将12/16化简，并生成运行结果

def gcd(n1, n2):
    while n1 != 0:
        n1, n2 = n2 % n1, n1
    return n2


if __name__ == '__main__':
    fraction = input()
    fraction = fraction.split('/')
    num1 = int(fraction[0])
    num2 = int(fraction[1])
    result = gcd(num1, num2)
    new_num1 = int(num1/result)
    new_num2 = int(num2/result)
    print_str = str(new_num1)+"/"+str(new_num2)
    print(print_str)
