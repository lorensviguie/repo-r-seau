# TP reseaux 3

## I.ARP

### 1.Echange ARP
 on ping une machine avec l'autre 

        [it5@localhost ~]$ ping 10.3.1.11
        PING 10.3.1.11 (10.3.1.11) 56(84) bytes of data.
        64 bytes from 10.3.1.11: icmp_seq=1 ttl=64 time=0.719 ms
 table arp de john

        [it5@localhost ~]$ ip neigh show
        10.3.1.12 dev enp0s9 lladdr 08:00:27:92:63:5d STALE
        10.3.1.1 dev enp0s9 lladdr 0a:00:27:00:00:3a STALE
 table arp de marcel

        [it5@localhost ~]$ ip neigh show
        10.3.1.1 dev enp0s9 lladdr 0a:00:27:00:00:3a DELAY
        10.3.1.11 dev enp0s9 lladdr 08:00:27:10:cf:7a STALE

 l'adresse mac de marcel est  08:00:27:92:63:5d 
 l'adresse mac de John   est  08:00:27:10:cf:7a

 preuve de la mac  de Marcel

        [it5@localhost ~]$ ip neigh show 10.3.1.12
        10.3.1.12 dev enp0s9 lladdr 08:00:27:92:63:5d STALE

preuve de la mac de john

        [it5@localhost ~]$ ip neigh show 10.3.1.11
        10.3.1.11 dev enp0s9 lladdr 08:00:27:10:cf:7a STALE

### 2.Echange de trames 
je t'epargne le resultat de la commande 

        sudo tcpdump -i enp0s9 -c 10 -w capturesharktp3trames.pcap

sudo ip neigh flush all sur les deux machines 
les deux table arp contiennent juste le chemin vers la carte reseaux 

        [it5@localhost ~]$ ip neigh show
        10.3.1.1 dev enp0s9 lladdr 0a:00:27:00:00:3a DELAY

apres un ping vers marcel une nouvelle ligne apparait le chemin vers le pc de marcel

        [it5@localhost ~]$ ip neigh show
        10.3.1.12 dev enp0s9 lladdr 08:00:27:92:63:5d REACHABLE
        10.3.1.1 dev enp0s9 lladdr 0a:00:27:00:00:3a REACHABLE


## II.Routegage

### 1.Mise en place du routage 
        [it5@localhost ~]$ sudo firewall-cmd --get active-zone
        public
         interfaces: enp0s9 enp0s10
les autres commandes affiche juste succes

je crée une route dans marcel pour ping jhon 

        [it5@localhost network-scripts]$ ip route show
        10.3.1.11 via 10.3.2.254 dev enp0s9 proto static metric 100

je ping jhon avec marcel 

        [it5@localhost network-scripts]$ ping 10.3.1.11
        PING 10.3.1.11 (10.3.1.11) 56(84) bytes of data.
        64 bytes from 10.3.1.11: icmp_seq=1 ttl=63 time=0.653 ms
        64 bytes from 10.3.1.11: icmp_seq=2 ttl=63 time=0.773 ms
        --- 10.3.1.11 ping statistics ---
        2 packets transmitted, 2 received, 0% packet loss, time 1055ms
        rtt min/avg/max/mdev = 0.653/0.713/0.773/0.060 ms

### 2.Analyse des trames


| ordre | type trame  | IP source | MAC source              | IP destination | MAC destination            |
|-------|-------------|-----------|-------------------------|----------------|----------------------------|
| 1     | Requête ARP |           | 08:00:27:92:63:5d       | Broadcast      | ff:ff:ff:ff:ff:ff          |
| 2     | Réponse ARP | x         | 08:00:27:87:97:db       | pcsCompu_87:97:db | 08:00:27:92:63:5d       |
| ...   | ...         | ...       | ...                     |                |                            |
| 3     | Ping        | 10.3.2.12 |  08:00:27:92:63:5d      | 10.3.1.11      | 08:00:27:87:97:db                     |
| 4     | Pong        | 10.3.1.11 | 08:00:27:87:97:db       | 10.3.2.12      | 08:00:27:92:63:5d                           |

### 3.accés a internet 

on ecrit dans le fichier networrk qui est dans /etc/sysconfig/
pour jhon

        GATEWAY=10.3.1.254

pour marcel 

        GATEWAY=10.3.2.254

