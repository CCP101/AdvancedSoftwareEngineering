# 设有n个长度不等的有序表，各表中元素按降序排列，要求通过两两合并的方法将n个有序表最终合并成一个降序表，
# 并要求在最坏情况下比较的总次数达到最少。将[30,28,26,23,20,17,14,10],[28,27,25,23,22,16,15],
# [16,14,12,10,8]以及[14,11,7],最终合并成一个降序表，并打印输出。

def sortList(sum):
    while len(sum) > 1:
        l1 = sum[0]
        l2 = sum[1]
        sum.remove(l1)
        sum.remove(l2)
        for i in l2:
            l1.append(i)
        l1 = sorted(l1, reverse=True)
        sum.append(l1)
    print(sum[0])


if __name__ == '__main__':
    list_sum = []
    list_1 = [30, 28, 26, 23, 20, 17, 14, 10]
    list_sum.append(list_1)
    list_2 = [28, 27, 25, 23, 22, 16, 15]
    list_sum.append(list_2)
    list_3 = [16, 14, 12, 10, 8]
    list_sum.append(list_3)
    list_4 = [14, 11, 7]
    list_sum.append(list_4)
    sortList(list_sum)
