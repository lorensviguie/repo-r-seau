# TP Reseaux 1


## I: Exploration local en solo

1. Affichage d'informations sur la pile TCP/IP locale
    ipconfig /all
    Carte réseau sans fil Wi-Fi : 
    Adresse physique . . . . . . . . . . . : 58-6C-25-7F-A6-16
    Adresse IPv4. . . . . . . . . . . . . .: 10.33.16.213(préféré)
    
    Carte Ethernet Ethernet : 
    Adresse physique . . . . . . . . . . . : 08-8F-C3-0A-24-53
    j'ai pas d'adresse IP
    
    ipconfig /all
    Passerelle par défaut. . . . . . . . . : 10.33.19.254
    
    arp -a
    10.33.19.254          00-c0-e7-e0-04-4e     dynamique
    
    on ouvre le panneau de configuration reeau internet et centre reseau 
    ![](https://i.imgur.com/leLKch2.png)
2. Modifications des informations
    pour modifer son adresse ip panneau de config on va dans centre Reseau et partage on choisit notre carte wifi et on va modifier les proprietés et on modifie le protocole de version 4
    
    j'ai perdu internet car l'adresse ip que j'ai rentré a dut etre utiliser pas quelqun d'autre 
         Adresse IPv4. . . . . . . . . . . . . .: 10.33.16.127
         Adresse IPv4. . . . . . . . . . . . . .: 10.33.16.213(préféré)
     
## II. Exploration locale en duo

3. Modification d'adresse IP

    on a rentré tout les deux la meme adresse ip soit 10.10.10.127 mais cette     fois ci sur le port ethernet et pas la carte reseaux 
    
        Carte Ethernet Ethernet : 
         Adresse IPv4. . . . . . . . . . . . . .: 10.10.10.127(préféré)
 
 
       PS C:\Users\33603> ping 10.10.10.227
        Envoi d’une requête 'Ping'  10.10.10.227 avec 32 octets de données :
        Réponse de 10.10.10.127 : octets=32 temps<1ms TTL=128
  
      voila l'addresse mac  de mon partenaire 
         10.10.10.227          04-42-1a-89-b3-1a     dynamique

4. Utilisation d'un des deux comme gateway
    
        PS C:\Users\33603> ping 8.8.8.8

        Envoi d’une requête 'Ping'  8.8.8.8 avec 32 octets de données :
        Réponse de 8.8.8.8 : octets=32 temps=57 ms TTL=113
        
        PS C:\Users\33603> tracert 10.10.10.227

        Détermination de l’itinéraire vers PC-Samy [10.10.10.227]
        avec un maximum de 30 sauts :

          1     1 ms     1 ms     1 ms  PC-Samy [10.10.10.227]

5. Petit Chat Privé


    sur le pc client 
    
         PS C:\Users\33603\Downloads\netcat-1.11> .\nc.exe 10.10.10.227 8888
         ping
            pong
    
    sur le pc serveur 
    
         PS C:\Users\samyd\OneDrive\Bureau\netcat-win32-1.11\netcat-1.11> .\nc.exe -l -p 8888
         pong
         ping

    pour verifier la connexion 

        PS C:\Windows\system32> netstat -a -n -b
        TCP    10.10.10.127:63479     10.10.10.227:8888      ESTABLISHED
        [nc.exe]
6. Firewall

    on va dans le panneau de configuration , systeme et securité , parefeu , parametre avancé , et on cherche partage de fichier et d'imprimante 
    domaine IPV4 et on active la regle dans le sortant et l'entrant .
    