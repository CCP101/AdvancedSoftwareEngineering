# 1.回溯法求解0-1背包问题：有n件物品和一个容量为c的背包。第i件物品的价值是v[i],重量是w[i]。求解将哪些物品装入背包可使价值总和最大。
# 要求使用迭代算法，不得使用递归算法。
# 设有三个物品，其重量分别为：16,15,15；价值分别为：45，25，25；请选择物品，使其重量不超过30，但价值最大。


if __name__ == '__main__':
    n = 3
    c = 30
    w = [16, 15, 15]
    v = [45, 25, 25]
    x = [0 for i in range(n)]
    bestValue = 0
    maxWeight = 30
    currentWeight = 0
    currentValue = 0
    bestWay = None
    for i in range(len(x)):
        x[i] = 1
        z = i + 1
        flag = 0
        currentValue = x[0]*v[0]+x[1]*v[1]+x[2]*v[2]
        if currentValue >= bestValue:
            bestValue = currentValue
            bestWay = x
        for z in range(len(x)-1-i):
            y = z
            x[y+1] = 1
            flag = 0
            currentWeight = x[0]*w[0]+x[1]*w[1]+x[2]*w[2]
            if currentWeight >= 30:
                flag = 1
            else:
                currentValue = x[0]*v[0]+x[1]*v[1]+x[2]*v[2]
                if currentValue >= bestValue:
                    bestValue = currentValue
                    bestWay = x
            if flag == 1:
                x[y+1] = 0
        if flag == 1:
            x[i] = 0
    str_result = ""
    for s in range(len(bestWay)):
        if bestWay[s] == 1:
            x = s
            str_result += ("第"+str(x+1)+"件 ")
    print("价值最大为：" + str(bestValue))
    print("拿去方法为：" + str_result)
