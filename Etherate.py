import os
import subprocess
import getpass



query = "\033[34m<•> \033[0m" # Python print descriptions by The Spiral Of Powah
error = "\033[31m<X> \033[0m" # Python print descriptions by The Spiral Of Powah
triumph = "\033[32m<✓> \033[0m" # Python print descriptions by The Spiral Of Powah
info = "\033[36m<∘> \033[0m" # Python print descriptions by The Spiral Of Powah

def PsExec(command, username, password, port, ip):
    psexec_args = [
        "psexec.exe",
        f'\\\\{ip}',
        "-u",
        username,
        "-p",
        password,
        "-n",
        "30",
        "-accepteula",
        command,
    ]

    try:
        subprocess.check_call(psexec_args)
        print(f"{triumph}Hostname {ip}:{port} successfully executed {command} from args {psexec_args}")
    except subprocess.CalledProcessError as e:
        print(f"{error}Command '{command}' on {ip}:{port} failed with error: {e}")
    except Exception as e:
        print(f"{error}An unexpected error occurred: {e}")

os.system("cls")
print("""\033[34m   ▄████████     ███        ▄█    █▄       ▄████████    ▄████████    ▄████████     ███        ▄████████
\033[31m  ███    ███ ▀█████████▄   ███    ███     ███    ███   ███    ███   ███    ███ ▀█████████▄   ███    ███
\033[34m  ███    █▀     ▀███▀▀██   ███    ███     ███    █▀    ███    ███   ███    ███    ▀███▀▀██   ███    █▀ 
\033[31m ▄███▄▄▄         ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀   ███    ███     ███   ▀  ▄███▄▄▄    
\033[34m▀▀███▀▀▀         ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀███████████     ███     ▀▀███▀▀▀    
\033[31m  ███    █▄      ███       ███    ███     ███    █▄  ▀███████████   ███    ███     ███       ███    █▄ 
\033[34m  ███    ███     ███       ███    ███     ███    ███   ███    ███   ███    ███     ███       ███    ███
\033[31m  ██████████    ▄████▀     ███    █▀      ██████████   ███    ███   ███    █▀     ▄████▀     ██████████
\033[0mETHERATE: To communicate data over the network. \033[31m       ███    ███ """)

ip_address = input(f"{query}What IP address would you like to shell to: ")
port_number = input(f"{query}What port number would you like to listen to: ")
username = input(f"{query}Enter the username of the remote system: ")
password = getpass.getpass(f"{query}Enter the password for that user on the remote system (optional if system has no password): ")

print(f"{info}It'll start by running ipconfig, to test if it works.")
PsExec('ipconfig', username, password, port_number, ip_address)

while True:
    command = input("")
    PsExec(command, username, password, port_number, ip_address)