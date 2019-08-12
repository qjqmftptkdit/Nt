import argparse
import arpScan

def main() :
    parser = argparse.ArgumentParser(description="nt.py -s <ScanNum> [Options]")

    parser.add_argument("-s", "--scantype", type=int, help="스캔타입을 지정한다. 1:Arpscan")
    parser.add_argument("-i", "--interface", help="네트워크 인터페이스를 설정한다.")
    parser.add_argument("-r", "--range", help="네트워크 범위를 지정한다.")
    parser.add_argument("-o", "--option", help="추가적인 옵션을 지정한다.")

    args = parser.parse_args()
    if args.scantype==1 :
        if args.interface and args.range :
            arpScan.scan(args.interface, args.range, args.option)
        else :
            print("nt.py -s 1 -i <Network InterFace> -r <Ip Range> [-o option]")
            print("-o 없음 : 일반 ARP 스캐닝(DEFAULT)")
            print("-o 1 : 1~3초간 랜덤으로 간격을 두고 보낸다.")
            print("-o 2 : ip주소를 순서대로 보내지 않고, 무작위로 보낸다.")
            print("-o 3 : 1,2의 옵션이 결합됨")
            print("ex) nt.py -s 1 -i eth0 -r 192.168.111.1/24")
    else :
        print("nt.py -s <ScanNum> [Options]")

if __name__ == "__main__" :
    main()
