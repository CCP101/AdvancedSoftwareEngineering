# 用动态规划法求如下最优二叉查找树问题的最优解：集合{10,15,20,25,30,35,40,45,50,55}的查找概率是
# {0.1,0.05,0.15,0.1,0.05,0.15,0.05,0.05,0.2,0.1}。要求打印输出最少平均比较次数，以及最优二叉查找树的先序遍历结果。

n = 10
l = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
p = [-1, 0.1, 0.05, 0.15, 0.1, 0.05, 0.15, 0.05, 0.05, 0.2, 0.1]
root = [[0 for i in range(n + 2)] for j in range(n + 2)]
w = [[0 for i in range(n + 2)] for j in range(n + 2)]
e = [[0 for i in range(n + 2)] for j in range(n + 2)]


def optimalBST(p, n):
    for i in range(1, n + 2):
        w[i][i - 1] = 0
        e[i][i - 1] = 0

    for len in range(1, n + 1):
        for i in range(1, n - len + 2):
            j = i + len - 1
            e[i][j] = 9999
            w[i][j] = w[i][j - 1] + p[j]
            for k in range(i, j + 1):
                temp = e[i][k - 1] + e[k + 1][j] + w[i][j]
                if temp < e[i][j]:
                    e[i][j] = temp
                    root[i][j] = k


def printOptimalBST(i, j, r):
    rootChild = root[i][j]  # 子树根节点
    if rootChild == root[1][n]:
        print("%d" % l[rootChild - 1], end=' ')
        printOptimalBST(i, rootChild - 1, rootChild)
        printOptimalBST(rootChild + 1, j, rootChild)
        return
    if j < i - 1:
        return
    elif j == i - 1:
        return
    else:
        print("%d" % l[rootChild - 1], end=' ')

    printOptimalBST(i, rootChild - 1, rootChild)
    printOptimalBST(rootChild + 1, j, rootChild)


if __name__ == '__main__':
    optimalBST(p, n)
    printOptimalBST(1, n, -1)
    print()
    print("平均比较次数 %f" % e[1][n])
