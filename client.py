import io
import subprocess
import requests

IP = "192.168.1.101"
IP = "192.168.1.153"
PORT = 8000

proc = subprocess.Popen(["./single_chan_pkt_fwd"], stdout=subprocess.PIPE)
for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):  # or another encoding
    line = line.strip()
    print(line)
    if len(line) > 0 and line[0] == "{":
        requests.post(f"http://{IP}:{PORT}/put_moisture", line)
