def lst_operations():
    lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]

    #add
    lst.append(10)  # Add an element to the end of the
    print(lst)

    lst.insert(1,11)
    print(lst)

    lst.extend([12,13,14,15])
    print(lst)

    #delete
    lst.pop()    #弹出位置
    print(lst)

    lst.pop(5)   #弹出指定末尾
    print(lst)

    del lst[0]   #删除指定位置
    print(lst)

    #modify
    lst[0] = 88  #直接赋值
    print(lst)

    #Get
    lst.index(4)  #找到4的位置
    print(lst.index(4))

     #统计1的个数
    print(lst.count(1) )

    #排序
    lst.sort()  #升序
    print(lst)

    lst.sort(reverse=True)  #降序
    print(lst)

    sorted(lst)   #返回排序后的新列表
    print("sorted", sorted(lst) )

    lst.reverse()
    print("reversed", lst)

    #其他
    print('len', len(lst))

    lst.copy()
    print(lst)

    lst.clear()  # 清空
    print(lst)

def cut():
    lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(lst[2:5])  #切片:[4, 1,5]
    print(lst[:5])   #切片 [3, 1, 4, 1,5]
    print(lst[2:])   #切片 [4, 1, 5, 9, 2, 6, 5]
    print(lst[-3:])  #切片 从倒数第三个开始到末尾  [2, 6, 5]
    print(lst[::2])  #切片 从头到位，步长为2 [3, 4, 5, 2, 5]
    print(lst[::-1]) #切片 从尾到头，步长为1 [5,6,2,9,5,1,4,1,3]

def tuple():
    t = (3, 1, 4, 1, 5, 9, 2, 6, 5)
    print('find 4 ', t.index(4))

    print('count 1', t.count(1))

    print("len", len(t))



if __name__ == "__main__":
    # lst_operations())
    # cut()
    tuple()
