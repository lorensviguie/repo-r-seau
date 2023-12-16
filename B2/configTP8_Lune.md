```powershell
Batiment2#show running-config
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

```
# R1
```powershell

R1#show running-config
nterface FastEthernet0/0
 no ip address
 shutdown
 duplex auto
 speed auto
!
interface FastEthernet0/1
 no ip address
 duplex auto
 speed auto
!
interface FastEthernet0/1.5
 encapsulation dot1Q 5
 ip address 10.7.5.254 255.255.255.0
!
interface FastEthernet0/1.10
 encapsulation dot1Q 10
 ip address 10.7.10.254 255.255.255.0
!
interface FastEthernet0/1.11
 encapsulation dot1Q 11
 ip address 10.7.11.254 255.255.255.0
 ip helper-address 10.8.5.251
!
interface FastEthernet0/1.40
 encapsulation dot1Q 40
 ip address 10.7.40.254 255.255.255.0
!
interface FastEthernet0/1.45
 encapsulation dot1Q 45
 ip address 10.7.45.254 255.255.255.0
!
interface FastEthernet0/1.50
 encapsulation dot1Q 50
 ip address 10.7.50.254 255.255.255.0
!
interface FastEthernet0/1.60
 encapsulation dot1Q 60
 ip address 10.7.60.254 255.255.255.0
!
interface FastEthernet0/1.65
 encapsulation dot1Q 65
 ip address 10.7.65.254 255.255.255.0
 ip helper-address 10.8.5.251
!
interface FastEthernet0/1.70
 encapsulation dot1Q 70
 ip address 10.7.70.254 255.255.255.0
 ip helper-address 10.8.5.251
!
interface FastEthernet1/0
 ip address 10.10.1.253 255.255.255.252
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
 router-id 1.1.1.1
 log-adjacency-changes
 network 10.7.11.0 0.0.0.255 area 1
!

```
```powershell
IOU6#show running-config
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

```
```powershell

Serveur1#show running-config
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk

```
```powershell
IOU3#show running-config
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
interf
```
```powershell
IOU5#show running-config
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

```
```powershell
Batiment1#show running-config
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

```
```powershell
serveurtest2#show running-config
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
 switchport mode acces
```
```powershell
Serveurtest#show running-config
interface Ethernet0/0
 switchport access vlan 5,10
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
 switchport mode acces
!
[...]
interface Ethernet2/0
 switchport access vlan 5
 switchport mode access
!

```
```powershell
openSpace#show running-config
interface Ethernet0/1
 switchport access vlan 45
 switchport mode access
!
interface Ethernet0/2
 switchport access vlan 45
 switchport mode access
!
interface Ethernet0/3
 switchport access vlan 45
 switchport mode access
!
interface Ethernet1/0
 switchport access vlan 50
 switchport mode access
!
interface Ethernet1/1
 switchport access vlan 40
 switchport mode access
!
interface Ethernet1/2
 switchport access vlan 40
 switchport mode access
```
```powershell
LOPD#show running-config
interface Ethernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
!
interface Ethernet0/1
!
interface Ethernet0/2
!
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
!

```

