# TP5 : Intégration

## I. Tester

🌞 Récupérer l'application dans la VM hosting.tp5.b1  
[appPyton](./APP_TP5/server.py)  

🌞 Essayer de lancer l'app  
```powershell
C:\Users\33603\B1\repo-r-seau\B2\APP_TP5>scp -i C:\Users\33603\.ssh\id_rsa C:\Users\33603\B1\repo-r-seau\B2\APP_TP5\server.py it5@192.168.206.4:/home/it5/server.py
Enter passphrase for key 'C:/Users/33603/.ssh/id_rsa':
server.py                                                                                                                                                                                                  100% 4761     4.7MB/s   00:00
[it5@localhost log]$ sudo chown -R it5:it5 /var/log/bs_server
[it5@localhost /]$ sudo python3 /home/it5/server.py -p 1048
1048
Le serveur tourne sur 192.168.206.4:1048
[it5@localhost ~]$ ss -tuln | grep 1048
tcp   LISTEN 0      1      192.168.206.4:1048      0.0.0.0:*
```

🌞 Tester l'app depuis hosting.tp5.b1

```powershell
[it5@localhost /]$ cat /var/log/bs_client/bs_client.log

2023-11-28 14:44:23 INFO Connexion réussie à 192.168.206.4:1048
2023-11-28 14:44:29 INFO Message envoyé au serveur 192.168.206.4 : 3+3
2023-11-28 14:44:29 INFO Réponse reçue du serveur 192.168.206.4 : b'6'
2023-11-28 14:44:53 INFO Connexion réussie à 192.168.206.4:1048
2023-11-28 14:45:02 INFO Connexion réussie à 192.168.206.4:1048
2023-11-28 14:45:05 INFO Message envoyé au serveur 192.168.206.4 : 6-4
2023-11-28 14:45:05 INFO Réponse reçue du serveur 192.168.206.4 : b'2'

```

## II. Intégrer 

### 1. Environnement  

🌞 Créer un dossier /opt/calculatrice
```powershell
[it5@localhost calculatrice]$sudo cat /etc/passwd |grep calc
calc:x:1001:1001::/home/calc:/bin/nologin
[it5@localhost calculatrice]$sudo chown -R calc:calc /opt/calculatrice
[it5@localhost calculatrice]$ cat /etc/systemd/system/calculatrice.services
[Unit]
Description=Service pour l application Calc
After=network.target

[Service]
Type=simple
User=calc
ExecStart=/usr/bin/python /opt/calculatrice/server.py
Restart=on-always

[Install]
WantedBy=multi-user.target

[it5@localhost system]$ sudo ls -al /etc/systemd/system/ |grep calc
-rw-r-----. 1 root root  217 Nov 28 15:27 calculatrice.service
[it5@localhost system]$ ss -tuln |grep 1048
tcp   LISTEN 0      1      192.168.206.4:1048      0.0.0.0:*
[it5@localhost calculatrice]$ sudo python3 /home/it5/client.py
Veuillez saisir une opération arithmétique : 3+3
[it5@localhost calculatrice]$ cat /var/log/bs_client/bs_client.log
[...]
2023-11-28 15:36:31 INFO Message envoyé au serveur 192.168.206.4 : 3+3
2023-11-28 15:36:31 INFO Réponse reçue du serveur 192.168.206.4 : b'6'

```

## 2. systemd service

### B. Service basique
🌞 Créer le fichier /etc/systemd/system/calculatrice.service


[fichier.services calc](./APP_TP5/configcalc.services)

🌞 Tester que la politique de redémarrage fonctionne
```powershell
[it5@localhost system]$ sudo systemctl status calculatrice.service
     Loaded: loaded (/etc/systemd/system/calculatrice.service; enabled; preset: disabled)
     Active: active (running) since Tue 2023-11-28 15:46:36 CET; 2s ago
   Main PID: 2295 (python)
[it5@localhost system]$ sudo kill -9 2295
    Process: 2295 ExecStart=/usr/bin/python /opt/calculatrice/server.py (code=killed, signal=KILL)
[it5@localhost system]$ sudo systemctl status calculatrice.service
● calculatrice.service - Service pour l'application Calc
     Loaded: loaded (/etc/systemd/system/calculatrice.service; enabled; preset: disabled)
     Active: active (running) since Tue 2023-11-28 15:47:04 CET; 10s ago
```

