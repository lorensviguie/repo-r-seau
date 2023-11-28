# On importe la lib argparse
import argparse
import sys
import socket
import logging
import time
import threading
import json as js
# Création d'un objet ArgumentParser
parser = argparse.ArgumentParser()

# On ajoute la gestion de l'option -n ou --name
# "store" ça veut dire qu'on attend un argument à -n

# on va stocker l'argument dans une variable
parser.add_argument("-p", "--port", type=int, default=13337,
                    help="Usage: python bs_server.py [OPTION]..."
                    "Run a server"
                    "Mandatory arguments to long options are mandatory for short options too."
                    "-p, --port                  Specify the port for the server to run on."
                    "                            Ports are integer between 0 and 65535"
                    "                            Ports below 1025 are considered privileged."
                    "-h, --help                  Help of the command"
)

# Permet de mettre à jour notre objet ArgumentParser avec les nouvelles options
args = parser.parse_args()

#dur dur le fichier de conf 

def get_host_ip_from_json():
    try:
        with open('conf.json', 'r') as file:
            data = js.load(file)
            host_ip = data.get('Hostip', None)
            if host_ip is not None:
                return str(host_ip)
            else:
                return "Clé 'Hostip' non trouvée dans le fichier JSON."
    except FileNotFoundError:
        return "Fichier 'conf.json' non trouvé."
    except js.JSONDecodeError:
        return "Erreur de décodage JSON dans le fichier 'conf.json'."
    except Exception as e:
        return f"Erreur inattendue : {str(e)}"

print(args.port)

if (args.port < 0 or args.port> 65535):
    print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535).")
    sys.exit(1)
elif (args.port >= 0 and args.port<= 1024):
    print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024.")
    sys.exit(2)

class CustomFormatter(logging.Formatter):

    yellow = "\x1b[33;20m"
    reset = "\x1b[0m"

    FORMATS = {
        logging.WARNING: yellow + "%(levelname)s %(asctime)s %(message)s" + reset,
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
    f_handler = logging.FileHandler('/var/log/bs_server/bs_server.log')
    c_handler.setLevel(logging.DEBUG)  # Set to DEBUG to ensure all levels are logged to console
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

# SOCK_STREAM is the socket type for TCP, the protocol that will be used.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# On choisit une IP et un port où on va écouter
host = '192.168.206.4' # string vide signifie, dans ce conetxte, toutes les IPs de la machine
port = args.port # port choisi arbitrairement
# Bind the socket to the address and port number.
s.bind((host, port))

# Listen for incoming connections (with a backlog of 1).
s.listen(1)


logger.info("Le serveur tourne sur %s:%s", host, str(port))

# Function to check for last client connection
def check_last_client_connection():
    global last_client_time
    while True:
        time.sleep(60)  # Wait for one minute
        if time.time() - last_client_time > 60:
            logger.warning("Aucun client depuis plus de une minute.")

# Start the thread for checking the last client connection
check_thread = threading.Thread(target=check_last_client_connection)
check_thread.daemon = True  # Make sure the thread does not block program exit
check_thread.start()

# Main server loop
while True:
    try:
        #Accept a connection
        conn, addr = s.accept()
        last_client_time = time.time()  # Update the time of the last client connection
        logger.info("Un client %s s'est connecté.", addr)

        while True:
            # Receive data from the client
                data = conn.recv(1024)

                if not data:
                    break  # Exit the inner loop if no data is received

                # Decode the received data to a string
                message = data.decode('utf-8')
                logger.info("Le client %s a envoyé %s", addr, message)

                # Send a response to the client
                result = eval(message)
                messageServeur = str(result)
                conn.sendall(messageServeur.encode())
                logger.info("Réponse envoyée au client %s : %s.", addr, messageServeur)
    except socket.error as e:
        print(f"Socket error occurred: {e}")
        break

conn.close()
