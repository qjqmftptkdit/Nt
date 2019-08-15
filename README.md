NetworkTools(NT) 0.2.0  
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
### 1. Arp-Scanning(LAN)
python nt.py -s 1 -i \<Network Interface> -r \<Network Range> [-o \<Option>]  
option 없음 : 일반 ARP 스캐닝(DEFAULT)  
option 1 : 1~3초간 랜덤으로 간격을 두고 보낸다.  
option 2 : ip주소를 순서대로 보내지 않고, 무작위로 보낸다.  
option 3 : 1,2의 옵션이 결합됨  
~~~bash
python nt.py -s 1 -i eth0 -r 192.168.0.1/24 -o 2
~~~

### 2. Arp-Spoofing(LAN)
python nt.py -a 1 -i \<Network InterFace> -t \<TargetIpAddress> -g \<GatewayIpAddress>
~~~bash
python nt.py -a 1 -i eth0 -t 192.168.111.3 -g 192.168.111.1
~~~

### 3. ICMP-Scanning(WAN)
python nt.py -s 2 -i \<Network Interface> -r \<Network Range> [-o \<Option>]  
option 없음 : 일반 ICMP 스캐닝(DEFAULT)  
option 1 : 1~3초간 랜덤으로 간격을 두고 보낸다.  
option 2 : ip주소를 순서대로 보내지 않고, 무작위로 보낸다.  
option 3 : 1,2의 옵션이 결합됨  
~~~bash
python nt.py -s 2 -i eth0 -r 67.210.233.1/24 -o 2
~~~