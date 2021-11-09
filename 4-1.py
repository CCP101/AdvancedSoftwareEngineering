# 用动态规划法求如下0/1背包问题的最优解：有5个物品，其重量分别为（3,2,1,4,5），价值分别为（25,20,15,40,50），
# 背包容量为6。要求打印输出最优解对应的装入背包的物品，以及物品的价值。

def backpack(num, wei, w, v):
    result = [[0 for i in range(wei + 1)] for i in range(num + 1)]
    for i in range(1, num + 1):
        for j in range(1, wei + 1):
            if j < w[i - 1]:
                result[i][j] = result[i - 1][j]
            else:
                result[i][j] = max(result[i - 1][j], result[i - 1][j - w[i - 1]] + v[i - 1])
    return result


if __name__ == '__main__':
    number = 5
    weight = 6
    weights = [3, 2, 1, 4, 5]
    values = [25, 20, 15, 40, 50]
    result = backpack(number, weight, weights, values)
    print("最优解为：" + str(result[number][weight]))
    print("所选取的物品为：")
    item = [0 for i in range(number + 1)]
    j = weight
    for i in range(number, 0, -1):
        if result[i][j] > result[i - 1][j]:
            item[i - 1] = 1
            j -= weights[i - 1]
    for i in range(number):
        if item[i] == 1:
            print("第" + str(i + 1) + "件")
