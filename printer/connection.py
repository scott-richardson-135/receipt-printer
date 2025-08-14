from escpos.printer import Network
from dotenv import load_dotenv
import os

PORT = 9100 #maybe make env idk

def getPrinter():

    load_dotenv()
    printer_ip = os.getenv("PRINTER_IP")

    if not printer_ip:
        raise ValueError("Printer IP not set")
    
    return Network(printer_ip, PORT)