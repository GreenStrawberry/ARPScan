import socket
import struct
import ipaddress


# A类地址:10.0.0.0至10.255.255.255
# B类地址:172.16.0.0 至172.31.255.255
# C类地址:192.168.0.0至192.168.255.255


def ip_range(start_ip: str, end_ip: str):
    start = struct.unpack('!I', socket.inet_aton(start_ip))[0]
    end = struct.unpack('!I', socket.inet_aton(end_ip))[0]
    ip_list = []
    for ip in range(start, end + 1):
        ip_list.append(socket.inet_ntoa(struct.pack('!I', ip)))
    return ip_list


# 给定一个范围的ip,输出这个范围里面所有的ip地址
def get_ip_range(ip_str: str):
    if len(ip_str.split("-")) == 2:
        first_ip = ip_str.split("-")[0]
        last_ip = ip_str.split("-")[1]
        ip_list = ip_range(first_ip, last_ip)
        return ip_list
    elif ipaddress.IPv4Network(ip_str):
        network = ipaddress.ip_network(ip_str, strict=False)
        first_ip = str(network.network_address + 1)
        last_ip = str(network.broadcast_address - 1)
        ip_list = ip_range(first_ip, last_ip)
        return ip_list
    else:
        return False


def ip_cidr(ip_address, subnet_mask):
    try:
        # 将IP地址和子网掩码转换为ipaddress对象
        ip_network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask}", strict=False)

        # 获取第一个主机位和最后一个主机位
        first_host = ip_network.network_address + 1
        last_host = ip_network.broadcast_address - 1

        return str(first_host), str(last_host)
    except ipaddress.AddressValueError:
        return None, None


# 检查输入的ip地址的范围格式是否合法
def check_ip_range_format(ip_range_str: str):
    if len(ip_range_str.split("-")) == 2:
        start_ip = ip_range_str.split("-")[0]
        last_ip = ip_range_str.split("-")[1]
        if ipaddress.IPv4Network(start_ip) and ipaddress.IPv4Network(last_ip):
            start_ip_a = int(start_ip.split(".")[0])
            start_ip_b = int(start_ip.split(".")[1])
            start_ip_c = int(start_ip.split(".")[2])
            start_ip_d = int(start_ip.split(".")[3])
            last_ip_a = int(last_ip.split(".")[0])
            last_ip_b = int(last_ip.split(".")[1])
            last_ip_c = int(last_ip.split(".")[2])
            last_ip_d = int(last_ip.split(".")[3])
            # 开始的ip要比结束的ip要小，
            if start_ip_a < last_ip_a:
                return True
            elif start_ip_a == last_ip_a:
                if start_ip_b < last_ip_b:
                    return True
                elif start_ip_b == last_ip_b:
                    if start_ip_c < last_ip_c:
                        return True
                    elif start_ip_c == last_ip_c:
                        if start_ip_d < last_ip_d:
                            return True
                        elif start_ip_d == last_ip_d:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


print(check_ip_range_format("192.168.1.1-192.167.2.2"))


# 检查输入的ip地址的范围格式是否合法
def check_ip_cidr_format(ip_range_str: str):
    if len(ip_range_str.split("/")) == 2:
        ip_address = ip_range_str.split("/")[0]
        subnet_mask = int(ip_range_str.split("/")[1])
        if 8 <= subnet_mask <= 30:
            if ipaddress.IPv4Network(ip_address):
                return True
        else:
            return False
    else:
        return False
