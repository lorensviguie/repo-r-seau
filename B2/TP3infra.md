# TP3 INFRA : Premiers pas GNS, Cisco et VLAN

## I. Dumb switch

### 3. Setup topologie 1

🌞 Commençons simple
```powershell

PC2> ip 10.3.1.2 255.255.255.0
Checking for duplicate address...
PC2 : 10.3.1.2 255.255.255.0

PC1> ip 10.3.1.1 255.255.255.0
Checking for duplicate address...
PC1 : 10.3.1.1 255.255.255.0

PC1> ping 10.3.1.2

84 bytes from 10.3.1.2 icmp_seq=1 ttl=64 time=0.108 ms
84 bytes from 10.3.1.2 icmp_seq=2 ttl=64 time=0.260 ms
84 bytes from 10.3.1.2 icmp_seq=3 ttl=64 time=0.259 ms



PC2> show ip
[...]
MAC         : 00:50:79:66:68:01
[...]

PC1> show ip
[...]
MAC         : 00:50:79:66:68:00
[...]

IOU1#show mac address-table
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
   1    0050.7966.6800    DYNAMIC     Et0/1
   1    0050.7966.6801    DYNAMIC     Et0/2
Total Mac Addresses for this criterion: 2

```


## II. VLAN

### 3. Setup topologie 2

🌞 Adressage

```powershell

PC3> show ip
NAME        : PC3[1]
[...]
IP/MASK     : 10.3.1.3/24
[...]

PC1> ping 10.3.1.2

84 bytes from 10.3.1.2 icmp_seq=1 ttl=64 time=0.108 ms
84 bytes from 10.3.1.2 icmp_seq=2 ttl=64 time=0.260 ms
84 bytes from 10.3.1.2 icmp_seq=3 ttl=64 time=0.259 ms

PC1> ping 10.3.1.3

84 bytes from 10.3.1.3 icmp_seq=1 ttl=64 time=0.104 ms
84 bytes from 10.3.1.3 icmp_seq=2 ttl=64 time=0.245 ms
84 bytes from 10.3.1.3 icmp_seq=3 ttl=64 time=0.273 ms

```

🌞 Configuration des VLANs

```powershell

IOU1(config)#vlan 10
IOU1(config-vlan)#name Vlan10
IOU1(config-vlan)#exit
IOU1(config)#vlan 20
IOU1(config-vlan)#name Vlan20
IOU1(config-vlan)#exit
IOU1(config)#interface Et0/1
IOU1(config-if)#switchport mode
IOU1(config-if)#switchport mode access
IOU1(config-if)#switchport acces vlan 10
IOU1(config-if)#no shutdown
IOU1(config-if)#exit
IOU1(config)#interface Et0/2
IOU1(config-if)#switchport mode access
IOU1(config-if)#switchport acces vlan 10
IOU1(config-if)#no shutdown
IOU1(config-if)#exit
IOU1(config)#interface Et0/3
IOU1(config-if)#switchport mode access
IOU1(config-if)#switchport acces vlan 20
IOU1(config-if)#no shutdown
IOU1(config-if)#exit

IOU1#show vlan br

VLAN Name                             Status    Ports
[...]
10   Vlan10                           active    Et0/1, Et0/2
20   Vlan20                           active    Et0/3

PC3> ping 10.3.1.1
host (10.3.1.1) not reachable
PC3> ping 10.3.1.2
host (10.3.1.2) not reachable

PC1> ping 10.3.1.2
84 bytes from 10.3.1.2 icmp_seq=1 ttl=64 time=0.123 ms
84 bytes from 10.3.1.2 icmp_seq=2 ttl=64 time=0.236 ms
PC1> ping 10.3.1.3
host (10.3.1.3) not reachable

PC2> ping 10.3.1.1
84 bytes from 10.3.1.1 icmp_seq=1 ttl=64 time=0.533 ms
PC2> ping 10.3.1.3
host (10.3.1.3) not reachable
```

## III. Ptite VM DHCP