NetworkTools(NT) 1.0.0 
===
## 1. 개요
네트워크 스캐닝 및 해킹툴 제작하기 프로젝트

## 2. 실행시키는 방법
1. python을 설치한다.
~~~bash
sudo apt-get install python3.6
~~~
2. scapy를 설치한다.
~~~bash
pip install scapy
~~~
3. nt.py를 실행시킨다.
~~~bash
python nt.py --help
~~~

## 3. 사용해보기
## > Scanning  
### 1. Arp-Scanning(LAN)
python nt.py -s 1 -i \<Network Interface> -r \<Network Range> [-o \<Option>]  
option 없음 : 일반 ARP 스캐닝(DEFAULT)  
option 1 : 1~3초간 랜덤으로 간격을 두고 보낸다.  
option 2 : ip주소를 순서대로 보내지 않고, 무작위로 보낸다.  
option 3 : 1,2의 옵션이 결합됨.  
~~~bash
python nt.py -s 1 -i eth0 -r 192.168.0.1/24 -o 2
~~~

### 2. ICMP-Scanning(WAN)
python nt.py -s 2 -i \<Network Interface> -r \<Network Range> [-o \<Option>]  
option 없음 : 일반 ICMP 스캐닝(DEFAULT)  
option 1 : 1~3초간 랜덤으로 간격을 두고 보낸다.  
option 2 : ip주소를 순서대로 보내지 않고, 무작위로 보낸다.  
option 3 : 1,2의 옵션이 결합됨.  
~~~bash
python nt.py -s 2 -i eth0 -r 67.210.233.1/24 -o 2
~~~

### 3. TCP Connection Port Scanning
python nt.py -s 3 -i \<Network InterFace> -t \<TargetIpAddress> [-p \<Port>]  
-p 옵션 없음 : 자주 사용되는 포트를 중심으로 스캐닝한다.
-p 옵션 : 22,80 이나 80-90 과 같이 특정 포트를 지정할 수 있다.
~~~bash
python nt.py -s 3 -i eth0 -t 192.168.111.3 -p 10-30,80
~~~

## > Attack  
### 1. Arp-Spoofing(LAN)
python nt.py -a 1 -i \<Network InterFace> -t \<TargetIpAddress> -g \<GatewayIpAddress>
~~~bash
python nt.py -a 1 -i eth0 -t 192.168.111.3 -g 192.168.111.1
~~~

### 2. Sniffing  
nt.py -a 2 -i \<Network InterFace> [-t \<AddressToFilter>] [-k \<PorotocolToFilter>] [-f \<FilterString>] [-e \<FileNameToSave>]  
-t : 해당 Ip 주소가 포함된 패킷만 스니핑한다.  
-k : 해당 프로토콜만 스니핑한다.  
-f : 직접 필터링을 위한 문자열을 적는다. (앞의 -t -k 인자가 무시됨)  
-e : 해당 인자를 이름으로 해서 결과를 텍스트파일로 저장한다.  
~~~bash
python nt.py -a 2 -i eth0 -t 192.168.111.2 -k ip -e result.txt  
python nt.py -a 2 -i eth0 -f "host 192.168.111.2 and ip" -e result.txt
~~~