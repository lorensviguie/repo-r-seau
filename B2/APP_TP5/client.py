import socket
import sys
import re
import logging
import json
# On définit la destination de la connexion
host = '10.33.67.166'  # IP du serveur
port = 13337               # Port choisir par le serveur

class CustomFormatter(logging.Formatter):

    red = "\x1b[31;20m"
    reset = "\x1b[0m"
    
    FORMATS = {
        logging.ERROR: red + "%(levelname)s %(asctime)s %(message)s" + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno) 
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)




try:
    # Create a custom logger
    logger = logging.getLogger("bs_server")
    logger.setLevel(logging.DEBUG)  # This needs to be DEBUG to capture all levels of logs

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('./B2/APP_TP5/bs_client.log')
    c_handler.setLevel(logging.ERROR)  # Set to DEBUG to ensure all levels are logged to console
    f_handler.setLevel(logging.DEBUG)  # Set to DEBUG to ensure all levels are logged to file

    # Create formatters and add it to handlers
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    c_handler.setFormatter(CustomFormatter())
    f_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
except Exception as e:
    print(f"Failed to configure logging: {e}")
    sys.exit(1)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    logger.info("Connexion réussie à %s:%s", host, port)
    
    userMessage = input("Veuillez saisir une opération arithmétique : ")

    pattern = r'^(-?\d{1,5})\s*([+*-])\s*(-?\d{1,5})$'

    match= re.match(pattern, userMessage)
    if match:
        num1, operator, num2 = match.groups()
        num1, num2 = int(num1), int(num2)

        # Vérifiez si les nombres sont dans la plage [-100000, 100000]
        if -100000 <= num1 <= 100000 and -100000 <= num2 <= 100000:
            s.sendall(userMessage.encode("utf-8"))
            logger.info("Message envoyé au serveur %s : %s", host, userMessage)
        else:
            raise ValueError("l'opération autorisée n'accepte que des nombres entiers compris entre -100000 et +100000")
    else:
        raise ValueError("l'opération autorisée n'accepte que les signes suivants (-,+,*) et des nombres entiers compris entre -100000 et +100000")
    
    data = s.recv(1024)
    s.close()
    logger.info(f"Réponse reçue du serveur {host} : {repr(data)}")
    sys.exit(0)
   # Assurez-vous que le socket est fermé même en cas d'erreur
except socket.error as e :
    logger.error("Impossible de se connecter au serveur %s sur le port %s", host, port)
    s.close()
    sys.exit(1)
# Close the connection.

