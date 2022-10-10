# TP Reseaux 2

## I.Setup Ip

on utilise la comande netsh pour changer nos parametres reseaux dans le terminal 

netsh interface ipv4 set adress name="Wi-Fi" static adresse ip voulu masque de sous reseau et et le broadcast

        netsh interface ipv4 show config

    Configuration pour l'interface « Ethernet »
        DHCP activé :                         Non
       Adresse IP :                           10.10.10.127
       Préfixe de sous-réseau :               10.10.8.0/22 (masque 255.255.252.0)
       Passerelle par défaut :               10.10.8.0
       Métrique de passerelle :              1
       Métrique de l'interface :             25
       Serveurs DNS configurés statiquement : 8.8.8.8
       Enregistrer avec le suffixe :           Principale uniquement
       Serveurs WINS configurés statiquement : Aucun

nos deux adresse ip sont 10.10.10.2 et 10.10.10.127
l'adresse reseaux 10.10.8.0
l'adresse broadcast 10.10.11.255


        PS C:\Windows\system32> ping 10.10.10.2

        Envoi d’une requête 'Ping'  10.10.10.2 avec 32 octets de données :
        Réponse de 10.10.10.2 : octets=32 temps=1 ms TTL=64


pour le ping c'est un type 8(echo (ping)request) qui est envoyé 
pour le pong c'est un type 0 (echo (ping)reply) qui est envoyé 

## II.ARP my bro

on utilise arp -a pour afficher l'ensemble de la talbe arp (pour des raison de lisibilite je la mets pas)
grace a cette comande j'ai trouvé l'addresse mac de mon partenaire 
         
          10.10.10.2            50-a0-30-02-ef-59     dynamique

et pour la gateway sur le reseaux Ynov  toujours grace a arp -a

        10.33.19.254          00-c0-e7-e0-04-4e     dynamique

grace a arp -d on peut supprimer des elements de la table arp

Arp -a

        PS C:\Windows\system32> arp -a

        Interface : 10.10.10.127 --- 0x3
            Adresse Internet      Adresse physique      Type
            10.10.10.2            50-a0-30-02-ef-59     dynamique
            10.10.11.255          ff-ff-ff-ff-ff-ff     statique
            224.0.0.22            01-00-5e-00-00-16     statique
            224.0.0.251           01-00-5e-00-00-fb     statique
            224.0.0.252           01-00-5e-00-00-fc     statique
            239.255.255.250       01-00-5e-7f-ff-fa     statique

        Interface : 192.168.56.1 --- 0xf
            Adresse Internet      Adresse physique      Type
            192.168.56.255        ff-ff-ff-ff-ff-ff     statique
            224.0.0.22            01-00-5e-00-00-16     statique
            224.0.0.251           01-00-5e-00-00-fb     statique
            224.0.0.252           01-00-5e-00-00-fc     statique
            239.255.255.250       01-00-5e-7f-ff-fa     statique
            255.255.255.255       ff-ff-ff-ff-ff-ff     statique

        Interface : 10.33.17.0 --- 0x10
            Adresse Internet      Adresse physique      Type
            10.33.19.254          00-c0-e7-e0-04-4e     dynamique
            10.33.19.255          ff-ff-ff-ff-ff-ff     statique
            224.0.0.2             01-00-5e-00-00-02     statique
            224.0.0.22            01-00-5e-00-00-16     statique
            224.0.0.251           01-00-5e-00-00-fb     statique
            224.0.0.252           01-00-5e-00-00-fc     statique
            239.255.255.250       01-00-5e-7f-ff-fa     statique
            255.255.255.255       ff-ff-ff-ff-ff-ff     statique
arp -d
            PS C:\Windows\system32> arp -a

        Interface : 10.10.10.127 --- 0x3
            Adresse Internet      Adresse physique      Type
            224.0.0.22            01-00-5e-00-00-16     statique
            239.255.255.250       01-00-5e-7f-ff-fa     statique

        Interface : 192.168.56.1 --- 0xf
            Adresse Internet      Adresse physique      Type
            224.0.0.22            01-00-5e-00-00-16     statique
            239.255.255.250       01-00-5e-7f-ff-fa     statique

        Interface : 10.33.17.0 --- 0x10
            Adresse Internet      Adresse physique      Type
            10.33.19.254          00-c0-e7-e0-04-4e     dynamique
            224.0.0.2             01-00-5e-00-00-02     statique
            224.0.0.22            01-00-5e-00-00-16     statique
            239.255.255.250       01-00-5e-7f-ff-fa     statique

on constate que plein d'adresse on été suprimer notament celle qui commence par 224

quand je ping 8.8.8.8 on constante que en effets des ip sont réaparue 

        224.0.0.2             01-00-5e-00-00-02     statique
        224.0.0.22            01-00-5e-00-00-16     statique
        224.0.0.251           01-00-5e-00-00-fb     statique
        224.0.0.252           01-00-5e-00-00-fc     statique
pour le ping 
l'adresse source c'est la mac de celui qui ping et la destination qui repond c'est la mac de celui qui a l'IP de celui que j'ai ping 
le pong renvoyer provient de l'adresse mac de celui que j'ai ping et a destination de l'adresse mac de celui qui a ping 

# II.5 Interlude hackerzz

# III. DHCP you too my brooo

on definit un ip static donc plus de dhcp avec

    netsh interface ip set address name="Wi-Fi" static 10.33.19.254 255.255.255.0
puis on reactive le dhcp avec

    netsh interface ip set adress name="Wi-Fi" dhcp


