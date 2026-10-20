from openpyxl.styles.builtins import total


def dict():
    d = {'a': 1, 'b': 2, 'c': 3}

    #Get values
    print(d["a"])  # Output: 1
    print(d.get("b")) # Output: 2
    print(d.get("d", "Not Found"))  # Output: Not Found

    #Get values
    print(d['a'])
    print('keys', d.keys())
    print('values', d.values())
    print('items', d.items())

    #Add or update values
    d['d'] = 4  # Add new key-value pair
    d['a'] = 10  # Update existing key-value pair
    d.update({'e': 5, 'f': 6})   # Add multiple key-value pairs
    d.setdefault('g', 7) # Add key-value pair if key does not exist
    print(d)  # Output: {'a': 10, 'b': 2

    #del
    print(d.pop('a'))
    print(d.pop("z", "Not Found"))  # Output: Not Found
    del d['b']  # Remove key-value pair by key
    print(d)

    d.clear()
    print(d)

def dict_for():
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key, d[key])  # Output: a 1, b 2, c 3

    for key, value in d.items():
        print(key, value)  # Output: a 1, b 2, c 3

    for i, (key, value) in enumerate(d.items()):
        print(i, key, value)  # Output: 0 a 1, 1 b 2, 2 c 3

def dict_list():
    port = [1,2,3,4]

    port.append(5)
    up_ports = [p for p in port if p % 2 == 0]
    print(up_ports)

def tuple():
    ne = ('NE1', '192.168.2.1', 161)

    name, ip, port = ne

    print(name, ip, port)

def dict_config():
    config = {
        'host': '192.168.2.45',
        'port': 161,
        'timeout': 5
    }

    timeout = config.get('complex', 10)  # Default to 10 if not found
    print(timeout)

def dict_config_update():
    nes = [
        {"name":"NE1", "ip": "192.168.2.54", "port": 12, "status": "online"},
        {"name":"NE2", "ip": "192.168.2.55", "port": 8, "status": "offline"},
        {"name":"NE3", "ip": "192.168.2.56", "port": 9, "status": "online"},
        {"name":"NE4", "ip": "192.168.2.57", "port": 10, "status": "offline"},
    ]

    online = [ne for ne in nes if ne['status'] == 'online']
    print("online NE", online)

    total_ports = sum(ne['port'] for ne in nes)
    print("total ports", total_ports)

    ports = [port for port in nes]
    print("ports", ports)

    sorted_port = sorted(nes, key=lambda n: n['port'])
    print("sorted port", sorted_port)

    #get port
    ports = [ne['port'] for ne in nes]
    print("ports", ports)

    sorted_nes = sorted(nes, key=lambda x:x['ip'])
    print("按IP排序", sorted_nes)
    for ne in sorted_nes:
        print(f" {ne['name']} - {ne['ip']}")

    ne_tuple = ("NE1", "192.168.1.1")

    name, ip = ne_tuple
    print(f"Name: {name}, IP: {ip}")
    print(f"解包：{name}, {ip}")

    config = {
        'timeout': 5,
        'retries': 3,
        'community': 'public'
    }
    print('timeout:', config.get('timeout'), 10)  # Output: 5
    print('unknown keys', config.get('unknown', '默认值'))

    sorted_by_ports = sorted(nes, key=lambda x: x['port'], reverse=True)
    print("sorted by_ports")
    for ne in sorted_by_ports:
        print(f" {ne['name']} - {ne['ip']}")


    # 8. total online/offline num
    from collections import Counter
    status_counts = Counter(ne['status'] for ne in nes)
    print("Status counts:", status_counts)

    # 9. NE name -> IP的dict
    name_to_ip = {ne['name']: ne['ip'] for ne in nes}
    print("Name to IP mapping:", name_to_ip)

def result_counter():
    result = ['PASS', 'FAIL', 'PASS', 'PASS', 'FAIL', 'PASS']
    from collections import Counter
    result_counts = Counter(result)
    print("Result counts:", result_counts)


if __name__ == '__main__':
    # dict()
    # dict_for()
    # dict_list()
    # tuple()
    # dict_config()
    # dict_config_update()
    result_counter()