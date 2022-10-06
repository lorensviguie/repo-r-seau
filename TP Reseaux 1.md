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

    pour definir un port particulier dans ces meme parametres sauf que dans les option des port on definit un port particulier ici 8888

    maintenant meme avec le pare feu  activer le ping marche mtn
         ping 1.1.1.1

        Envoi d’une requête 'Ping'  1.1.1.1 avec 32 octets de données :
        Réponse de 1.1.1.1 : octets=32 temps=49 ms TTL=54
        Réponse de 1.1.1.1 : octets=32 temps=44 ms TTL=54

    et le netcat marche aussi

        .\nc.exe 10.10.10.227 8888
        coucou
        le pountos

## III. Manipulations d'autres outils/protocoles côté client

1. DHCP
    toutes les informations sont obtenue grace a ipconfig /all

        Bail obtenu. . . . . . . . . . . . . . : jeudi 6 octobre 2022 08:52:54
        Bail expirant. . . . . . . . . . . . . : vendredi 7 octobre 2022 08:52:53
        Passerelle par défaut. . . . . . . . . : 10.33.19.254            
        Serveur DHCP . . . . . . . . . . . . . : 10.33.19.254

  2. DNS

 avec la commande nslookup c'est l'adresse 8.8.8.8 qui revient tout le temps c'est donc surement l'adresse dns que mon ordinateur utilise 
        
        nslookup www.ynov.com
        Serveur :   dns.google
        Address:  8.8.8.8

        Réponse ne faisant pas autorité :
        Nom :    www.ynov.com
        Addresses:  2606:4700:20::681a:ae9
             2606:4700:20::681a:be9
             2606:4700:20::ac43:4ae2
             172.67.74.226
             104.26.10.233
             104.26.11.233  

        nslookup google.com
        Serveur :   dns.google
        Address:  8.8.8.8

        Réponse ne faisant pas autorité :
        Nom :    google.com
        Addresses:  2a00:1450:4007:80f::200e
            216.58.209.238

## Wireshark

1. Intro Wireshark 

    je ping 10.10.10.227
    on cherche la ligne qui a été ping avec l'addresse 10.10.10.227

        179	87.494287	10.10.10.127	10.10.10.227	ICMP	74	Echo (ping) request  id=0x0001, seq=45/11520, ttl=128 (reply in 180)

    on lance le chat dans la barre de recherche on tape tcp.port== 8888
    et on obtient toutes les communication effectuer sur le port 8888 
    
        5	2.943657	10.10.10.127	10.10.10.227	TCP	59	55917 → 8888 [PSH, ACK] Seq=1 Ack=1 Win=1026 Len=5
        6	2.994243	10.10.10.227	10.10.10.127	TCP	60	8888 → 55917 [ACK] Seq=1 Ack=6 Win=8195 Len=0

    je ping Ynov.com
        
        103	14.742893	10.33.17.0	104.26.10.233	ICMP	74	Echo (ping) request  id=0x0001, seq=57/14592, ttl=128 (reply in 104)

2. Bonus : avant-goût TCP et UDP

    l'ip du serveur yt quand je regarde une video yt est 142.250.179.78
    et le port et 443