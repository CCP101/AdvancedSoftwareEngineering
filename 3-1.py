# 利用动态规划，求一个n个数的序列的最长单调递增子序列。对（6, 4, 8, 2, 17, 9, 5）输出最长单调递增子序列的长度以及对应子序列。


def findMax(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


def findList(dp, nums):
    max_length = max(dp)
    lis_list = []
    for i in range(max_length):
        lis_list.append(dp.index(i+1))
    for i in range(len(lis_list)):
        lis_list[i] = nums[lis_list[i]]
    return lis_list


if __name__ == '__main__':
    input_list = [6, 4, 8, 2, 17, 9, 5]
    get_dp = findMax(input_list)
    get_list = findList(get_dp, input_list)
    print("最长单调递增子序列的长度:" + str(len(get_list)))
    print("最长单调递增子序列为:" + str(get_list))
