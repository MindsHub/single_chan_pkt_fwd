import io
import subprocess
import requests
import os
import sys
import traceback

IP = "192.168.1.101"
PORT = 8000
EXECUTABLE = os.path.dirname(os.path.abspath(__file__)) + "/single_chan_pkt_fwd"

def handleLine(line):
    try:
        print(line, end="", flush=True)
        line = line.strip()
        print(" ->", line, end="", flush=True)
        if len(line) > 0 and line[0] == ord(b"{"):
            print(" -> sending", end="", flush=True)
            requests.post(f"http://{IP}:{PORT}/soil_data_received_from_sensor", line, timeout=3)
        print(flush=True)
    except:
        print("Error", sys.stderr)
        traceback.print_exc()

def runLoraListener():
    proc = subprocess.Popen([EXECUTABLE], stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        handleLine(line)

def debugHandleLine(line):
    handleLine('Hello') # does nothing
    handleLine('    {"I": 0, "H": 64.4, "T": 21.6, "M": 1024}\n') # tl 0%
    handleLine('    {"I": 1, "H": 64.4, "T": 21.6, "M": 800}\n')  # tr 40%
    handleLine('    {"I": 2, "H": 64.4, "T": 21.6, "M": 700}\n')  # br 60%
    handleLine('    {"I": 3, "H": 64.4, "T": 21.6, "M": 300}\n')  # bl 100%

if __name__ == "__main__":
    runLoraListener()
