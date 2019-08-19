from scapy.all import sr, IP, TCP

class tcpConnectScan :
    def __init__(self, interface, targetIp, dstPorts) :
        if dstPorts :
            self._dstports = self._getDstPorts(dstPorts)
        else :
            self._dstports = [0, 8, 20, 21, 22, 23, 25, 53, 80, 110, 123, 161, 162, 443, 445, 1433, 1521, 3306, 8080, 3389]
        self._portlist = {0:"ICMP", 8:"ICMP", 20:"FTP(data)", 21:"FTP(send)", 22:"SSH", 23:"Telnet", 25:"SMTP", 53:"DNS", 80:"http", 110:"POP3", 123:"NTP", 145:"netBios", 161:"SNMP", 443:"https", 1433:"mssql", 1521:"oracle", 3305:"mysql", 3389:"MsService", 8080:"oracle"}
        self._interface = interface
        self._targetIp = targetIp

    def startScan(self) :
        g = '\033[92m'
        e = '\033[0m'
        print(g+"[*] TCP Connection Port Scanning이 시작됨"+e)

        ans, unans = sr(IP(dst=self._targetIp)/TCP(dport=self._dstports, flags="S"), timeout=3, iface=self._interface, verbose=False)

        print("총 보낸 패킷 갯수 :", len(ans) + len(unans))
        print("응답된 패킷 갯수 :", len(ans))
        print("응답되지 않은패킷 갯수 :", len(unans))
        print(g+"[*] 활성화된 포트 정보"+e)

        print("포트번호 / 사용용도")
        for send, recv in ans :
            if recv[TCP].flags == 'SA' :
                scanPort = send[TCP].dport
                if scanPort in self._portlist :
                    portName = self._portlist[scanPort]
                else :
                    portName = "특정불가"
                
                print("{} / {}".format(scanPort, portName))

        print(g+"[*] TCP Connection Port Scanning이 완료됨"+e)
    
    def _getDstPorts(self, dstPorts) :
        dstPortList = []
        for port in dstPorts.split(',') :
            if '-' in port :
                n1 = int(port.split('-')[0])
                n2 = int(port.split('-')[1])
                for i in range(n1,n2+1) :
                    dstPortList.append(i)
            else :
                dstPortList.append(int(port))
        return dstPortList

# 도움말을 출력한다.
def help_tcpConnect() :
    print("nt.py -s 3 -i <Network InterFace> -t <TargetIpAddress> [-p <Port>]")
    print("-p : 특정 포트를 지정할 수 있으며, 없을 경우 자주 사용되는 포트들을 스캔합니다.")
    print("ex) nt.py -s 3 -i eth0 -t 192.168.111.3 -p 10-30,80")