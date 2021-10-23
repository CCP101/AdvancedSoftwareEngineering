# 插入法调整堆。已知（k1,k2,...,kn)是堆，设计算法将（k1,k2,...,kn，kn+1)调整为堆（假设调整为大根堆）。
# 对（47,35,26,20,18，7,13,10），插入37，将其调整为大根堆，并打印输出。

def construct_heap(heap, num):
    heap.append(num)
    flag = 0
    length = len(heap)
    interrupt = int(length/2)
    while flag == 0:
        flag = 1
        for i in range(length):
            if i <= interrupt-1:
                if heap[i] < heap[(i+1)*2-1]:
                    heap[i], heap[(i+1)*2-1] = heap[(i+1)*2-1], heap[i]
                    flag = 0
                elif heap[i] < heap[(i+1)*2]:
                    heap[i], heap[(i+1)*2] = heap[(i+1)*2], heap[i]
                    flag = 0
    return heap


if __name__ == '__main__':
    list_heap = [47, 35, 26, 20, 18, 7, 13, 10]
    insert_num = 37
    heap = construct_heap(list_heap,insert_num)
    print(heap)
