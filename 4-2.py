# 用动态规划法求两个字符串A="xzyzzyx"和B="zxyyzxz"的最长公共子序列。
# 要求打印输出最长公共子序列以及公共子序列的长度。
def longestCommonSubsequence(text1, text2):
    text1 = ' ' + text1
    text2 = ' ' + text2
    N, M = len(text1), len(text2)
    dp = [[0] * M for _ in range(N)]

    for i in range(1, N):
        for j in range(1, M):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = N - 1
    j = M - 1
    list_dp = [0 for i in range(N - 1)]
    while i > 0:
        if dp[i][j] > dp[i - 1][j]:
            list_dp[i] = 1
            j = j - 1
        i -= 1
    i = 0
    listp = []
    for x in list_dp:
        if x == 1:
            listp.append(text2[i + 1])
        i += 1
    return dp[-1][-1], listp


if __name__ == '__main__':
    list_A = "xzyzzyx"
    list_B = "zxyyzxz"
    length, listdp = longestCommonSubsequence(list_A, list_B)
    print("长度为" + str(length))
    print("字符串为" + str(listdp))

