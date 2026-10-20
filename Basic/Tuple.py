import copy

# Tuple vs List
def tuple_vs_list():

    a = (1, 2, 3)
    b = [1, 2, 3, 3, 5]
    #a.append(4)  # This will raise an AttributeError since tuples are immutable
    b.append(5)

    print('tuple',a)  # Output: (1, 2, 3)
    print('list',b)  # Output: [1, 2, 3, 5]
    setb = set(b)
    print('set',setb)  # Output: {1, 2, 3, 5}

#dict vs set
def dict_vs_list():
    b = [1, 2, 3, 3, 5]
    c = {'in1': 'a', 'in2': 'b', 'in3': 'c'}
    d = {1, 2, 3}

    #print key and value
    for k in c:
        print("key", k)  # Output: in1, in2, in3
    for v in c.values():
        print("value", v)  # Output: a, b, c
    for k, v in c.items():
        print("key and value", k, v)  # Output: in1 a, in2 b, in3 c


    #index and value
    print("index and value", list(enumerate(b)))  # Output: [(0, 1), (1, 2), (2, 3), (3, 5), (4, 5)]
    print('dict[in1]',c['in1'])  # Output: {1: 'a', 2: 'b', 3: 'c'})


# copy vs deepcopy
def copy_vs_deepcopy():
    original_list = [1, 2, [3, 4]]
    shallow_copy = copy.copy(original_list)
    deep_copy = copy.deepcopy(original_list)

    #original_list external change
    original_list.append(5)
    print("original_list external changed",original_list)
    print("shallow_copy", shallow_copy)  # Output: [1, 2, [3, 4]]
    print("deep_copy", deep_copy)  # Output: [1, 2, [3, 4]]

    #original_list external change
    # original_list[2].append(8)
    print("original_list inner changed",original_list)
    print("shallow_copy", shallow_copy)  # Output: [1, 2, [3, 4]]
    print("deep_copy", deep_copy)  # Output: [1, 2, [3, 4]]

    #shallow copy internal change
    shallow_copy[2].append(6)
    print("change inner shallow_copy", shallow_copy)
    print("Original_list", original_list)

    #deep copy external change
    deep_copy.append(7)
    print("deep_copy changed", deep_copy)
    print("original_list", original_list)

    #deep copy inner change
    deep_copy[2].append(7)
    print("deep_copy inner changed", deep_copy)
    print("original_list", original_list)

def tuple_operate():
    t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #不包含t[6]，所以输出[9, 8]
    print(t[6:-1])  # Output: [9， 8]
    print(t[:6])  # Output: [1, 2, 3, 4, 5, 6] #不包含t[6]，所以输出[1, 2, 3, 4, 5, 6]
    print(t[:6:-2]) # Output: [9] #不包含t[6]，所以输出[9, 7]

def enumerate_operate():
    str = 'history'
    lst = ['act', 'buy', 'cut', 'duck']
    tuple1 = ('e','r','t','y','utils')

    for index, value in enumerate(str, start=5):
        print(index, value)  # Output: 0 a, 1 b, 2 c, 3 d

    for index, value in enumerate(lst, start=5):
        print(index, value)  # Output: 0 a, 1 b, 2 c, 3 d

    for index, value in enumerate(tuple1, start=5):
        print(index, value)  # Output: 0 a, 1 b, 2 c, 3 d

#Use Python to generate Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    lst = []
    for _ in range(n):
        #yield a
        a, b = b, a + b
        lst.append(a)
    return lst


if __name__ == '__main__':
#     copy_vs_deepcopy()
    tuple_operate()
    #enumerate_operate()
    # p = fibonacci(10)


