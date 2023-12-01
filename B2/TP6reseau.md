# TP6 : STP, OSPF, bigger infra

## I. STP

🌞 Configurer STP sur les 3 switches

```powershell
IOU3#show spanning-tree

VLAN0001
  Spanning tree enabled protocol rstp
  Root ID    Priority    32769
             Address     aabb.cc00.0100
             Cost        100
             Port        2 (Ethernet0/1)
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec

  Bridge ID  Priority    32769  (priority 32768 sys-id-ext 1)
             Address     aabb.cc00.0300
             Hello Time   2 sec  Max Age 20 sec  Forward Delay 15 sec
             Aging Time  300 sec

Interface           Role Sts Cost      Prio.Nbr Type
------------------- ---- --- --------- -------- --------------------------------
Et0/0               Altn BLK 100       128.1    Shr
Et0/1               Root FWD 100       128.2    Shr
Et0/2               Desg FWD 100       128.3    Shr
Et0/3               Desg FWD 100       128.4    Shr
Et1/0               Desg FWD 100       128.5    Shr
Et1/1               Desg FWD 100       128.6    Shr
Et1/2               Desg FWD 100       128.7    Shr
```


🌞 Altérer le spanning-tree

```powershell
IOU3#show spanning-tree
[...]
Et0/0               Desg FWD 100       128.1    Shr
Et0/1               Root FWD 100       128.2    Shr
Et0/2               Desg FWD 100       128.3    Shr
Et0/3               Desg FWD 100       128.4    Shr
Et1/0               Desg FWD 100       128.5    Shr
Et1/1               Desg FWD 100       128.6    Shr
Et1/2               Desg FWD 100       128.7    Shr
```

🌞 Altérer le spanning-tree

```powershell
IOU3(config)#interface Et 0/0
IOU3(config-if)#spanning-tree cost 10
IOU3#show spanning-tree
[...]
Et0/0               Root FWD 10        128.1    Shr
Et0/1               Altn BLK 20000000  128.2    Shr
```
[🦈 tp6_stp.pcapng](./tramewirehsark/stp.pcapng)


## II. OSPF

🌞 Montez la topologie

```powershell
waf> show ip
NAME        : waf[1]
IP/MASK     : 10.6.1.11/24
GATEWAY     : 10.6.1.254
meo> show ip
NAME        : meo[1]
IP/MASK     : 10.6.2.11/24
GATEWAY     : 10.6.2.254
john> show ip

NAME        : john[1]
IP/MASK     : 10.6.3.11/24
GATEWAY     : 10.6.3.254

```
conf des routeur avec OSPF
[routeur 1](/tp6_config/r1.txt)
[routeur 2](/tp6_config/r2.txt)
[routeur 3](/tp6_config/r3.txt)
[routeur 4](/tp6_config/r4.txt)
[routeur 5](/tp6_config/r5.txt)  


