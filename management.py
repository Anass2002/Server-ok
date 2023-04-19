import json
import os

SERVERS_FILE = "servers.json"

# Controleren of servers.json bestaat in de huidige werkmap
def load_servers():
    if os.path.isfile(SERVERS_FILE):
        with open(SERVERS_FILE, "r") as f:
            return json.load(f)
    else:
        return "Er zijn geen hosts gevonden, voeg eerst hosts toe!"

# Lijst opslaan in een JSON-bestand met indeling van 2 spaties per niveau
def save_servers(servers):
    with open(SERVERS_FILE, "w") as f:
        json.dump(servers, f, indent=2)

def management_mode():
    servers = load_servers()
    while True:
        print("Kies uit:")
        print("1. Host toevoegen")
        print("2. Host Verwijderen")
        print("3. Lijst van alle Hosts")
        print("4. Exit")
        choice = input("> ")
        if choice == "1":
            host = input("Voer de hostnaam of het IP-adres van de server in: ")
            servers.append({"host": host})
            save_servers(servers)
        elif choice == "2":
            print("Servers:")
            for i, server in enumerate(servers):
                i = i + 1
                print(f'{i}: {server["host"]}')
            index = int(input("Kies uit de lijst en vul de nummer in: "))
            index = index - 1
            del servers[index]
            save_servers(servers)
        elif choice == "3":
            print("Servers:")
            for i, server in enumerate(servers):
                i = i + 1
                print(f'{i}: {server["host"]}')
        elif choice == "4":
            break
        else:
            print("Ongeldig!")