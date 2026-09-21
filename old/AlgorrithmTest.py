
def slice_test():
    '''
    slice frame:
    1. a[start:stop:step]
    2. start: 起始索引，默认为0
    3. stop: 结束索引（不包含），默认为列表长度
    4. step: 步长，默认为1
    5. 负数步长表示反向切片
    '''
    a = [0,1,2,3,4,5,6,7,8,9]
    #[9, 8, 7]
    print(a[:4:-3])

#enumerate()
def enumerate_test():
    a = ['a', 'b', 'c', 'd']
    for index, value in enumerate(a,start=2):
        print(index, value)
        print(f"index: {index}, value: {value}")
        print("index is %d, value is %s" % (index, value))
        reversed = "index is {}, value is {}".format(index, value)
        result = "====".join(a)
    print(f"reverserd is {reversed}")
    print(f"join() is {result}")


def copy_test():
    #shallow copy: modify the shallow copy will affect the original list, but modify the original list will not affect the shallow copy
    shallow = [0,1,2,3,[4,5]]
    b = shallow.copy()
    b.append(6)
    print(f"original is {shallow}")

    shallow.append(7)
    print(f'original list is {shallow}')
    print(f'shallow copy is {b}')

    shallow.extend([8,9])
    print(f"shallow list is {shallow}")

    b.pop()
    print(f"shallow list is {shallow}")
    print(f"shallow copy is {b}")

def fabonacci(n):
    #fabonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabonacci(n-1) + fabonacci(n-2)

def fabonacci_iterative(n):
    '''
    list1 = []
    if n <= 0:
        list1.append(0)
    elif n == 1:
        list1.append(1)
    elif n == 2:
        list1.extend([1.1])
    else:
        a, b = 1, 1
        list1.extend([1, 1])
        for _ in range(2, n + 1):
            a, b = b, a + b
            list1.extend([b])
    return list1
    '''
    #the another way to do it is to use a list to store the fabonacci sequence
    sequence = [0, 1]
    for i in range(2, n + 1):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)
    return sequence[:n + 1]

if __name__ == '__main__':
    #enumerate_test()
    #slice_test()
    #copy_test()
    #this is not suitable my need
    fab = fabonacci(10)
    print(f"the 10th fabonacci number is {fab}")
    fab = fabonacci_iterative(10)
    print(f"the iterative fabonacci list is {fab}")

