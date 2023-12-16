# TP7 INFRA : 3-tier architecture et redondance

## 0. Setup

### E. Preuve et rendu
🌞 show-run sur tous les équipements
- routeur 
```powershell
R1
#R1 show run
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
 ip address 10.7.10.253 255.255.255.0
 standby 10 ip 10.7.10.254
 standby 10 priority 150
!
interface FastEthernet0/1.20
 encapsulation dot1Q 20
 ip address 10.7.20.253 255.255.255.0
 standby 10 ip 10.7.20.254
 standby 10 priority 150
!
interface FastEthernet0/1.30
 encapsulation dot1Q 30
 ip address 10.7.30.253 255.255.255.0
 standby 10 ip 10.7.30.254
no ip http server
no ip http secure-server
ip nat inside source list 1 interface FastEthernet0/0 overload
!
access-list 1 permit any
[...]

R2
R2#show run
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
 ip address 10.7.10.252 255.255.255.0
 standby 10 ip 10.7.10.254
!
interface FastEthernet0/1.20
 encapsulation dot1Q 20
 ip address 10.7.20.252 255.255.255.0
 standby 10 ip 10.7.20.254
!
interface FastEthernet0/1.30
 encapsulation dot1Q 30
 ip address 10.7.30.252 255.255.255.0
 standby 10 ip 10.7.30.254
 standby 10 priority 150
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip nat inside source list 1 interface FastEthernet0/0 overload
[...]
```
- switch core
```powershell
Sw1
#sw1 show run
[...]
interface Port-channel1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 channel-group 1 mode on
!
interface Ethernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 channel-group 1 mode on
!
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet1/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
[...]
IOU1#show etherchannel
                Channel-group listing:
                ----------------------

Group: 1
----------
Group state = L2
Ports: 2   Maxports = 4
Port-channels: 1 Max Port-channels = 1
Protocol:    -
Minimum Links: 0


Sw2
#sw2 show run
[...]
interface Port-channel1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 channel-group 1 mode on
!
interface Ethernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 channel-group 1 mode on
!
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet1/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
[...]
IOU2#show etherchannel port
                Channel-group listing:
                ----------------------

Group: 1
----------
                Ports in the group:
                -------------------
Port: Et0/1
------------

Port state    = Up Mstr In-Bndl
Channel group = 1           Mode = On              Gcchange = -
Port-channel  = Po1         GC   =   -             Pseudo port-channel = Po1
Port index    = 0           Load = 0x00            Protocol =    -

Age of the port in the current state: 0d:00h:35m:58s

Port: Et0/2
------------

Port state    = Up Mstr In-Bndl
Channel group = 1           Mode = On              Gcchange = -
Port-channel  = Po1         GC   =   -             Pseudo port-channel = Po1
Port index    = 0           Load = 0x00            Protocol =    -

```
- switch distrib
```powershell
Sw3
#sw3 show run
[...]
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet1/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
[...]
Sw4
#sw4 show run
[...]
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet1/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!

[...]
```
- switch acces
```powershell
Sw5
#sw5 show run
[...]
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/2
 switchport access vlan 10
 switchport mode access
!
interface Ethernet0/3
 switchport access vlan 20
 switchport mode access

[...]

Sw6
#sw6 show run
[...]
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/2
!
interface Ethernet0/3
 switchport access vlan 20
 switchport mode access

[...]

Sw7
#sw7 show run
[...]
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/2
 switchport access vlan 30
 switchport mode access

[...]
```
🌞 depuis pc4.tp7.b1
10.7.10.12 existe pas
```powershell

PC4> ping 10.7.20.12

84 bytes from 10.7.20.12 icmp_seq=1 ttl=63 time=30.007 ms
84 bytes from 10.7.20.12 icmp_seq=2 ttl=63 time=16.265 ms
PC4> ping ynov.com
ynov.com resolved to 104.26.11.233



```

## 3. Bonus

### A. ACL

🌞 Le réseau 10.7.30.0/24...
sur tous les switch acces
```powershell
configure terminal
interface ethernet 0/3
spanning-tree bpduguard enable
exit
interface ethernet 0/2
spanning-tree bpduguard enable
exit
exit
```

