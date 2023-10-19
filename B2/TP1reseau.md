# TP reseaux 1 B2

# I.Basics

### ☀️ Carte réseau WiFi

``` powershell
C:\Users\33603>ipconfig /all
[...]
Adresse physique . . . . . . . . . . . : 58-6C-25-7F-A6-16
Adresse IPv4. . . . . . . . . . . . . .: 172.20.10.3
Masque de sous-réseau. . . . . . . . . : 255.255.255.240 | /28
```
adresse Mac = ```58-6C-25-7F-A6-16```
adresse Ip = ```172.20.10.3```
Masque de sous reseau / Notation CIDR = ```255.255.255.240``` / ```28```

### ☀️ Déso pas déso

Basé sur la commande au dessus.

l'adresse de réseau du LAN = ```172.20.10.0 ```   
l'adresse du broadcast = ```172.20.10.15```   
nombre d'ip possible = ```14```   

### ☀️ Hostname

```powershell
C:\Users\33603>hostname
LAPTOP-VPED60LK
```

### ☀️ Passerelle du réseau

```powershell
C:\Users\33603>ipconfig /all
   Masque de sous-réseau. . . . . . . . . : 255.255.255.240
   Bail obtenu. . . . . . . . . . . . . . : jeudi 12 octobre 2023 15:44:36
   Bail expirant. . . . . . . . . . . . . : vendredi 13 octobre 2023 16:13:26
   Passerelle par défaut. . . . . . . . . : fe80::b440:a4ff:fe66:7d64%17
                                       172.20.10.1
   Serveur DHCP . . . . . . . . . . . . . : 172.20.10.1

   C:\Users\33603>arp -a   
   Interface : 172.20.10.3 --- 0x11
  Adresse Internet      Adresse physique      Type
  172.20.10.1           b6-40-a4-66-7d-64     dynamique
  172.20.10.15          ff-ff-ff-ff-ff-ff     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique

```

l'adresse IP de la passerelle du réseau =  ```172.20.10.1```    
l'adresse MAC de la passerelle du réseau = ```b6-40-a4-66-7d-64 ```   


### ☀️ Serveur DHCP et DNS

```powershell
C:\Users\33603>ipconfig /all
Serveur DHCP . . . . . . . . . . . . . : 172.20.10.1    
   Serveurs DNS. . .  . . . . . . . . . . : fe80::b440:a4ff:fe66:7d64%17
                                       172.20.10.1
```

l'adresse IP du serveur DHCP qui vous a filé une IP = ```172.20.10.1 ```  
l'adresse IP du serveur DNS que vous utilisez quand vous allez sur internet = ```172.20.10.1```   


### ☀️ Table de routage
```powershell
===========================================================================

IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0      172.20.10.1      172.20.10.3     55
```

# II. Go further


### ☀️ Hosts ?
```powershell
C:\>cd Windows\System32\drivers\etc
C:\Windows\System32\drivers\etc>notepad hosts

192.168.56.131 web.tp5.linux
192.168.56.132 www.nextcloud.tp6
1.1.1.1 b2.hello.vous


C:\Windows\System32\drivers\etc>ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=50 ms TTL=59
Réponse de 1.1.1.1 : octets=32 temps=61 ms TTL=59
```

### ☀️ Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...

l'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo 
13.107.6.158

le port du serveur auquel vous êtes connectés 
au port  443

le port que votre PC a ouvert en local pour se connecter au port du serveur distant 
50282

### ☀️ Requêtes DNS 


à quelle adresse IP correspond le nom de domaine www.ynov.com
```powershell
C:\Users\33603>nslookup www.ynov.com
Serveur :   livebox.home
Address:  

Réponse ne faisant pas autorité :
Nom :    www.ynov.com
Addresses:  2606:4700:20::681a:ae9
          2606:4700:20::681a:be9
          2606:4700:20::ac43:4ae2
          104.26.10.233
          104.26.11.233
          172.67.74.226
```
à quel nom de domaine correspond l'IP 174.43.238.89
```powershell
C:\Users\33603>nslookup -type=PTR 174.43.238.89
Serveur :   livebox.home
Address:  

Réponse ne faisant pas autorité :
89.238.43.174.in-addr.arpa      name = 89.sub-174-43-238.myvzw.com
```

