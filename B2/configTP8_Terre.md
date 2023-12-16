```powershell
IOU2#show running-config
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
!
interface Ethernet1/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet1/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
```

```powershell
IOU1#show running-config
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
!
interface Ethernet1/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet1/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
!

```
```powershell
Etage1#show running-config

interface Ethernet0/0
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

```
```powershell
etage2#show running-config
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

```
# R2
```powershell
R2#show running-config
interface FastEthernet0/0
 no ip address
 duplex auto
 speed auto
!
interface FastEthernet0/0.5
 encapsulation dot1Q 5
 ip address 10.8.5.252 255.255.255.240
 ip access-group ACCES_LIST_internet out
 ip nat inside
 ip virtual-reassembly
 standby 5 ip 10.8.5.254
 standby 5 priority 50
!
interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.8.10.252 255.255.255.192
 ip access-group ACCES_LIST_internet out
 ip nat inside
 ip virtual-reassembly
 standby 10 ip 10.8.10.254
 standby 10 preempt
!
interface FastEthernet0/0.11
 encapsulation dot1Q 11
 ip address 10.8.11.12 255.255.255.240
 ip access-group ACCES_LIST_ADMIN in
 ip nat inside
 ip virtual-reassembly
 standby 11 ip 10.8.11.14
 standby 11 preempt
!
interface FastEthernet0/0.40
 encapsulation dot1Q 40
 ip address 10.8.40.252 255.255.255.240
 ip access-group ACCES_LIST_RIEN in
 standby 40 ip 10.8.40.254
 standby 40 preempt
!
interface FastEthernet0/0.45
 encapsulation dot1Q 45
 ip address 10.8.45.252 255.255.255.240
 standby 45 ip 10.8.45.254
 standby 45 preempt
!
interface FastEthernet0/0.50
 encapsulation dot1Q 50
 ip address 10.8.50.252 255.255.255.240
 ip access-group ACCES_LIST_RIEN in
 standby 50 ip 10.8.50.254
 standby 50 preempt
!
interface FastEthernet0/0.60
 encapsulation dot1Q 60
 ip address 10.8.60.252 255.255.255.0
 ip nat inside
 ip virtual-reassembly
 standby 60 ip 10.8.60.254
 standby 60 preempt
!
interface FastEthernet0/0.65
 encapsulation dot1Q 65
 ip address 10.8.65.108 255.255.255.240
 ip access-group ACCES_LIST_DIRECTION in
 ip nat inside
 ip virtual-reassembly
 standby 65 ip 10.8.65.110
 standby 65 preempt
!
interface FastEthernet0/0.70
 encapsulation dot1Q 70
 ip address 10.8.70.252 255.255.255.0
 ip access-group ACCES_LIST_DEV in
 ip nat inside
 ip virtual-reassembly
 standby 70 ip 10.8.70.254
 standby 70 preempt
!
interface FastEthernet0/1
 ip address dhcp
 ip nat outside
 ip virtual-reassembly
 duplex auto
 speed auto
!
interface FastEthernet0/1.11
 ip helper-address 10.8.5.251
!
interface FastEthernet0/1.65
 ip helper-address 10.8.5.251
!
interface FastEthernet0/1.70
 ip helper-address 10.8.5.251
!
interface FastEthernet1/0
 ip address 10.10.1.254 255.255.255.252
 duplex auto
 speed auto
!
interface FastEthernet2/0
 no ip address
 shutdown
 duplex auto
 speed auto
!
router ospf 1
 router-id 2.2.2.2
 log-adjacency-changes
 network 10.8.5.240 0.0.0.15 area 2
 network 10.8.10.192 0.0.0.63 area 2
 network 10.8.11.0 0.0.0.15 area 2
 network 10.8.40.240 0.0.0.15 area 2
 network 10.8.45.240 0.0.0.15 area 2
 network 10.8.50.240 0.0.0.15 area 2
 network 10.8.60.0 0.0.0.255 area 2
 network 10.8.65.96 0.0.0.15 area 2
 network 10.8.70.0 0.0.0.255 area 2
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip nat inside source list 1 interface FastEthernet0/1 overload
!
ip access-list extended ACCES_LIST_ADMIN
 permit ip 10.8.11.0 0.0.0.15 10.8.65.96 0.0.0.15
 permit ip 10.8.11.0 0.0.0.15 10.8.45.240 0.0.0.15
 permit ip 10.8.11.0 0.0.0.15 10.8.40.240 0.0.0.15
 permit ip 10.8.11.0 0.0.0.15 10.8.50.240 0.0.0.15
 permit ip 10.8.11.0 0.0.0.15 10.8.60.0 0.0.0.255
 permit ip 10.8.11.0 0.0.0.15 10.8.70.0 0.0.0.255
 permit ip 10.8.11.0 0.0.0.15 10.8.5.240 0.0.0.15
 permit ip 10.8.11.0 0.0.0.15 10.8.10.192 0.0.0.63
 permit ip 10.8.11.0 0.0.0.15 any
 deny   ip any any log
ip access-list extended ACCES_LIST_DEV
 permit ip 10.8.70.0 0.0.0.255 10.8.10.192 0.0.0.63
 permit ip 10.8.70.0 0.0.0.255 10.8.50.240 0.0.0.15
 permit ip 10.8.70.0 0.0.0.255 10.8.40.240 0.0.0.15
 permit ip 10.8.70.0 0.0.0.255 host 10.8.5.249
 permit ip 10.8.70.0 0.0.0.255 any
 deny   ip any any log
ip access-list extended ACCES_LIST_DIRECTION
 permit ip 10.8.65.96 0.0.0.15 10.8.40.240 0.0.0.15
 permit ip 10.8.65.96 0.0.0.15 10.8.50.240 0.0.0.15
 permit ip 10.8.65.96 0.0.0.15 any
 deny   ip any any log
ip access-list extended ACCES_LIST_RIEN
 deny   ip any any log
ip access-list extended ACCES_LIST_camera
 deny   ip any any log
 permit ip 10.8.45.240 0.0.0.15 host 10.8.5.248
ip access-list extended ACCES_LIST_internet
 permit ip 10.8.0.0 0.0.255.255 any
 deny   ip any any log
!
logging trap debugging
logging 10.8.5.248
access-list 1 permit any
no cdp log mismatch duplex
!
!
```