je peux ping google 

        [it5@localhost sysconfig]$ ping 8.8.8.8
        PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
        64 bytes from 8.8.8.8: icmp_seq=1 ttl=112 time=21.4 ms

        --- 8.8.8.8 ping statistics ---
        1 packets transmitted, 1 received, 0% packet loss, time 0ms
        rtt min/avg/max/mdev = 21.430/21.430/21.430/0.000 ms

        [it5@localhost sysconfig]$ ping google.com
        PING google.com (142.250.74.238) 56(84) bytes of data.
        64 bytes from par10s40-in-f14.1e100.net (142.250.74.238): icmp_seq=1 ttl=247 time=21.3 ms

| ordre | type trame  | IP source | MAC source              | IP destination | MAC destination            |
|-------|-------------|-----------|-------------------------|----------------|----------------------------|
| 1     | Ping        | 10.3.1.11 | 08:00:27:10:cf:7a       | 8.8.8.8        | 08:00:27:ab:ec:20          |
| 2     | Pong        | 8.8.8.8   | 08:00:27:ab:ec:20       | 10.3.1.11      | 08:00:27:10:cf:7a          |


## III.DHCP

### 1.Mise en place du serveur DHCP

creation d'un serveur dhcp sur jhon 
        [it5@localhost ~]$ sudo cat /etc/dhcp/dhcpd.conf
        [sudo] password for it5:

        default-lease-time 900;
        max-lease-time 10800;

        authoritative;

        subnet 10.3.1.0 netmask 255.255.255.0 {
                range dynamic-bootp 10.3.1.10 10.3.1.253;
                option broadcast-address 10.3.1.254;
                option subnet-mask 255.255.255.0;
   
on dit a bob comment il va recuperer son ip 

        [it5@localhost etc]$ sudo cat /etc/sysconfig/network-scripts/ifcfg-enp0s9
        [sudo] password for it5:

        DEVICE=enp0s9

        BOOTPROTO=dhcp
        ONBOOT=yes

adresse ip de bob 
        
        inet 10.3.1.10/24

bob qui ping la passerelle 

        [it5@localhost etc]$ ping 10.3.1.254
        PING 10.3.1.254 (10.3.1.254) 56(84) bytes of data.
        64 bytes from 10.3.1.254: icmp_seq=1 ttl=64 time=0.293 ms
        64 bytes from 10.3.1.254: icmp_seq=2 ttl=64 time=0.415 ms

on reinitialise l'ip de bob 

        [it5@localhost etc]$ sudo nmcli con reload
        [it5@localhost etc]$ sudo nmcli con up "System enp0s9"
        Connection successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/2)
        [it5@localhost etc]$ sudo systemctl restart NetworkManager

il peut ping sa passerelle 

        [it5@localhost etc]$ ping 10.3.1.254
        PING 10.3.1.254 (10.3.1.254) 56(84) bytes of data.
        64 bytes from 10.3.1.254: icmp_seq=1 ttl=64 time=0.666 ms

ca route par default est 1.1.1.1

        [it5@localhost ~]$ ping 1.1.1.1
        PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
        64 bytes from 1.1.1.1: icmp_seq=1 ttl=53 time=21.5 ms

on teste avec notre route 

        [it5@localhost ~]$ dig google.com

        ; <<>> DiG 9.16.23-RH <<>> google.com
        ;; global options: +cmd
        ;; Got answer:
        ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 39076
        ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

        ;; OPT PSEUDOSECTION:
        ; EDNS: version: 0, flags:; udp: 512
        ;; QUESTION SECTION:
        ;google.com.                    IN      A

        ;; ANSWER SECTION:
        google.com.             275     IN      A       216.58.214.78

        ;; Query time: 27 msec
        ;; SERVER: 8.8.8.8#53(8.8.8.8)
        ;; WHEN: Fri Oct 28 11:42:52 CEST 2022
        ;; MSG SIZE  rcvd: 55

on ping google.com

        [it5@localhost ~]$ ping google.com
        PING google.com (216.58.214.78) 56(84) bytes of data.
        64 bytes from fra15s10-in-f14.1e100.net (216.58.214.78): icmp_seq=1 ttl=112 time=21.8 ms

### 2.Analyse de trames

l'IP fournit par le serveur DHCP au client et 10.3.1.146 
l'adresse de la passerelle est 10.3.1.254
l'adresse du serveur DHCP est 10.3.1.11