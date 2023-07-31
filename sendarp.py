from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp
import get_ip_list


#  对指定ip发送arp包，超时时间1秒
# def send_arp_request(dst_ip, network_interface):
#     arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=dst_ip)
#     arp_response = srp(arp_request, timeout=1, iface=network_interface, verbose=False)[0]
#     if arp_response:
#         return dst_ip


# print(send_arp_request("10.29.164.2", "WLAN"))


def send_arp_request(ip_range: str, network_interface: str):
    # ip_list = []
    ip_list = get_ip_list.get_ip_range(ip_range)
    for ip in ip_list:
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(op=1, pdst=ip)
        arp_response = srp(arp_request, timeout=1, iface=network_interface, verbose=False)[0]
        if arp_response:
            return ip

print(send_arp_request("192.168.1.1/23", "WLAN"))