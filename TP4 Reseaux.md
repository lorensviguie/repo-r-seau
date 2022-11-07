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

on utlise le protocole tcp car on se connecte via une authentification il faut donc que le mdp arrive dans le bonne ordre