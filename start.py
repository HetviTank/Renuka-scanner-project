import subprocess
import serial.tools.list_ports
import serial


def start_process():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        subprocess.Popen(["pythonw", "main.py", port.name])


if __name__ == "__main__":
    start_process()
