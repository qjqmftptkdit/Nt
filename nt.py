# -*- coding: utf-8 -*- 
import argparse
import arpScan
import arpSpoofing
import icmpScan

def main() :
    parser = argparse.ArgumentParser(description="nt.py [-s|-a] <TypeNum> [Options]")

    parser.add_argument("-s", "--scantype", type=int, help="스캔타입을 지정한다. 1:Arpscan, 2:IcmpScan")
    parser.add_argument("-a", "--attacktype", type=int, help="공격타입을 지정한다. 1:ArpSpoofing")
    parser.add_argument("-i", "--interface", help="네트워크 인터페이스를 설정한다.")
    parser.add_argument("-r", "--range", help="네트워크 범위를 지정한다.")
    parser.add_argument("-o", "--option", help="추가적인 옵션을 지정한다.")
    parser.add_argument("-t", "--target", help="타겟 주소를 지정한다.")
    parser.add_argument("-g", "--gateway", help="게이트웨이 주소를 지정한다.")

    args = parser.parse_args()
    if args.scantype==1 :
        if args.interface and args.range :
            arpScan.scan(args.interface, args.range, args.option)
        else :
            arpScan.help()
    elif args.scantype==2 :
        if args.interface and args.range :
            icmpScan.scan(args.interface, args.range, args.option)
        else :
            icmpScan.help()

    elif args.attacktype==1 :
        if args.interface and args.target and args.gateway :
            arpSpoofing.ArpSpoofing(args.interface, args.target, args.gateway).startArpSpoofing()
        else :
            arpSpoofing.help()
    else :
        print("nt.py [-s|-a] <TypeNum> [Options]")

if __name__ == "__main__" :
    main()