🌞 Configurer OSPF sur tous les routeurs
```powershell
R1#show ip route
     10.0.0.0/8 is variably subnetted, 8 subnets, 2 masks
O       10.6.13.0/30 [110/30] via 10.6.21.2, 00:12:21, FastEthernet0/0
O       10.6.1.0/24 [110/2] via 10.6.41.2, 00:11:32, FastEthernet1/0
O       10.6.2.0/24 [110/11] via 10.6.41.2, 00:11:32, FastEthernet1/0
C       10.6.3.0/24 is directly connected, FastEthernet2/0
C       10.6.21.0/30 is directly connected, FastEthernet0/0
O       10.6.23.0/30 [110/20] via 10.6.21.2, 00:12:21, FastEthernet0/0
C       10.6.41.0/30 is directly connected, FastEthernet1/0
O IA    10.6.52.0/30 [110/11] via 10.6.21.2, 00:12:22, FastEthernet0/0

R2#show ip route
     10.0.0.0/8 is variably subnetted, 8 subnets, 2 masks
O       10.6.13.0/30 [110/20] via 10.6.23.2, 00:20:14, FastEthernet0/1
O IA    10.6.1.0/24 [110/12] via 10.6.21.1, 00:12:13, FastEthernet0/0
O IA    10.6.2.0/24 [110/21] via 10.6.21.1, 00:12:13, FastEthernet0/0
O IA    10.6.3.0/24 [110/11] via 10.6.21.1, 00:17:07, FastEthernet0/0
C       10.6.21.0/30 is directly connected, FastEthernet0/0
C       10.6.23.0/30 is directly connected, FastEthernet0/1
O IA    10.6.41.0/30 [110/11] via 10.6.21.1, 00:12:48, FastEthernet0/0
C       10.6.52.0/30 is directly connected, FastEthernet1/0

R3# show ip route
     10.0.0.0/8 is variably subnetted, 8 subnets, 2 masks
C       10.6.13.0/30 is directly connected, FastEthernet0/0
O IA    10.6.1.0/24 [110/22] via 10.6.23.1, 00:12:40, FastEthernet0/1
O IA    10.6.2.0/24 [110/31] via 10.6.23.1, 00:12:40, FastEthernet0/1
O IA    10.6.3.0/24 [110/21] via 10.6.23.1, 00:17:35, FastEthernet0/1
O       10.6.21.0/30 [110/20] via 10.6.23.1, 00:20:43, FastEthernet0/1
C       10.6.23.0/30 is directly connected, FastEthernet0/1
O IA    10.6.41.0/30 [110/21] via 10.6.23.1, 00:13:16, FastEthernet0/1
O IA    10.6.52.0/30 [110/11] via 10.6.23.1, 00:20:34, FastEthernet0/1

R4#show ip route
     10.0.0.0/8 is variably subnetted, 8 subnets, 2 masks
O IA    10.6.13.0/30 [110/40] via 10.6.41.1, 00:13:21, FastEthernet0/0
C       10.6.1.0/24 is directly connected, FastEthernet1/0
C       10.6.2.0/24 is directly connected, FastEthernet0/1
O IA    10.6.3.0/24 [110/11] via 10.6.41.1, 00:13:21, FastEthernet0/0
O IA    10.6.21.0/30 [110/20] via 10.6.41.1, 00:13:21, FastEthernet0/0
O IA    10.6.23.0/30 [110/30] via 10.6.41.1, 00:13:21, FastEthernet0/0
C       10.6.41.0/30 is directly connected, FastEthernet0/0
O IA    10.6.52.0/30 [110/21] via 10.6.41.1, 00:13:22, FastEthernet0/0

R5#show ip route
     10.0.0.0/8 is variably subnetted, 8 subnets, 2 masks
O IA    10.6.13.0/30 [110/30] via 10.6.52.2, 00:13:45, FastEthernet0/1
O IA    10.6.1.0/24 [110/22] via 10.6.52.2, 00:13:45, FastEthernet0/1
O IA    10.6.2.0/24 [110/31] via 10.6.52.2, 00:13:45, FastEthernet0/1
O IA    10.6.3.0/24 [110/21] via 10.6.52.2, 00:13:45, FastEthernet0/1
O IA    10.6.21.0/30 [110/20] via 10.6.52.2, 00:13:45, FastEthernet0/1
O IA    10.6.23.0/30 [110/20] via 10.6.52.2, 00:13:45, FastEthernet0/1
O IA    10.6.41.0/30 [110/21] via 10.6.52.2, 00:13:47, FastEthernet0/1
C       10.6.52.0/30 is directly connected, FastEthernet0/1

R1#show ip ospf neighbor
Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/DR         00:00:38    10.6.21.2       FastEthernet0/0
4.4.4.4           1   FULL/DR         00:00:34    10.6.41.2       FastEthernet1/0
R2#show ip ospf neighbor
Neighbor ID     Pri   State           Dead Time   Address         Interface
3.3.3.3           1   FULL/DR         00:00:31    10.6.23.2       FastEthernet0/1
1.1.1.1           1   FULL/BDR        00:00:37    10.6.21.1       FastEthernet0/0
5.5.5.5           1   FULL/BDR        00:00:37    10.6.52.1       FastEthernet1/0
R3#show ip ospf neighbor
Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/BDR        00:00:39    10.6.23.1       FastEthernet0/1
R4#show ip ospf neighbor
Neighbor ID     Pri   State           Dead Time   Address         Interface
1.1.1.1           1   FULL/BDR        00:00:38    10.6.41.1       FastEthernet0/0
R5#show ip ospf neighbor
Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/DR         00:00:31    10.6.52.2       FastEthernet0/1
```

🌞 Test
```powershell
PC3> ping 1.1.1.1

1.1.1.1 icmp_seq=1 timeout
84 bytes from 1.1.1.1 icmp_seq=2 ttl=86 time=67.429 ms
84 bytes from 1.1.1.1 icmp_seq=3 ttl=86 time=57.557 ms
PC3> ping 10.6.3.11

84 bytes from 10.6.3.11 icmp_seq=1 ttl=62 time=51.403 ms
84 bytes from 10.6.3.11 icmp_seq=2 ttl=62 time=32.458 ms
84 bytes from 10.6.3.11 icmp_seq=3 ttl=62 time=36.131 ms
84 bytes from 10.6.3.11 icmp_seq=4 ttl=62 time=33.474 ms
84 bytes from 10.6.3.11 icmp_seq=5 ttl=62 time=34.991 ms
PC2> ping 10.6.52.1

84 bytes from 10.6.52.1 icmp_seq=1 ttl=252 time=64.417 ms
84 bytes from 10.6.52.1 icmp_seq=2 ttl=252 time=45.035 ms
PC2> ping 10.6.52.2

84 bytes from 10.6.52.2 icmp_seq=1 ttl=253 time=51.398 ms
PC1> ping 10.6.21.2

84 bytes from 10.6.21.2 icmp_seq=1 ttl=254 time=24.660 ms
84 bytes from 10.6.21.2 icmp_seq=2 ttl=254 time=30.411 ms
PC1> ping 10.6.52.1

84 bytes from 10.6.52.1 icmp_seq=1 ttl=253 time=50.166 ms
84 bytes from 10.6.52.1 icmp_seq=2 ttl=253 time=45.148 ms
```

[🦈 tp6_ospf.pcapng](./tramewirehsark/bpdus.pcapng)

## III. DHCP relay
