# TP4 : Router-on-a-stick

## I. Topo 1 : VLAN et Routing

### 3. Setup topologie 1

🌞 Adressage
```powershell
PC1> ip 10.1.10.1 255.255.255.0 10.1.10.254
PC2> ip 10.1.10.2 255.255.255.0 10.1.10.254
adm1> ip 10.1.20.1 255.255.255.0 10.1.20.254
```

🌞 Configuration des VLANs

```powershell
sw1#show vlan br

VLAN Name                             Status    Ports
[...]
10   VLAN0010                         active    Et0/1, Et0/2
20   VLAN0020                         active    Et0/3
30   VLAN0030                         active    Et1/0

sw1(config)#interface Et0/0
sw1(config-if)#switchport trunk encapsulation dot1q
sw1(config-if)#switchport mode trunk
sw1(config-if)#switchport trunk allowed vlan add 10,20,30
sw1(config-if)#exit
sw1(config)#exit
sw1#show interface trunk

Port        Mode             Encapsulation  Status        Native vlan
Et0/0       on               802.1q         trunking      1

Port        Vlans allowed on trunk
Et0/0       1-4094

Port        Vlans allowed and active in management domain
Et0/0       1,10,20,30

Port        Vlans in spanning tree forwarding state and not pruned
Et0/0       none

```

🌞 Config du routeur
```powershell
RI(config) interface fastEthernet 0/1.10
R1(config-subif)# encapsulation dot1Q 10
R1(config-subif)# ip addr 10.1.10.254 255.255.255.0 
R1(config-subif)# exit
RI(config) interface fastEthernet 0/1.20
R1(config-subif)# encapsulation dot1Q 20
R1(config-subif)# ip addr 10.1.20.254 255.255.255.0 
R1(config-subif)# exit
RI(config) interface fastEthernet 0/1.30
R1(config-subif)# encapsulation dot1Q 30
R1(config-subif)# ip addr 10.1.30.254 255.255.255.0 
R1(config-subif)# exit
R1(config)#interface fastEthernet 0/1
R1(config-if)#no shut

R1#show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            unassigned      YES unset  administratively down down
FastEthernet0/1            unassigned      YES unset  up                    up
FastEthernet0/1.10         10.1.10.254     YES manual up                    up
FastEthernet0/1.20         10.1.20.254     YES manual up                    up
FastEthernet0/1.30         10.1.30.254     YES manual up                    up

```

🌞 Vérif

la route par default a été setup lors de l'attribution des ip au debut du tp
```powershell
adm1> ping 10.1.30.1
84 bytes from 10.1.30.1 icmp_seq=1 ttl=63 time=29.767 ms

PC1> ping 10.1.20.1

84 bytes from 10.1.20.1 icmp_seq=1 ttl=63 time=19.459 ms

PC2> ping 10.1.30.1

84 bytes from 10.1.30.1 icmp_seq=1 ttl=63 time=29.626 ms

```


## II. NAT

### 3. Setup topologie 2

🌞 Ajoutez le noeud Cloud à la topo

```powershell


R1(config)#interface FastEthernet0/0
R1(config-if)#ip address dhcp
R1(config-if)#no shut


R1#ping 1.1.1.1

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 1.1.1.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 16/20/28 ms

```

🌞 Configurez le NAT

```powershell
(config)# interface fastEthernet 0/0
(config-if)# ip nat outside
(config-if)# exit

(config)# interface fastEthernet 0/1
(config-if)# ip nat inside
(config-if)# exit


R1(config)#access-list 1 permit any
R1(config)#ip nat inside source list 1 interface fastEthernet 0/0 overload

```

🌞 Test

```powershell
PC1> ip dns 1.1.1.1

PC1> show ip

NAME        : PC1[1]
IP/MASK     : 10.1.10.1/24
GATEWAY     : 10.1.10.254
DNS         : 1.1.1.1
MAC         : 00:50:79:66:68:00
LPORT       : 20012
RHOST:PORT  : 127.0.0.1:20013
MTU         : 1500

PC1> ping google.com
google.com resolved to 142.250.178.142

84 bytes from 142.250.178.142 icmp_seq=1 ttl=114 time=29.620 ms
84 bytes from 142.250.178.142 icmp_seq=2 ttl=114 time=24.150 ms

```

## III. Add a building
### 3. Setup topologie 3

🌞  Vous devez me rendre le show running-config de tous les équipements
```powershell

sw3#show running-config
[...]
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport access vlan 10
 switchport mode access
!
interface Ethernet0/2
 switchport access vlan 10
 switchport mode access
!
interface Ethernet0/3
 switchport access vlan 10
 switchport mode access
!
interface Ethernet1/0
 switchport access vlan 10
 switchport mode access
[...]

sw2#show running-config
[...]
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport access vlan 10
 switchport mode access
!
interface Ethernet0/2
 switchport access vlan 10
 switchport mode access
!
interface Ethernet0/3
 switchport access vlan 20
 switchport mode access
!
interface Ethernet1/0
 switchport access vlan 30
 switchport mode access
[...]

sw1#show running-config
[...]
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
[...]

R1#show running-config
[...]
interface FastEthernet0/0
 ip address dhcp
 ip nat outside
 ip virtual-reassembly
 duplex auto
 speed auto
!
interface FastEthernet0/1
 no ip address
 ip nat inside
 ip virtual-reassembly
 duplex auto
 speed auto
!
interface FastEthernet0/1.10
 encapsulation dot1Q 10
 ip address 10.1.10.254 255.255.255.0
!
interface FastEthernet0/1.20
 encapsulation dot1Q 20
 ip address 10.1.20.254 255.255.255.0
!
interface FastEthernet0/1.30
 encapsulation dot1Q 30
 ip address 10.1.30.254 255.255.255.0
[...]
```

🌞  Mettre en place un serveur DHCP dans le nouveau bâtiment


```powershell
PC4> dhcp
DDORA IP 10.1.10.101/24 GW 10.1.10.254

```
🌞  Vérification
```powershell
PC3> dhcp
DDORA IP 10.1.10.100/24 GW 10.1.10.254

PC3> show ip

NAME        : PC3[1]
IP/MASK     : 10.1.10.100/24
GATEWAY     : 10.1.10.254
DNS         : 8.8.8.8

PC3> ping 10.1.30.1

84 bytes from 10.1.30.1 icmp_seq=1 ttl=63 time=13.630 ms
84 bytes from 10.1.30.1 icmp_seq=2 ttl=63 time=15.910 ms

PC3> ping 1.1.1.1

1.1.1.1 icmp_seq=1 timeout
84 bytes from 1.1.1.1 icmp_seq=2 ttl=55 time=37.429 ms
84 bytes from 1.1.1.1 icmp_seq=3 ttl=55 time=27.557 ms

PC3> ping ynov.com
ynov.com resolved to 104.26.11.233

84 bytes from 104.26.11.233 icmp_seq=1 ttl=55 time=31.328 ms

```