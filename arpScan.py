# Arp Scanning을 실행한다.
def scan(interface, ipRange, option) :
    g = '\033[92m'
    e = '\033[0m'
    v = '\033[95m'

    print(g+"[*] ARP Scanning이 시작됨"+e)
    from scapy.all import srp,Ether,ARP,conf
    import random
    import time

    if option : # Option
        ipList = getIpList(ipRange)
    else : # No Option
        ipList = ipRange

    conf.verb=0
    ans=[]; unans=[]

    if option=='1' : # Option
        print(g+"[*] 옵션 : 1~3초간 랜덤으로 간격을 두고 보낸다."+e)
        for i in range(len(ipList)) :
            time.sleep(random.randrange(1,4))
            _ans, _unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ipList[i]), iface=interface, timeout=0.2)
            if(_ans) : ans.append((_ans[0][0].pdst, _ans[0][1].src))
            if(_unans) : unans.append(_unans[0].pdst)
            if(i%10==0) : print(v+"[*] 현재 진행률 : "+str(int(i/len(ipList)*100))+"%"+e)
    elif option=='2' :
        print(g+"[*] 옵션 : ip주소를 순서대로 보내지 않고, 무작위로 보낸다."+e)
        ipListLen = len(ipList)
        for i in range(ipListLen) :
            selNum = random.randrange(0, len(ipList))
            _ans, _unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ipList[selNum]), iface=interface, timeout=0.2)
            if(_ans) : ans.append((_ans[0][0].pdst, _ans[0][1].src))
            if(_unans) : unans.append(_unans[0].pdst)
            del ipList[selNum]
            if(i%10==0) : print(v+"[*] 현재 진행률 : "+str(int(i/ipListLen*100))+"%"+e)
    elif option=='3' :
        print(g+"[*] 옵션 : 1,2 옵션이 결합됨"+e)
        ipListLen = len(ipList)
        for i in range(ipListLen) :
            time.sleep(random.randrange(1,4))
            selNum = random.randrange(0, len(ipList))
            _ans, _unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ipList[selNum]), iface=interface, timeout=0.2)
            if(_ans) : ans.append((_ans[0][0].pdst, _ans[0][1].src))
            if(_unans) : unans.append(_unans[0].pdst)
            del ipList[selNum]
            if(i%10==0) : print(v+"[*] 현재 진행률 : "+str(int(i/ipListLen*100))+"%"+e)
    else : # No Option
        print(g+"[*] 기본 ARP Scanning"+e)
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ipList), iface=interface, timeout=2)

    
    print("총 보낸 주소 갯수 :", len(ans) + len(unans))
    print("응답된 주소 갯수 :", len(ans))
    print("응답되지 않은 주소 갯수 :", len(unans))
    print(g+"[*] 상세정보"+e)

    if option : # Option
        for pdst, src in ans :
            print(pdst, " -> ", src)
    else : # No Option
        for send, recv in ans :
            print(send.pdst, " -> ", send.src)
    
    print(g+"[*] ARP Scanning이 완료됨"+e)

# ipList를 얻는다.
def getIpList(ipRange) :
    ip, ntBits = ipRange.split('/')
    ipList = []

    if ntBits=="24" :
        for i in range(256) :
            ipList.append(".".join(ip.split('.')[:-1]) + "." + str(i))
    elif ntBits=="16" :
        for i in range(256) :
            for j in range(256) :
                ipList.append(".".join(ip.split('.')[:-2]) + "." + str(i) + "." + str(j))   
    elif ntBits=="8" :
        for i in range(256) :
            for j in range(256) :
                for z in range(256) :
                    ipList.append(".".join(ip.split('.')[:-3]) + "." + str(i) + "." + str(j) + "." + str(z))   

    return ipList

