def findRi(point, index):
    flag = 0
    length = len(point)
    middle = int(length/2)
    point_left = point[0:middle]
    point_right = point[middle:]
    if point_left[0] == index:
        result = point_left[0]
        print("R"+str(result)+"=="+str(result))
        flag = 1
        exit(0)
    if point_left[-1] > middle + index:
        if len(point_right) > 1 and flag == 0:
            findRi(point_right, middle + 1 + index)
    else:
        if len(point_left) > 1 and flag == 0:
            findRi(point_left, index)


if __name__ == '__main__':
    list_point = [30, 25, 15, 9, 8, 6, 5, 4, 3, 2, 1]
    findRi(list_point, 0)
