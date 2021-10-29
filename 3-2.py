# 回文是正序和逆序相同的非空字符串。利用动态规划求给定输入字符串的最长回文子序列。
# 例如，给定输入acivicb,算法应该返回civic。对给定输入character,输出其最长回文子序列的长度以及对应子序列。

def longestHW(str_hw):
    str_length = len(str_hw)
    if str_length < 2:
        return str_hw

    dp = [[False] * str_length for _ in range(str_length)]
    for i in range(str_length):
        dp[i][i] = True

    max_len = 1
    begin = 0
    for l in range(2, str_length + 1):
        for i in range(str_length):
            j = l + i - 1
            if j >= str_length:
                break
            if str_hw[i] == str_hw[j]:
                if j - i < 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = False
            if dp[i][j] and j - i + 1 > max_len:
                max_len = j - i + 1
                begin = i
    return str_hw[begin:begin + max_len]


if __name__ == '__main__':
    input_str = "acivicb"
    get_str = longestHW(input_str)
    print("最长回文子序列的长度:" + str(len(get_str)))
    print("最长回文子序列为:" + str(get_str))
