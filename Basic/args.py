def print_info(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
    print("-" * 20)

def add_port(port, ports = []):
    ports.append(port)
    print("ports:", ports)
    return ports

def add_port1(port, ports = None):
    if ports is None:
        ports = []

    ports.append(port)
    print("ports:", ports)
    return ports

def lambda_test():
    nes = [
        {"name": "NE1", "ports": 8},
        {"name": "NE2", "ports": 2},
        {"name": "NE3", "ports": 4},
    ]
    sorted_nes = sorted(nes, key = lambda ne: ne["ports"], reverse = True)
    print(sorted_nes)

    #get port
    ports = list(map(lambda ne: ne["ports"], nes))
    print("port", ports)

    port1 = [ne["ports"] for ne in nes]
    print("ports1", port1)

def outer_counter():
    counter = 0

    def inner_test():
        nonlocal counter
        counter += 1
        print("counter:", counter)

    return inner_test
    pass





if __name__ == "__main__":
    # print_info(1, 2, 3)
    # lst = [4, 5, 6]
    # print("list args",*lst)
    #
    # set = {7, 8, 9}
    # print("set args",*set)
    #
    # print_info(name = "admin", port = 161)
    # print_info(1,2, name = "admin", port = 161)
    #
    # print("第一次", add_port(port = 88))
    # print("第二次", add_port(port = 89))
    # print("第三次", add_port(port = 90))
    #
    # print("第一次", add_port1(port=88))
    # print("第二次", add_port1(port=89))
    # print("第三次", add_port1(port=90))

    # lambda_test()
    # 测试
    c = outer_counter()
    print(c())  # 输出 1
    print(c())  # 输出 2
    print(c())  # 输出 3