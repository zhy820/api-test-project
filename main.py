# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from collections import Counter


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

# test enumerate() function
def enumerate_test():
    a = ['a', 'b', 'c', 'd']
    for index, value in enumerate(a,start=2):
        print(index, value)


''''
class Example:
    def __init__(self):
        self.x = 10  # 实例变量

    @staticmethod
    def print_x():
        print(self.x)  # 会报错，因为 self 未定义

'''
def counter():
    lst = [6, 8, 9, 5, 6.7, 7, 2, 7, 3, 5, 8, 1, 9, 7, 7]
    counter = Counter(lst)

    # 找到出现次数最多的数字及对应次数

    print(counter)
    print(type(counter))
    print(counter.most_common(5))
    most_common_num, max_count = counter.most_common(1)[0]
    linux = counter.most_common(1)

    print(f"看看结构", linux)
    print(f"出现次数最多的数字是：{most_common_num}，出现了 {max_count} 次")

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    #a = [0,1,2,3,4,5,6,7,8,9]
    #enumerate_test()
    #funA()
    #ex = Example()
    #ex.print_x()
    #counter()
    #a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #print(a[:6:-1])
    fruits = ['apple', 'banana', 'cherry']
    for index, value in enumerate(fruits):
        print(f"{index}: {value}")  # 输出:# 0: apple# 1: banana# 2: cherry


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
