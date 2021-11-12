# 设计分治算法求解一维空间上n个点的最近对问题。
# 对{1,3,5,6,8,10,12}求解最近对距离以及对应的两个点，并打印输出。

def get_md(rec):
    min_distance = 99999
    min_ab = ""
    for i in rec:
        list_t = i
        length = len(list_t)
        for i in range(length):
            for j in range(i + 1, length):
                temp_dis = list_t[j] - list_t[i]
                if temp_dis < min_distance:
                    min_distance = temp_dis
                    min_ab = str(list_t[i]) + "--" + str(list_t[j])
    print("最近对距离为:" + str(min_distance))
    print("对应的两个点为：" + min_ab)


def rec(point):
    list_rec = []
    list_f = point[0:int((len(point) - 1) / 2)]
    list_rec.append(list_f)
    list_b = point[int((len(point) - 1) / 2):]
    list_rec.append(list_b)
    list_m = point[int((len(point) - 1) / 2) - 1:int((len(point) - 1) / 2) + 1]
    list_rec.append(list_m)
    get_md(list_rec)


if __name__ == '__main__':
    list_point = [1, 3, 5, 6, 8, 10, 12]
    rec(list_point)
