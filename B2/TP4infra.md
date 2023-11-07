# TP4 : Router-on-a-stick

## I. Topo 1 : VLAN et Routing

### 3. Setup topologie 1

🌞 Adressage
```powershell
PC1> ip 10.1.10.1 255.255.255.0
PC2> ip 10.1.10.2 255.255.255.0
adm1> ip 10.1.20.1 255.255.255.0
Web1> ip 10.1.30.1 255.255.255.0
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
R1#show ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            unassigned      YES unset  administratively down down
FastEthernet0/0.10         10.1.10.254     YES manual administratively down down
FastEthernet0/0.20         10.1.20.254     YES manual administratively down down
FastEthernet0/0.30         10.1.30.254     YES manual administratively down down
FastEthernet0/1            unassigned      YES unset  administratively down down
```

🌞 Vérif
```powershell

```