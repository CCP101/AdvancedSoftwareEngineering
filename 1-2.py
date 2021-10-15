#  设计算法，判定一个以邻接表表示的连通图是否具有欧拉回路。自己画一个包含至少10个顶点的连通图，提交连通图以及运行结果。
list_graph = [(1, 2), (1, 5), (1, 7), (1, 9), (2, 4), (2, 8), (2, 10), (3, 4), (3, 6), (4, 7),
              (4, 10), (5, 10), (6, 10), (7, 9), (8, 10), (9, 4), (9, 8), (9, 1)]
list_point = []

if __name__ == '__main__':
    for i in list_graph:
        if i[0] not in list_point:
            list_point.append(i[0])
        if i[1] not in list_point:
            list_point.append(i[1])
    list_point.sort()
    list_edge = [[0 for i in range(len(list_point))] for j in range(len(list_point))]
    for i in list_graph:
        i0 = i[0] - 1
        i1 = i[1] - 1
        list_edge[i0][i1] = 1
        list_edge[i1][i0] = 1
    Flag = 0
    for i in list_edge:
        count = 0
        for j in i:
            if Flag == 0:
                if j == 1:
                    count += 1
        if count % 2 != 0:
            Flag = 1
            break
    if Flag == 0:
        print("是邻接矩阵")
    else:
        print("不是邻接矩阵")
