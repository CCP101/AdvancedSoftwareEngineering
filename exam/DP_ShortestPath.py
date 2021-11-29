matrix = [[4, 2, 3, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 9, 8, 0, 0, 0, 0],
          [0, 0, 0, 6, 7, 8, 0, 0, 0],
          [0, 0, 0, 0, 4, 7, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 5, 6, 0],
          [0, 0, 0, 0, 0, 0, 8, 6, 0],
          [0, 0, 0, 0, 0, 0, 6, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 3],
          [0, 0, 0, 0, 0, 0, 0, 0, 3]]

if __name__ == '__main__':
    dp_path = [[10, ""]] * 9
    for i in range(9):
        max_dp = 99
        for j in range(9):
            if matrix[j][i] != 0:
                if j == 0:
                    dp_path[i] = [matrix[j][i], str(j) + "-" + str(i+1)]
                if j != 0:
                    dp_new = matrix[j][i] + dp_path[j-1][0]
                    if dp_new < max_dp:
                        max_dp = dp_new
                        dp_path[i] = [dp_new, dp_path[j-1][1] + str(j) + "-" + str(i+1)]

    print(dp_path)
    print("最短长度：" + str(dp_path[8][0]))
    print("最短路径：" + str(dp_path[8][1]))
