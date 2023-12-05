import json
import subprocess
import time

def read_config(file_path):
    with open(file_path, 'r') as config_file:
        config_data = json.load(config_file)
    return config_data

def update_firewall(config):
    while True:
        for service, port in config.items():
            check_service_status = f'systemctl is-active {service}.service'
            service_running = subprocess.run(check_service_status, shell=True, stdout=subprocess.PIPE).stdout.decode().strip()

            if service_running == 'active':
                print(f"{service} is running. Opening port {port}.")
                open_port = f'firewall-cmd --add-port={port}/tcp --permanent'
                subprocess.run(open_port, shell=True)
            else:
                print(f"{service} is not running. Closing port {port}.")
                close_port = f'firewall-cmd --remove-port={port}/tcp --permanent'
                subprocess.run(close_port, shell=True)

        reload_firewall = 'firewall-cmd --reload'
        subprocess.run(reload_firewall, shell=True)

        time.sleep(5)

if __name__ == "__main__":
    config_file_path = 'firewall_config.json'
    firewall_config = read_config(config_file_path)
    update_firewall(firewall_config)
