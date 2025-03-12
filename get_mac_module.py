import scapy.all as scapy

def get_mac(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcastingt_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcastingt_packet / arp_packet
    
    
    answered = scapy.srp(combined_packet, timeout=2, verbose=False)[0]
    if answered:
        for (sent, received) in answered:
            return received.hwsrc
    else:
        return None

    
    

