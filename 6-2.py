# 给定一个正整数集合X={x1,x2,...,xn}和一个正整数y，设计回溯算法，求集合X的一个子集Y，使得Y中元素之和等于y。
# 要求使用迭代算法，不得使用递归算法。 设X={4,3,5,7,6}，y=20。4 3 7 6


def cal(x, y):
    return x[0] * y[0] + x[1] * y[1] + x[2] * y[2] + x[3] * y[3] + x[4] * y[4]


if __name__ == '__main__':
    inputList = [4, 3, 5, 7, 6]
    target = 20
    x = [0 for i in range(5)]
    flag = 1

    for a in range(2):
        x[0] = a
        if flag == 1:
            for b in range(2):
                x[1] = b
                if flag == 1:
                    for c in range(2):
                        x[2] = c
                        num = cal(x, inputList)
                        if num > 20:
                            break
                        for d in range(2):
                            x[3] = d
                            num = cal(x, inputList)
                            if num > 20:
                                break
                            for e in range(2):
                                x[4] = e
                                num = cal(x, inputList)
                                if num == 20:
                                    bestWay = x
                                    flag = 0
                                    str_a = "20="
                                    count = 0
                                    for i in bestWay:
                                        if i == 1:
                                            str_a += str(inputList[count])
                                            str_a += "+"
                                        count += 1
                                    print(str_a[:-1])