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

w