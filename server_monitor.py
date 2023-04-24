import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(8.0)
import requests
import re
import os
import threading
lck = threading.Lock()
TOKEN = "5719788810:AAESwA90j6bXDVVXXXXXXXXXXXXX"
CHAT_ID = "-10018XXXXXXXX"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())
hostsfile=open("/etc/ansible/hosts")
os.system("touch down.txt")

def hostcheck(ip,host,cid):
        if os.system("ping -c 5 " + ip) == 0:
            response=0
        elif sock.connect_ex((ip,80))  == 0 :
            print("http ok")
            response=0
        else:
            response=1
        
        if response == 0:
            with open(r'down.txt', 'r') as file:
             content = file.read()
             if ip in content:
               print(ip, 'is up!')
               message=ip+" is up hostname="+host+" "+str(cid)
               url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
               print(requests.get(url).json())
               with open(r'down.txt', 'r') as f:
                output = []
                for line in f:
                    if not ip in line:
                        output.append(line)
               f = open('down.txt', 'w')
               f.writelines(output)
               f.close()
             else:
               print('string does not exist')

        else:
            with open(r'down.txt', 'r') as file:
             content = file.read()
             if not ip in content:
              print(ipaddress, 'is down!')
              message=ipaddress+" is down hostname= "+host+" "+str(cid)
              url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
              print(requests.get(url).json())
              file1 = open("down.txt", "a")
              file1.write("\n")
              file1.write(ip)
              file1.close()


threads = []
for i in hostsfile.readlines():
     if not i.startswith('#') and (re.search("([0-9]{1,3}\.){3}[0-9]{1,3}",i)):
        ipaddress=re.search("([0-9]{1,3}\.){3}[0-9]{1,3}",i).group()
        print(ipaddress)

        try:
            clientid=re.search("clientid=([0-9]){1,4}",i).group()
            hostname=re.search("[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}",i).group()

        except:
            clientid=0000
            hostname=""
        print(clientid,hostname)
        th=threading.Thread(target=hostcheck(ipaddress,hostname,clientid))
for t in threads:
            t.join()

