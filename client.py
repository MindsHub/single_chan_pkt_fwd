import io
import subprocess
import requests

IP = "192.168.1.101"
PORT = 8000

def handleLine(line):
    print(line, end="", flush=True)
    line = line.strip()
    if len(line) > 0 and line[0] == "{":
        requests.post(f"http://{IP}:{PORT}/soil_data_received_from_sensor", line)

def runLoraListener():
    proc = subprocess.Popen(["./single_chan_pkt_fwd"], stdout=subprocess.PIPE)
    for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
        handleLine(line)

def debugHandleLine(line):
    handleLine('Hello') # does nothing
    handleLine('    {"I": 0, "H": 64.4, "T": 21.6, "M": 1024}\n') # tl 0%
    handleLine('    {"I": 1, "H": 64.4, "T": 21.6, "M": 800}\n')  # tr 40%
    handleLine('    {"I": 2, "H": 64.4, "T": 21.6, "M": 700}\n')  # br 60%
    handleLine('    {"I": 3, "H": 64.4, "T": 21.6, "M": 300}\n')  # bl 100%

if __name__ == "__main__":
    runLoraListener()
