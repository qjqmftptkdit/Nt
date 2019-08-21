from scapy.all import sniff, Raw

class Sniff :
    def __init__(self, interface, target, kinds, filter, extract) :
        
        if filter :
            self.filter = filter 
        elif target or kinds:
            self.filter = self._getFilter(target, kinds)
        else :
            self.filter = False 

        if extract :
            self.extract = extract
        else :
            self.extract = False

        self.interface = interface

    # 스니핑을 시작한다.
    def startSniff(self) :
        g = '\033[92m'
        e = '\033[0m'
        print(g+"[*] Sniffing이 시작됨"+e)

        number = 0
        if self.extract : # 파일에 내용 출력
            if self.filter : # 필터링
                while True :
                    result = sniff(timeout=1, filter=self.filter, iface=self.interface)
                    with open(self.extract, "a") as f :
                        for i in result :
                            number += 1
                            result = "#{} {}".format(number, i.summary())
                            if Raw in i :
                                result += " / Data : {}".format(i[Raw].load)
                            print(result)
                            f.write(result+'\n')
            else :
                while True :
                    result = sniff(timeout=1, iface=self.interface)
                    with open(self.extract, "a") as f :
                        for i in result :
                            number += 1
                            result = "#{} {}".format(number, i.summary())
                            if Raw in i :
                                result += " / Data : {}".format(i[Raw].load)
                            print(result)
                            f.write(result+'\n')

        else : # 내용을 출력하지 않는다.
            if self.filter : # 필터링
                while True :
                    result = sniff(timeout=1, filter=self.filter, iface=self.interface)
                    for i in result :
                        number += 1
                        result = "#{} {}".format(number, i.summary())
                        if Raw in i :
                            result += " / Data : {}".format(i[Raw].load)
                        print(result)

            else :
                while True :
                    result = sniff(timeout=1, iface=self.interface)
                    for i in result :
                        number += 1
                        result = "#{} {}".format(number, i.summary())
                        if Raw in i :
                            result += " / Data : {}".format(i[Raw].load)
                        print(result)

    # 주어진 값을 이용해서 필터링에 사용할 문자열을 반환한다.
    def _getFilter(self, target, kinds) :
        if target and kinds :
            return "host {} and {}".format(target, kinds)
        elif target :
            return "host {}".format(target)
        else :
            return kinds

# 도움말을 출력한다.
def help () :
    print("nt.py -a 2 -i <Network InterFace> [-t <AddressToFilter>] [-k <PorotocolToFilter>] [-f <FilterString>] [-e <FileNameToSave>]")
    print("-t : 해당 Ip 주소가 포함된 패킷만 스니핑합니다.")
    print("-k : 해당 프로토콜만 스니핑합니다.")
    print("-f : 직접 필터링을 위한 문자열을 적습니다. (앞의 -t -k 인자가 무시됨)")
    print("-e : 해당 인자를 이름으로 해서 결과를 텍스트파일로 저장합니다.")
    print("ex) nt.py -a 2 -i eth0 -t 192.168.111.2 -k ip -e result.txt")
    print('ex) nt.py -a 2 -i eth0 -f "host 192.168.111.2 and ip" -e result.txt')