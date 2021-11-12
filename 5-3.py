# 在递减有序序列（r1,r2,...,rn）中，存在序号i(1<=i<=n),使得ri=i。设计一个分治算法找出这个元素，
# 要求算法在最坏情况下的时间性能为O(log2n)。对（30,25,15,9,8,6,5,4,3,2,1）找出ri=i，并打印输出。
import sys


def findRi(point, index):
    length = len(point)
    middle = int(length/2)
    point_left = point[0:middle]
    point_right = point[middle:]
    if point_left[0] == index:
        result = point_left[0]
        print("R"+str(result)+"=="+str(result))
        sys.exit(0)
    if point_left[-1] > middle + index:
        if len(point_right) > 1:
            findRi(point_right, middle + 1 + index)
    else:
        if len(point_left) > 1:
            findRi(point_left, index)


if __name__ == '__main__':
    list_point = [30, 25, 15, 9, 8, 6, 5, 4, 3, 2, 1]
    findRi(list_point, 0)
