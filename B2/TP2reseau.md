# TP2 : Environnement virtuel

## 0. Prérequis


## I. Topologie réseau

### ☀️ Sur node1.lan1.tp2

```powershell
$ ssh it5@10.1.1.11
it5@10.1.1.11 s password:
Last login: Thu Oct 19 14:54:38 2023 from 10.1.1.1
[it5@node1 ~]$ hostname
node1.lan1.tp2

[it5@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:f9:ef:34 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fef9:ef34/64 scope link
       valid_lft forever preferred_lft forever

[it5@node1 ~]$ sudo nano /proc/net/arp
IP address       HW type     Flags       HW address            Mask     Device
10.1.1.254       0x1         0x2         08:00:27:03:e8:22     *        enp0s8
10.1.1.12        0x1         0x2         08:00:27:27:c4:fc     *        enp0s8
10.1.1.1         0x1         0x2         0a:00:27:00:00:0e     *        enp0s8

[it5@node1 ~]$ ping 10.1.2.12
PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=0.487 ms
64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=0.967 ms
^C
--- 10.1.2.12 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1040ms
rtt min/avg/max/mdev = 0.487/0.727/0.967/0.240 ms
[it5@node1 ~]$ traceroute 10.1.2.12
traceroute to 10.1.2.12 (10.1.2.12), 30 hops max, 60 byte packets
 1  _gateway (10.1.1.254)  0.929 ms  0.886 ms  0.836 ms
 2  10.1.2.12 (10.1.2.12)  0.758 ms !X  0.740 ms !X  0.652 ms !X
```

## II. Interlude accès internet

### ☀️ Sur router.tp2

```powershell
[it5@routertp2 ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=112 time=23.0 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=112 time=22.9 ms
^C
--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 22.875/22.956/23.037/0.081 ms

[it5@routertp2 ~]$ ping www.ynov.com
PING www.ynov.com (172.67.74.226) 56(84) bytes of data.
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=1 ttl=56 time=10.3 ms
^C64 bytes from 172.67.74.226: icmp_seq=2 ttl=56 time=12.1 ms

--- www.ynov.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 10.274/11.169/12.064/0.895 ms

```

### ☀️ Accès internet LAN1 et LAN2

```powershell
[it5@node1.lan1.tp2]$ sudo cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
[sudo] password for it5:
DEVICE=enp0s8

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.1.11
NETMASK=255.255.255.0

GATEWAY=10.1.1.254
DNS1=1.1.1.1
[it5@node1.lan1.tp2]$ sudo systemctl restart NetworkManager

[it5@node2 ~]$ sudo cat /etc/sysconfig/network-scripts/ifcfg-enp0s9
DEVICE=enp0s9

BOOTPROTO=static
ONBOOT=yes

IPADDR=10.1.2.12
NETMASK=255.255.255.0

GATEWAY=10.1.1.254
DNS1=8.8.8.8
[it5@node2 ~]$ sudo systemctl restart NetworkManager
[it5@node1 ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=111 time=22.4 ms
^C
--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 22.429/22.429/22.429/0.000 ms
[it5@node1 ~]$ ping www.ynov.com
PING www.ynov.com (172.67.74.226) 56(84) bytes of data.
64 bytes from 172.67.74.226 (172.67.74.226): icmp_seq=1 ttl=55 time=11.7 ms
^C
--- www.ynov.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 11.661/11.661/11.661/0.000 ms
```

## III. Services réseau

### 1. DHCP

#### ☀️ Sur dhcp.lan1.tp2

```powershell
[it5@dhcp ~]$ hostname
dhcp.lan1.tp2
[it5@dhcp ~]$ sudo cat /etc/sysconfig/network-scripts/ifcfg-enp0s8 | grep IP
IPADDR=10.1.1.253

[it5@dhcp ~]$ sudo dnf -y install dhcp-server
[root@dhcp it5]# sudo cat /etc/dhcp/dhcpd.conf
option domain-name     "srv.world";
# specify DNS server's hostname or IP address
option domain-name-servers     1.1.1.1;
# default lease time
default-lease-time 600;
# max lease time
max-lease-time 7200;
# this DHCP server to be declared valid
authoritative;
# specify network address and subnetmask
subnet 10.1.1.0 netmask 255.255.255.0 {
    # specify the range of lease IP address
    range dynamic-bootp 10.1.1.100 10.1.1.200;
    # specify broadcast address
    option broadcast-address 10.1.1.255;
    # specify gateway
    option routers 10.1.1.254;
}

[it5@dhcp it5]# sudo systemctl status dhcpd | grep Acti
     Active: active (running) since Thu 2023-10-19 16:03:02 CEST; 1min 12s ago

```

#### ☀️ Sur node1.lan1.tp2

```powershell
[it5@node1 ~]$ ip a
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:f9:ef:34 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.100/24 brd 10.1.1.255 scope global dynamic noprefixroute enp0s8
       valid_lft 517sec preferred_lft 517sec
    inet6 fe80::a00:27ff:fef9:ef34/64 scope link
       valid_lft forever preferred_lft forever

```

### 2. Web web web

#### ☀️ Sur web.lan2.tp2

```powershell
[it5@web ~]$ ss -tuln | grep :80
LISTEN     0      128           *:80                     *:*

[it5@web ~]$ sudo firewall-cmd --add-port=80/tcp --permanent
success

[it5@web ~]$ sudo firewall-cmd --reload
[sudo] password for it5:
success
[it5@web ~]$ sudo cat /etc/hosts
10.1.2.12     site_nul_tp2
```
