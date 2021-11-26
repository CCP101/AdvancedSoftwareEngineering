# 设有一m行n列迷宫，O为可到达点，X为不可到达点，F为食物，9为起点，E为终点，有一小虫，想从S走到E。
# 该虫只能上、下、左、右四个方向移动，且不能出界。该虫最多能走k步，当其走到F时，又可以走k步。
# 9起始点 0可走路径 1不可走路径 2中点 8结束点
# 求从S到E的最短“可行”路线. 例如：m=7,n=7,k=20
# 要求打印出 每一步小虫在迷宫中的位置，即在该位置标记小虫走的步数。
maze = [[0, 0, 1, 2, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 3],
        [0, 0, 0, 1, 1, 0, 0]]
maze_count = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]]


def path_que(nums):
    res = []
    res2 = []
    choices_x = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 上下左右四种走法
    n = len(nums)  # 二维迷宫深度

    def find_2(nums):
        for i in range(0, n):
            for j in range(0, n):
                if nums[i][j] == 2:
                    return i, j

    def find_3(nums):
        for i in range(0, n):
            for j in range(0, n):
                if nums[i][j] == 3:
                    return i, j

    def trace(path, choices, x, y, tx, ty, res_path):
        if len(res) >= 20:
            return
        if x == tx and y == ty:
            res_path.append(list(path))
            return

        for choice in choices:
            if x + choice[0] < 0 or x + choice[0] >= n or y + choice[1] < 0 or y + choice[1] >= n:
                continue
            if nums[x + choice[0]][y + choice[1]] == 1:
                continue
            if [x + choice[0], y + choice[1]] in path:
                continue
            path.append([x + choice[0], y + choice[1]])
            maze_count[x + choice[0]][y + choice[1]] += 1
            trace(path, choices, x + choice[0], y + choice[1], tx, ty, res_path)
            path.pop()

    pos2_x, pos2_y = find_2(nums)
    pos3_x, pos3_y = find_3(nums)
    trace([[0, 0]], choices_x, 0, 0, pos2_x, pos2_y, res)
    trace([[pos2_x, pos2_y]], choices_x, pos2_x, pos2_y, pos3_x, pos3_y, res2)
    return res, res2


if __name__ == '__main__':
    result1, result2 = path_que(maze)
    path = []

    min_path1 = 999
    count_path1 = 0
    count_path1_min = 0
    for item in result1:
        if len(item) <= min_path1:
            count_path1_min = count_path1
            min_path1 = len(item)
        count_path1 += 1

    for item in result1[count_path1_min]:
        path += [item]
    count = 0

    min_path2 = 999
    count_path2 = 0
    count_path2_min = 0
    for item in result2:
        if len(item) <= min_path2:
            count_path2_min = count_path2
            min_path2 = len(item)
        count_path2 += 1

    for item2 in result2[count_path2_min]:
        if count != 0:
            path += [item2]
        count += 1

    print("最短步数: " + str(len(path)))
    print("最短路径: " + str(path))
    print("总各点测试走过数： " + str(maze_count))
