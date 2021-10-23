# 修改折半查找算法使之能够进行范围查找。所谓范围查找是要找出在给定值a和b之间的所有元素（a≤b)。对(7,14,18,21,23,29,31,35,38)，找出在15和30之间的所有元素，并打印输出。
def deep_search(list_s, length, num, flag):
    low = 0
    high = length - 1
    index = 0
    while low <= high:
        middle = int((low + high) / 2)
        if low == middle:
            if flag == 0:
                index = low
                break
            if flag == 1:
                index = low
                break
        if high == middle:
            if flag == 1:
                if list_s[high] == num:
                    index = high + 1
                    break
                else:
                    index = high
                    break
        if list_s[middle] > num:
            high = middle - 1
        elif list_s[middle] < num:
            low = middle + 1
    return index


def search(list_s, begin, end):
    length = len(list_s)
    if length <= 2 or begin > end:
        print("列表或范围不规范")
        return -1
    begin_index = deep_search(list_s, length, begin, 0)
    end_index = deep_search(list_s, length, end, 1)
    return begin_index, end_index


if __name__ == '__main__':
    list_search = [7, 14, 18, 21, 23, 29, 31, 35, 38]
    begin_search = 16
    end_search = 37
    begin, end = search(list_search, begin_search, end_search)
    new_list = list_search[begin:end]
    print(begin, end)
    print(new_list)
