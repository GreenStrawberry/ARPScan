import psutil


def get_network_interface():
    net_if_addrs = psutil.net_if_addrs()
    network_interface_list = []

    # 遍历网卡信息并输出名称和地址
    for interface_name, interface_addresses in net_if_addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                # print(interface_name)
                network_interface_list.append(interface_name)
    return network_interface_list
# print(get_network_interface())

