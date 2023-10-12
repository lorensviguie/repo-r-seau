# TP reseaux 4

# I.First Step

### Master Duel

c'est l'ip 54.249.176.254 sur le port 443  
le port local que mon pc a ouvert c'est 65324  
[Capture master duel ](./TP4ReseauxWireshark/Capture%20Master%20duel.pcapng)
```powershell
PS C:\Users\33603> netstat -n

Connexions actives

  Proto  Adresse locale         Adresse distante       État
  TCP    10.33.18.174:49290     54.168.119.58:443      ESTABLISHED
```
### Fall Guys update 

c'est l'ip 13.225.22.34 sur le port 80   
le port local que mon pc a ouvert est 49339  
[capture Fall Guys](./TP4ReseauxWireshark/Capture%20updatefallguys.pcapng)  
```powershell 
PS C:\Users\33603> netstat -n

Connexions actives

Proto  Adresse locale         Adresse distante       État
TCP    10.33.18.174:49335     13.225.22.34:80        ESTABLISHED  
TCP    10.33.18.174:49336     13.225.22.34:80        ESTABLISHED  
TCP    10.33.18.174:49337     13.225.22.34:80        ESTABLISHED  
TCP    10.33.18.174:49338     13.225.22.34:80        ESTABLISHED  
TCP    10.33.18.174:49339     13.225.22.34:80        ESTABLISHED  
```
### Daylimotion 
c'est l'ip 188.65.126.247 sur le port 443   
le port local que mon pc a ouvert est 49932  
[capture daylimotion](./TP4ReseauxWireshark/Capture%20Daylimotion.pcapng)
```powershell
PS C:\Users\33603> netstat -n

Connexions actives

Proto  Adresse locale         Adresse distante       État
TCP    10.33.18.174:49962     188.65.126.247:443     ESTABLISHED 
```

### Discord

c'est l'ip 35.214.72 sur le port 50002   
le port local que mon pc a ouvert est 55324  
[capture daylimotion](./TP4ReseauxWireshark/Discord.pcapng)

```powershell
$ netstat -n -b -a -p udp  | grep Discord -B 1
  UDP    0.0.0.0:55324          *:*
 [Discord.exe]

```
### ynov extranet 

c'est l'ip 178.32.154.7 sur le port 443  
le port local que mon pc a ouvert est 65440  
[capture ynov extra](./TP4ReseauxWireshark/ynovextranet.pcapng)

```powershell
PS C:\Users\33603> netstat -n

Connexions actives

Proto  Adresse locale         Adresse distante       État
TCP    10.33.18.174:65441     178.32.154.7:443       ESTABLISHED
```

# II.Mise en place 

## 1.ssh

on utlise le protocole tcp car on se connecte via une authentification il faut donc que le mdp arrive dans le bonne ordre.  

[•Capture Wire shark SSH](./TP4ReseauxWireshark/SSH%20Capture%20(propre).pcapng)

```powershell

[it5@node1 ~]$ ss
Netid      State      Recv-Q      Send-Q                         Local Address:Port              Peer Address:Port       Process

tcp        ESTAB      0           0                                  10.4.1.11:ssh                   10.4.1.1:57053
```


# II.DNS

## 1.présentation

capture des fichiers de cat 


```c
sudo cat /etc/named.conf
//
// named.conf
//
// Provided by Red Hat bind package to configure the ISC BIND named(8) DNS
// server as a caching only nameserver (as a localhost DNS resolver only).
//
// See /usr/share/doc/bind*/sample/ for example named configuration files.
//

options {
        listen-on port 53 { 127.0.0.1; };
        listen-on-v6 port 53 { ::1; };
        directory       "/var/named";
        dump-file       "/var/named/data/cache_dump.db";
        statistics-file "/var/named/data/named_stats.txt";
        memstatistics-file "/var/named/data/named_mem_stats.txt";
        secroots-file   "/var/named/data/named.secroots";
        recursing-file  "/var/named/data/named.recursing";
        allow-query     { localhost; };
        allow-query-cache { localhost; any; };

        /*
         - If you are building an AUTHORITATIVE DNS server, do NOT enable recursion.
         - If you are building a RECURSIVE (caching) DNS server, you need to enable
           recursion.
         - If your recursive DNS server has a public IP address, you MUST enable access
           control to limit queries to your legitimate users. Failing to do so will
           cause your server to become part of large scale DNS amplification
           attacks. Implementing BCP38 within your network would greatly
           reduce such attack surface
        */
        recursion yes;

        dnssec-validation yes;

        managed-keys-directory "/var/named/dynamic";
        geoip-directory "/usr/share/GeoIP";

        pid-file "/run/named/named.pid";
        session-keyfile "/run/named/session.key";

        /* https://fedoraproject.org/wiki/Changes/CryptoPolicy */
        include "/etc/crypto-policies/back-ends/bind.config";
};

logging {
        channel default_debug {
                file "data/named.run";
                severity dynamic;
        };
};

zone "tp4.b1" IN {
     type master;
     file "tp4.b1.db";
     allow-update { none; };
     allow-query {any; };
};

zone "1.4.10.in-addr.arpa" IN {
     type master;
     file "tp4.b1.rev";
     allow-update { none; };
     allow-query { any; };
};

```

