import serial
import time
import sys
import re
import requests
import time
import logging
import os

pid = os.getpid()
logging.basicConfig(
    filename="logs/log.txt",
    level=logging.DEBUG,
    format=f"%(levelname)s %(asctime)s {pid} %(message)s",
)

logging.basicConfig(level=logging.INFO)
logging.info(f"PID: {pid}")


def task(port, i=100):
    sys.setrecursionlimit(i)
    logging.debug("script loaded...")
    last_scan = None
    try:
        ser = serial.Serial(port, 9600, timeout=0)
        while True:
            barcode = ser.read(1000)
            str1 = barcode.decode("UTF-8")
            if str1:
                logging.info("Read: " + str1 + " lenght: " + str(len(str1)))
                logging.info(last_scan)
                if last_scan:
                    scan = last_scan + str1
                    match = regex(scan)
                    last_scan = scan
                else:
                    match = regex(str1)
                    last_scan = str1
                if match:
                    value = match.group(0)
                    logging.info("Match: " + value)
                    requst(value)
                    last_scan = None
                
    except serial.SerialException as e:
        logging.debug("Error in reading")
        logging.error(str(e))
        i = i + 1
        time.sleep(5)
        task(port, i)


def regex(barcode):
    x = re.search("\d+ [xX] \d+ [xX] \d+ -\d+", barcode)
    return x


def requst(barcode):
    from config import operation

    try:
        url = f"http://13.127.56.55/api/container/scan/{operation}"
        r = requests.put(url, data={"container": barcode})
        # print(r)
        logging.info("Request susscess")
    except Exception as e:
        logging.info("Request faild")
        logging.error(str(e))


if __name__ == "__main__":
    port = sys.argv[1]
    task(port, i=100)
