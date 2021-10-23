# 给定由n个整数组成的序列(a1, a2, …, an)，最大子段和问题要求该序列形如ai+...+aj的最大值以及对应下标i和j（1≤i≤j≤n）。
# 用分治法求解最大子段和问题，并将序列(-20, 11, -4, -1, 13, -5, -2, 10, -5)的最大子段和值，以及下标i和j输出。

def findMax(dlist, window):
    max = [0, 0]
    length = len(dlist) - (window - 1)
    for i in range(length):
        count = 0
        for j in range(window):
            count += dlist[i + j]
        if count > max[0]:
            max[0] = count
            max[1] = i
    return max


def divide_function(list1, window):
    length = len(list1)
    middle = int(length / 2)
    dlist1 = list1[0:middle]
    dlist2 = list1[middle:length]
    dlist3 = list1[middle - (window - 1):middle + (window + 1)]
    max_list1 = findMax(dlist1, window)
    max_list2 = findMax(dlist2, window)
    max_middle = findMax(dlist3, window)
    max_middle[1] += middle - (window - 1)
    if max_list1[0] > max_list2[0]:
        max_list = max_list1
    else:
        max_list = max_list2
    if max_middle[0] > max_list[0]:
        max_list = max_middle
    return max_list


if __name__ == '__main__':
    list_divide = [-20, 11, -4, -1, 13, -5, -2, 10, -5]
    window_size = 5
    max = divide_function(list_divide, window_size)
    print("最大值=" + str(max[0]) + "  i=" + str(max[1]) + "  j=" + (str(max[1] + window_size - 1)))