### ☀️ Hop hop hop

```powershell
C:\Users\33603>nslookup -q=ns www.ynov.com
Serveur :   livebox.home
Address:  2a01:cb19:ce4:2d00:46d4:54ff:fe25:5680

ynov.com
        primary name server = algin.ns.cloudflare.com
        responsible mail addr = dns.cloudflare.com
        serial  = 2322597658
        refresh = 10000 (2 hours 46 mins 40 secs)
        retry   = 2400 (40 mins)
        expire  = 604800 (7 days)
        default TTL = 1800 (30 mins)

C:\Users\33603>nslookup www.ynov.com algin.ns.cloudflare.com
Serveur :   algin.ns.cloudflare.com
Address:  2a06:98c1:50::ac40:213d

Nom :    www.ynov.com
Addresses:  2606:4700:20::ac43:4ae2
          2606:4700:20::681a:ae9
          2606:4700:20::681a:be9
          104.26.11.233
          104.26.10.233
          172.67.74.226
```
elle passe par une machine 

### ☀️ IP publique

```powershell
C:\Users\33603>nslookup myip.opendns.com resolver1.opendns.com
Serveur :   dns.opendns.com
Address:  2620:119:35::35

Nom :    myip.opendns.com
Address:  2a01:cb19:ce4:2d00:c8ea:13:155c:355a
```
### ☀️ Scan réseau
combien il y a de machines dans le LAN auquel vous êtes connectés 
```powershell
C:\Users\loren>for /L %i in (1,1,254) do @ping -n 1 -w 1 192.168.1.%i | find "Réponse"
Réponse de 192.168.1.1 : octets=32 temps<1ms TTL=64
Réponse de 192.168.1.11 : octets=32 temps=128 ms TTL=32
Réponse de 192.168.1.12 : octets=32 temps=4 ms TTL=64
Réponse de 192.168.1.13 : octets=32 temps=220 ms TTL=64
Réponse de 192.168.1.17 : octets=32 temps<1ms TTL=128
Réponse de 192.168.1.21 : octets=32 temps=8 ms TTL=64
Réponse de 192.168.1.22 : octets=32 temps<1ms TTL=64
Réponse de 192.168.1.25 : octets=32 temps=129 ms TTL=64
Réponse de 192.168.1.26 : octets=32 temps=287 ms TTL=128
Réponse de 192.168.1.27 : octets=32 temps=9 ms TTL=64
Réponse de 192.168.1.29 : octets=32 temps=237 ms TTL=64
^C^C
C:\Users\loren>
```
il y a 11 machine connecter dans mon lan. 

# III. Le requin

### ☀️ Capture ARP
[capturez un échange ARP entre votre PC et la passerelle du réseau](./tramewirehsark/arp.pcapng)
filtre arp 

### ☀️ Capture DNS 
[capturez une requête DNS vers le domaine de votre choix et la réponse](./tramewirehsark/dns.pcapng) filtre dns

```powershell
C:\Users\33603>ping www.ynov.com
Envoi d’une requête 'ping' sur www.ynov.com [2606:4700:20::681a:be9] avec 32 octets de données :
Réponse de 2606:4700:20::681a:be9 : temps=20 ms
Réponse de 2606:4700:20::681a:be9 : temps=16 ms
Réponse de 2606:4700:20::681a:be9 : temps=17 ms
Réponse de 2606:4700:20::681a:be9 : temps=18 ms

Statistiques Ping pour 2606:4700:20::681a:be9:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 16ms, Maximum = 20ms, Moyenne = 17ms
```

### ☀️ Capture TCP 

```powershell
$ ssh debian@162.19.65.43
Enter passphrase for key '/c/Users/33603/.ssh/id_rsa':
Linux vps-e4031a08 6.1.0-10-cloud-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.38-2 (2023-07-27) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Oct 19 08:22:26 2023 from 83.192.198.80
debian@vps-e4031a08:~$
```
[effectuez une connexion qui sollicite le protocole TCP](./tramewirehsark/tcp.pcapng) filtre tcp