# R3
```powershell
R3#show running-config

interface FastEthernet0/0
 no ip address
 duplex auto
 speed auto
!
interface FastEthernet0/0.5
 encapsulation dot1Q 5
 ip address 10.8.5.253 255.255.255.240
 ip access-group ACCES_LIST_internet out
 ip nat inside
 ip virtual-reassembly
 standby 5 ip 10.8.5.254
 standby 5 preempt
!
interface FastEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.8.10.253 255.255.255.192
 ip access-group ACCES_LIST_internet out
 ip nat inside
 ip virtual-reassembly
 standby 10 ip 10.8.10.254
 standby 10 priority 50
!
interface FastEthernet0/0.11
 encapsulation dot1Q 11
 ip address 10.8.11.13 255.255.255.240
 ip access-group ACCES_LIST_ADMIN in
 ip nat inside
 ip virtual-reassembly
 standby 11 ip 10.8.11.14
 standby 11 priority 50
!
interface FastEthernet0/0.40
 encapsulation dot1Q 40
 ip address 10.8.40.253 255.255.255.240
 ip access-group ACCES_LIST_RIEN in
 standby 40 ip 10.8.40.254
 standby 40 priority 50
!
interface FastEthernet0/0.45
 encapsulation dot1Q 45
 ip address 10.8.45.253 255.255.255.240
 standby 45 ip 10.8.45.254
 standby 45 priority 50
!
interface FastEthernet0/0.50
 encapsulation dot1Q 50
 ip address 10.8.50.253 255.255.255.240
 ip access-group ACCES_LIST_RIEN in
 standby 50 ip 10.8.50.254
 standby 50 priority 50
!
interface FastEthernet0/0.60
 encapsulation dot1Q 60
 ip address 10.8.60.253 255.255.255.0
 ip nat inside
 ip virtual-reassembly
 standby 60 ip 10.8.60.254
 standby 60 priority 50
!
interface FastEthernet0/0.65
 encapsulation dot1Q 65
 ip address 10.8.65.109 255.255.255.240
 ip access-group ACCES_LIST_DIRECTION in
 ip nat inside
 ip virtual-reassembly
 standby 65 ip 10.8.65.110
 standby 65 priority 50
!
interface FastEthernet0/0.70
 encapsulation dot1Q 70
 ip address 10.8.70.253 255.255.255.0
 ip access-group ACCES_LIST_DEV in
 ip nat inside
 ip virtual-reassembly
 standby 70 ip 10.8.70.254
 standby 70 priority 50
!
interface FastEthernet0/1
 ip address dhcp
 ip nat outside
 ip virtual-reassembly
 duplex auto
 speed auto
!
interface FastEthernet0/1.11
 ip helper-address 10.8.5.251
!
interface FastEthernet0/1.65
 ip helper-address 10.8.5.251
!
interface FastEthernet0/1.70
 ip helper-address 10.8.5.251
!
interface FastEthernet1/0
 no ip address
 shutdown
 duplex auto
 speed auto
!
interface FastEthernet2/0
 no ip address
 shutdown
 duplex auto
 speed auto
!
ip forward-protocol nd
!
!
no ip http server
no ip http secure-server
ip nat inside source list 1 interface FastEthernet0/1 overload
!
ip access-list extended ACCES_LIST_ADMIN
 permit ip 10.8.11.0 0.0.0.15 10.8.65.96 0.0.0.15
 permit ip 10.8.11.0 0.0.0.15 10.8.45.240 0.0.0.15
 permit ip 10.8.11.0 0.0.0.15 10.8.40.240 0.0.0.15
 permit ip 10.8.11.0 0.0.0.15 10.8.50.240 0.0.0.15
 permit ip 10.8.11.0 0.0.0.15 10.8.60.0 0.0.0.255
 permit ip 10.8.11.0 0.0.0.15 10.8.70.0 0.0.0.255
 permit ip 10.8.11.0 0.0.0.15 10.8.5.240 0.0.0.15
 permit ip 10.8.11.0 0.0.0.15 10.8.10.192 0.0.0.63
 permit ip 10.8.11.0 0.0.0.15 any
 deny   ip any any log
ip access-list extended ACCES_LIST_DEV
 permit ip 10.8.70.0 0.0.0.255 10.8.10.192 0.0.0.63
 permit ip 10.8.70.0 0.0.0.255 10.8.50.240 0.0.0.15
 permit ip 10.8.70.0 0.0.0.255 10.8.40.240 0.0.0.15
 permit ip 10.8.70.0 0.0.0.255 host 10.8.5.249
 permit ip 10.8.70.0 0.0.0.255 any
 deny   ip any any log
ip access-list extended ACCES_LIST_DIRECTION
 permit ip 10.8.65.96 0.0.0.15 10.8.40.240 0.0.0.15
 permit ip 10.8.65.96 0.0.0.15 10.8.50.240 0.0.0.15
 permit ip 10.8.65.96 0.0.0.15 any
 deny   ip any any log
ip access-list extended ACCES_LIST_RIEN
 deny   ip any any log
ip access-list extended ACCES_LIST_camera
 permit ip 10.8.45.240 0.0.0.15 host 10.8.5.248
 deny   ip any any log
ip access-list extended ACCES_LIST_internet
 permit ip 10.8.0.0 0.0.255.255 any
 deny   ip any any log
!
logging trap debugging
logging 10.8.5.248
access-list 1 permit any
no cdp log mismatch duplex
!
```
```powershell
RDC#show running-config

```
```powershell
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport access vlan 45
 switchport trunk encapsulation dot1q
 switchport mode access
!
interface Ethernet0/2
 switchport access vlan 65
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/3
 switchport access vlan 65
 switchport mode access
!
interface Ethernet1/0
 switchport access vlan 65
 switchport mode access
!
interface Ethernet1/1
 switchport access vlan 45
 switchport mode access

```
```powershell
Serveur#show running-config
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
!
interface Ethernet1/0
 switchport access vlan 5
 switchport mode access
!
interface Ethernet1/1
 switchport access vlan 5
 switchport mode access
!
interface Ethernet1/2
 switchport access vlan 5
 switchport mode access
!
interface Ethernet1/3
 switchport access vlan 5
 switchport mode access
!

```
```powershell
ServeurTEST#show running-config
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/2
 switchport access vlan 10
 switchport mode access

```
```powershell
OpenSpace1#show running-config
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
 switchport access vlan 50
 switchport mode access
!
interface Ethernet0/2
 switchport access vlan 70
 switchport mode access
!
interface Ethernet0/3
 switchport access vlan 70
 switchport mode access
!
interface Ethernet1/0
 switchport access vlan 70
 switchport mode acces

```
```powershell

OpenSpace#show running-config
interface Ethernet0/1
 switchport access vlan 11
 switchport mode access
!
interface Ethernet0/2
 switchport access vlan 11
 switchport mode access
!
interface Ethernet0/3
 switchport access vlan 11
 switchport mode access
!
interface Ethernet1/0
 switchport access vlan 70
 switchport mode access
!
interface Ethernet1/1
 switchport access vlan 70
 switchport mode access
!
interface Ethernet1/2
 switchport access vlan 70
 switchport mode access
!
interface Ethernet1/3
 switchport access vlan 70
 switchport mode access

```
```powershell
Bureaux1#show running-config
interface Ethernet0/1
 switchport access vlan 65
 switchport mode access
!
interface Ethernet0/2
 switchport access vlan 65
 switchport mode access
!
interface Ethernet0/3
 switchport access vlan 65
 switchport mode access
!
interface Ethernet1/0
 switchport access vlan 50
 switchport mode access
!
interface Ethernet1/1
 switchport access vlan 45
 switchport mode access
!
interface Ethernet1/2
 switchport access vlan 40
 switchport mode access
!
interface Ethernet1/3
 switchport access vlan 45
 switchport mode access
!

```