➜ Firewall !  

🌞 Ouverture automatique du firewall dans le fichier calculatrice.service  
[fichier.services calc](./APP_TP5/configcalc.services)
```powershell
[it5@pc-148 ~]$ sudo cat /etc/sudoers | tail -n 2
%calc ALL=(ALL) NOPASSWD: /usr/bin/firewall-cmd --add-port=1048/tcp
%calc ALL=(ALL) NOPASSWD: /usr/bin/firewall-cmd --remove-port=1048/tcp

```
## 3. Monitoring

🌞 Installer Netdata sur hosting.tp5.b1
```powershell
[it5@pc-148 opt]$ sudo systemctl status netdata
● netdata.service - Real time performance monitoring
     Loaded: loaded (/usr/lib/systemd/system/netdata.service; enabled; preset: enabled)
     Active: active (running) since Tue 2023-11-28 20:28:04 CET; 2min 25s ago
[it5@localhost netdata]$ sudo firewall-cmd --list-all | grep ports
  ports: 19999/tcp 1048/tcp
[it5@pc-148 system]$ ss -tuln |grep 1999
tcp   LISTEN 0      4096   192.168.206.4:19999      0.0.0.0:*
```
🌞 Configurer une sonde TCP
```powershell
[it5@localhost netdata]$ sudo cat go.d/portcheck.conf | tail -n 9
update every: 20
jobs:
 - name: calculatrice
   host: 10.0.2.15
   ports: [1048]
[it5@localhost netdata]$sudo cat health_alarm_notify.conf
#------------------------------------------------------------------------------
# discord (discordapp.com) global notification options

SEND_DISCORD="YES"
DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/lewebhook"
DEFAULT_RECIPIENT_DISCORD="alerts"

```

🌞 Alerting Discord
```powershell
[it5@localhost ~]$ sudo cat /etc/netdata/go.d/portcheck.conf
update every: 20
jobs:
 - name: calculatrice
   host: 10.0.2.15
   ports: [1048]
```
## III. Héberger

### 1. Interface bridge 

### 2. Firewall

🌞 Assurez-vous qu'aucun port est inutilement ouvert

```powershell
[it5@pc-148 ~]$ sudo firewall-cmd --list-all | grep ports
  ports: 1048/tcp
  forward-ports:
  source-ports:
[it5@pc-148 ~]$
```

### 3. Serveur SSH

🌞 Conf serveur SSH
```powershell
[it5@pc-148 ~]$sudo nano /etc/ssh/sshd_config
[it5@pc-148 ~]$sudo cat /etc/ssh/sshd_config | grep ListenAddres
ListenAddress 192.168.206.4

[it5@pc-148 ~]$ ss -lnut | grep 22
tcp   LISTEN 0      128    192.168.206.4:22        0.0.0.0:*

```

### 4. Serveur Calculatrice

🌞 Conf serveur Calculatrice


ajout du fichier de conf [fichier de conf](./APP_TP5/conf.json)
```powershell
import json

def get_host_ip_from_json():
    try:
        with open('conf.json', 'r') as file:
            data = json.load(file)
            host_ip = data.get('Hostip', None)
            if host_ip is not None:
                return str(host_ip)
            else:
                return "Clé 'Hostip' non trouvée dans le fichier JSON."
    except FileNotFoundError:
        return "Fichier 'conf.json' non trouvé."
    except json.JSONDecodeError:
        return "Erreur de décodage JSON dans le fichier 'conf.json'."
    except Exception as e:
        return f"Erreur inattendue : {str(e)}"
[it5@pc-148 ~]$ ss -tulnp | grep 1048
tcp   LISTEN 0      1       192.168.1.35:1048      0.0.0.0:*

```