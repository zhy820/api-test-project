
def para(*args, **kwargs):
    """
    A function that accepts any number of positional and keyword arguments.

    Args:
        *args: Variable length positional arguments.
        **kwargs: Variable length keyword arguments.

    """
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

def connect(host, port=161, timeout=5):
   print(f"{host}:{port}, timeout={timeout}")

def add(item, lst=[]):
    lst.append(item)
    print(lst)
    return lst

def add1(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    print(lst)
    return lst


if __name__ == "__main__":
    # para(1, 2, 3, 4, 5, name="Alice", age=30)
    connect("192.168.1.1", port=162, timeout=10)
    add(1)
    add(2)
    add1(1)
    add1(2)