### C. Observe then destroy then observe
🌞 Vérifier, à l'aide de commandes dédiées
-  l'état de l'agrégation LACP entre sw1 et sw2 
```powershell
sw1#show etherchannel summary 
Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)          -        Et0/1(P)    Et0/2(P)

sw1#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-ip

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination IP address
  IPv6: Source XOR Destination IP address

sw2#show etherchannel summary
Number of channel-groups in use: 1
Number of aggregators:           1

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1      Po1(SU)          -        Et0/1(P)    Et0/2(P)
sw2#show etherchannel load-balance
EtherChannel Load-Balancing Configuration:
        src-dst-ip

EtherChannel Load-Balancing Addresses Used Per-Protocol:
Non-IP: Source XOR Destination MAC address
  IPv4: Source XOR Destination IP address
  IPv6: Source XOR Destination IP address
```
-   l'état de la liaison HSRP entre r1 et r2
```powershell
R1#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa0/1.10    10   100   Standby 10.7.10.253     local           10.7.10.254
Fa0/1.20    10   100   Standby 10.7.20.253     local           10.7.20.254
Fa0/1.30    10   150   Active  local           10.7.30.253     10.7.30.254
R2#show standby brief
                     P indicates configured to preempt.
                     |
Interface   Grp  Pri P State   Active          Standby         Virtual IP
Fa0/1.10    10   150   Active  local           10.7.10.252     10.7.10.254
Fa0/1.20    10   150   Active  local           10.7.20.252     10.7.20.254
Fa0/1.30    10   100   Standby 10.7.30.252     local           10.7.30.254

```
- l'état de STP, par VLAN sur trois switches (un core, un distrib, un access)
```powershell
sw1#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             This bridge is the root
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0100
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Desg FWD 100       128.1    Shr
Et0/3               Desg FWD 100       128.4    Shr
Et1/0               Desg FWD 100       128.5    Shr
Et1/1               Desg FWD 100       128.6    Shr
Et1/2               Desg FWD 100       128.7    Shr
Et1/3               Desg FWD 100       128.8    Shr
Et2/0               Desg FWD 100       128.9    Shr
Et2/1               Desg FWD 100       128.10   Shr
Et2/2               Desg FWD 100       128.11   Shr
Et2/3               Desg FWD 100       128.12   Shr
Et3/0               Desg FWD 100       128.13   Shr
Et3/1               Desg FWD 100       128.14   Shr
Et3/2               Desg FWD 100       128.15   Shr
Et3/3               Desg FWD 100       128.16   Shr
Po1                 Desg FWD 56        128.65   Shr

sw3#show spanning-tree
[...]
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Root FWD 100       128.1    Shr
Et0/1               Altn BLK 100       128.2    Shr
Et0/2               Desg FWD 100       128.3    Shr
Et0/3               Desg FWD 100       128.4    Shr
Et1/0               Desg FWD 100       128.5    Shr
Et1/1               Desg FWD 100       128.6    Shr
Et1/2               Desg FWD 100       128.7    Shr

sw6#show spanning-tree
[...]
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Root FWD 100       128.1    Shr
Et0/1               Altn BLK 100       128.2    Shr
Et0/2               Desg FWD 100       128.3    Shr
Et1/0               Desg FWD 100       128.5    Shr
Et1/1               Desg FWD 100       128.6    Shr
Et1/2               Desg FWD 100       128.7    Shr
Et1/3               Desg FWD 100       128.8    Shr
Et2/0               Desg FWD 100       128.9    Shr
Et2/1               Desg FWD 100       128.10   Shr
Et2/2               Desg FWD 100       128.11   Shr
Et2/3               Desg FWD 100       128.12   Shr
Et3/0               Desg FWD 100       128.13   Shr
Et3/1               Desg FWD 100       128.14   Shr
Et3/2               Desg FWD 100       128.15   Shr
Et3/3               Desg FWD 100       128.16   Shr
```
🌞 Couper le routeur prioritaire

```powershell
#j'ai coupé le r1 pendant le ping et je relancé un ping dés que le premier c'est finit
PC4> ping 10.7.30.11

84 bytes from 10.7.30.11 icmp_seq=1 ttl=63 time=21.337 ms
84 bytes from 10.7.30.11 icmp_seq=2 ttl=63 time=16.383 ms
84 bytes from 10.7.30.11 icmp_seq=3 ttl=63 time=7.875 ms
10.7.30.11 icmp_seq=4 timeout
10.7.30.11 icmp_seq=5 timeout

PC4> ping 10.7.30.11

10.7.30.11 icmp_seq=1 timeout
84 bytes from 10.7.30.11 icmp_seq=2 ttl=63 time=21.377 ms
84 bytes from 10.7.30.11 icmp_seq=3 ttl=63 time=12.119 ms
84 bytes from 10.7.30.11 icmp_seq=4 ttl=63 time=21.034 ms
84 bytes from 10.7.30.11 icmp_seq=5 ttl=63 time=17.912 ms

```

🌞 Couper un switch crucial dans la topo STP
```powershell
#on a couper la swtich qui relie le routeur prio pour les client 
PC4> ping 10.7.10.254

84 bytes from 10.7.10.254 icmp_seq=1 ttl=255 time=9.630 ms
84 bytes from 10.7.10.254 icmp_seq=2 ttl=255 time=7.118 ms
84 bytes from 10.7.10.254 icmp_seq=3 ttl=255 time=1.607 ms
10.7.10.254 icmp_seq=4 timeout
10.7.10.254 icmp_seq=5 timeout

PC4> ping 10.7.10.254

host (10.7.10.254) not reachable

PC4> ping 10.7.10.254

84 bytes from 10.7.10.254 icmp_seq=1 ttl=255 time=19.760 ms
84 bytes from 10.7.10.254 icmp_seq=2 ttl=255 time=7.258 ms
84 bytes from 10.7.10.254 icmp_seq=3 ttl=255 time=4.901 ms
84 bytes from 10.7.10.254 icmp_seq=4 ttl=255 time=7.735 ms
84 bytes from 10.7.10.254 icmp_seq=5 ttl=255 time=9.995 ms

```