```c
sudo /var/named/tp4.b1.rev


$TTL 86400
@ IN SOA dns-server.tp4.b1. admin.tp4.b1. (
    2019061800 ;Serial
    3600 ;Refresh
    1800 ;Retry
    604800 ;Expire
    86400 ;Minimum TTL
)

; Infos sur le serveur DNS lui même (NS = NameServer)
@ IN NS dns-server.tp4.b1.

;Reverse lookup for Name Server
201 IN PTR dns-server.tp4.b1.
11 IN PTR node1.tp4.b1.
```

```c
sudo cat /var/named/.db

$TTL 86400
@ IN SOA dns-server.tp4.b1. admin.tp4.b1. (
    2019061800 ;Serial
    3600 ;Refresh
    1800 ;Retry
    604800 ;Expire
    86400 ;Minimum TTL
)

; Infos sur le serveur DNS lui même (NS = NameServer)
@ IN NS dns-server.tp4.b1.

; Enregistrements DNS pour faire correspondre des noms à des IPs
dns-server IN A 10.4.1.201
node1      IN A 10.4.1.11

```



### verification Named

```c
[it5@localhost etc]$ sudo systemctl status named
● named.service - Berkeley Internet Name Domain (DNS)
     Loaded: loaded (/usr/lib/systemd/system/named.service; enabled; vendor preset: disabled)
     Active: active (running) since Thu 2022-11-10 10:53:39 CET; 21min ago
   Main PID: 11150 (named)
      Tasks: 4 (limit: 5905)
     Memory: 17.0M
        CPU: 38ms
     CGroup: /system.slice/named.service
             └─11150 /usr/sbin/named -u named -c /etc/named.conf

Nov 10 10:53:39 localhost.localdomain named[11150]: configuring command channel from '/etc/rndc.key'
Nov 10 10:53:39 localhost.localdomain named[11150]: command channel listening on 127.0.0.1#953
Nov 10 10:53:39 localhost.localdomain named[11150]: configuring command channel from '/etc/rndc.key'
Nov 10 10:53:39 localhost.localdomain named[11150]: command channel listening on ::1#953
Nov 10 10:53:39 localhost.localdomain named[11150]: managed-keys-zone: loaded serial 0
Nov 10 10:53:39 localhost.localdomain named[11150]: zone 1.4.10.in-addr.arpa/IN: loaded serial 2019061800
Nov 10 10:53:39 localhost.localdomain named[11150]: zone tp4.b1/IN: loaded serial 2019061800
Nov 10 10:53:39 localhost.localdomain named[11150]: all zones loaded
Nov 10 10:53:39 localhost.localdomain systemd[1]: Started Berkeley Internet Name Domain (DNS).
Nov 10 10:53:39 localhost.localdomain named[11150]: running
```

### On ecoute sur les port

```c
[it5@localhost etc]$ sudo ss -tulpn
Netid      State       Recv-Q      Send-Q           Local Address:Port           Peer Address:Port      Process

udp                      UNCONN                    0                         0    127.0.0.1:53            0.0.0.0:*                        users:(("named",pid=11150,fd=16))

udp                      UNCONN                    0                         0   [::1]:53               [::]:*                        users:(("named",pid=11150,fd=19))
tcp                      LISTEN                    0                         10  127.0.0.1:53          0.0.0.0:*                        users:(("named",pid=11150,fd=17))

tcp                      LISTEN                    0                         4096  127.0.0.1:953        0.0.0.0:*                        users:(("named",pid=11150,fd=22))
tcp                      LISTEN                    0                         10  [::1]:53              [::]:*                        users:(("named",pid=11150,fd=21))


```

### config firewall4

```c

[it5@localhost etc]$ sudo firewall-cmd --add-port=57599/tcp --permanent
success

[it5@localhost ~]$ sudo firewall-cmd --reload
[sudo] password for it5:
success

```

on teste sur notre serveur dns marche   

le client vers le DNS
```c
[it5@node1 ~]$ dig server-dns-tp4.b1

; <<>> DiG 9.16.23-RH <<>> server-dns-tp4.b1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 29454
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;server-dns-tp4.b1.             IN      A

;; AUTHORITY SECTION:
.                       80965   IN      SOA     a.root-servers.net. nstld.verisign-grs.com. 2022111300 1800 900 604800 86400

;; Query time: 28 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Thu Nov 10 11:56:36 CET 2022
;; MSG SIZE  rcvd: 121


```

le client vers le client 
```c
[it5@node1 ~]$ dig node1.tp4.b1

; <<>> DiG 9.16.23-RH <<>> node1.tp4.b1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 48299
;; flags: qr rd ra ad; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;node1.tp4.b1.                  IN      A

;; AUTHORITY SECTION:
.                       86319   IN      SOA     a.root-servers.net. nstld.verisign-grs.com. 2022111300 1800 900 604800 86400

;; Query time: 28 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Thu Nov 10 11:55:24 CET 2022
;; MSG SIZE  rcvd: 116


```c
[it5@node1 ~]$ dig google.com

; <<>> DiG 9.16.23-RH <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 64279
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;google.com.                    IN      A

;; ANSWER SECTION:
google.com.             36      IN      A       216.58.214.78

;; Query time: 21 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Thu Nov 10 11:57:23 CET 2022
;; MSG SIZE  rcvd: 55

```

pour la derniere partie c'est un fait 

[trame dns request](./TP4ReseauxWireshark/Dns%20request%20failed.pcapng)
