import socket
import sys
import time
from threading import Thread

service="tcp"
usage = "python3 port_scanner.py <ip> <start_port> <end_port>"
def argument_check():
    if len(sys.argv) != 4:
        print("Error in usage")
        print(usage)
        sys.exit()
argument_check()
def check_port(port):
    #print(f"Scanning port {port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   # s.settimeout(1)
    connection = s.connect_ex((sys.argv[1],port))
    if not connection:
        print(f"{port}\t\t{socket.getservbyport(port, service)}")

def threading_port():
    
    print("Open ports\tService")
    for port in range(int(sys.argv[2]),int(sys.argv[3])):
        t = Thread(target=check_port,args=(port,))
        t.start()
threading_port()
