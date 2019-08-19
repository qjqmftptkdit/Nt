# -*- coding: utf-8 -*- 
import argparse
import arpScan
import arpSpoofing
import icmpScan
import portScan

def main() :
    parser = argparse.ArgumentParser(description="nt.py [-s|-a] <TypeNum> [Options]")

    parser.add_argument("-s", "--scantype", type=int, help="스캔타입을 지정한다. (0으로 목록확인 가능)")
    parser.add_argument("-a", "--attacktype", type=int, help="공격타입을 지정한다. (0으로 목록확인 가능)")
    parser.add_argument("-i", "--interface", help="네트워크 인터페이스를 설정한다.")
    parser.add_argument("-r", "--range", help="네트워크 범위를 지정한다.")
    parser.add_argument("-o", "--option", help="추가적인 옵션을 지정한다.")
    parser.add_argument("-t", "--target", help="타겟 주소를 지정한다.")
    parser.add_argument("-g", "--gateway", help="게이트웨이 주소를 지정한다.")
    parser.add_argument("-p", "--port", help="스캔할 포트를 지정한다.")

    args = parser.parse_args()
    if args.scantype==0 :
        showScanType()
    elif args.scantype==1 :
        if args.interface and args.range :
            arpScan.scan(args.interface, args.range, args.option)
        else :
            arpScan.help()
    elif args.scantype==2 :
        if args.interface and args.range :
            icmpScan.scan(args.interface, args.range, args.option)
        else :
            icmpScan.help()
    elif args.scantype==3 :
        if args.interface and args.target :
            portScan.tcpConnectScan(args.interface, args.target, args.port).startScan()
        else :
            portScan.help_tcpConnect()

    elif args.attacktype==0 :
        showAttackType()
    elif args.attacktype==1 :
        if args.interface and args.target and args.gateway :
            arpSpoofing.ArpSpoofing(args.interface, args.target, args.gateway).startArpSpoofing()
        else :
            arpSpoofing.help()
    else :
        print("nt.py [-s|-a] <TypeNum> [Options]")

def showScanType() :
    print("0 : 스캔타입 목록 출력")
    print("1 : Arp Scanning [LAN 전용]")
    print("2 : Icmp Scanning [WAN 전용]")
    print("3 : TCP Connection Port Scanning")

def showAttackType() :
    print("0 : 공격타입 목록 출력")
    print("1 : Arp Spoofing [LAN 전용]")

if __name__ == "__main__" :
    main()
