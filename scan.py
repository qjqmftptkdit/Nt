def arpScan(interface, range) :
    g = '\033[92m'
    e = '\033[0m'
    print(g+"[*] ARP Scanning이 시작됨"+e)

    from scapy.all import srp,Ether,ARP,conf
    conf.verb=0
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=range), iface=interface, timeout=2)

    print("총 보낸 주소 갯수 :", len(ans) + len(unans))
    print("응답된 주소 갯수 :", len(ans))
    print("응답되지 않은 주소 갯수 :", len(unans))
    print(g+"[*] 상세정보"+e)

    for send, recv in ans :
        print(send.pdst, " -> ", send.src)
    
    print(g+"[*] ARP Scanning이 완료됨"+e)



