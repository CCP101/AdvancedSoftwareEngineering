#  判断一个大整数能否被11整除 设计算法,判断一个大整数能否被11整除。可以通过以下方法:将该数的十进制表示从右端开始,每两位一组构成一个整数,
#  然后将这些数相加,判断其和能否被11整除。例如,将562843748分割成5,62,84,37和48,然后判断(5+62+84+37+48)能否被11整除。

def num_divide(num):
    list_divide = []
    while num % 100 != 0 & num >= 0:
        new_num = int(num % 100)
        list_divide.append(new_num)
        num = int(num / 100)
    return list_divide


if __name__ == '__main__':
    input_num = int(input())
    cal_list = num_divide(input_num)
    new_num = sum(cal_list)
    if new_num / 11 == 0:
        print(str(input_num) + "能被11整除")
    else:
        print(str(input_num) + "不能被11整除")
