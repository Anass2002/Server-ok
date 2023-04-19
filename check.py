import json
import os
import platform
import subprocess
import time
import management

LOG_FILE = "log.json"
HTML_FILE = "rapport.html"

def load_log():
    if os.path.isfile(LOG_FILE):
        with open(LOG_FILE, "r") as f:
          return json.load(f)
    else:
        return {}

def save_log(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

# ping-opdracht uitvoeren
def ping_server(server):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", server["host"]]
    success = subprocess.call(command, stdout=subprocess.PIPE) == 0
    if success:
        status = "Bereikbaar"
    else:
        status = "Onbereikbaar"
    return status

def check_servers(servers):
    results = {}
    for server in servers:
        result = ping_server(server)
        results[server["host"]] = result
    return results

def generate_report(results):
    with open('template.html', 'r') as f:
        template = f.read()
    rows = []
    for server, status in results.items():
        row = """
        <tr>
            <td>{server}</td>
            <td>{status}</td>
        </tr>
        """.format(server=server, status=status)
        rows.append(row)
    html = template.format(time=time.strftime("%Y-%m-%d %H:%M:%S"), rows="".join(rows))
    with open(HTML_FILE, "w") as f:
        f.write(html)
    print(f"Rapport gemaakt! ({HTML_FILE})!")

def check_mode():
    servers = management.load_servers()
    log = load_log()
    print("Hosts aan het checken...")
    results = check_servers(servers)
    save_log(results)
    generate_report(results)
    print(f"Bekijk de {HTML_FILE} voor de resultaten.")
