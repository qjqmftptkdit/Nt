import argparse
import scan

def main() :
    parser = argparse.ArgumentParser(description="nt.py -s <ScanNum> [Options]")

    parser.add_argument("-s", "--scantype", type=int, help="스캔타입을 지정한다. 1:Arpscan")
    parser.add_argument("-i", "--interface", help="네트워크 인터페이스를 설정한다.")
    parser.add_argument("-r", "--range", help="네트워크 범위를 지정한다.")

    args = parser.parse_args()
    if args.scantype==1 :
        if args.interface and args.range :
            scan.arpScan(args.interface, args.range)
        else :
            print("nt.py -s 1 -i <Network InterFace> -r <Ip Range>")
            print("ex) nt.py -s 1 -i eth0 -r 192.168.111.1/24")
    else :
        print("nt.py -s <ScanNum> [Options]")

if __name__ == "__main__" :
    main()
