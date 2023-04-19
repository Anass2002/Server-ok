import sys
import management
import check

def main():
  if len(sys.argv) > 1:
    if sys.argv[1] == "management":
        management.management_mode()
    elif sys.argv[1] == "check":
        check.check_mode()
    elif sys.argv[1] == "add":
      if len(sys.argv) > 2:
        host = sys.argv[2]
        servers = management.load_servers()
        servers.append({"host": host})
        management.save_servers(servers)
      else:
        print("Geen hostnaam opgegeven.")
    elif sys.argv[1] == "delete":
      if len(sys.argv) > 2:
        index = int(sys.argv[2]) - 1
        servers = management.load_servers()
        del servers[index]
        management.save_servers(servers)
    elif sys.argv[1] == "list":
        servers = management.load_servers()
        print("Servers:")
        for i, server in enumerate(servers):
            i = i + 1
            print(f'{i}: {server["host"]}')
    else:
      print("Ongeldige optie. Kies uit deze argumenten:\n'add host',\n'delete lijstnummer',\n'list',\n'check',\n'management'")
  else:
    check.check_mode()

if __name__ == "__main__":
    main()