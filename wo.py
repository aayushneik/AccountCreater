import amino
import json
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.RED)
print("""__________________________________________________________________"""'')
print(pyfiglet.figlet_format("     ViCIous", font="slant"))
print("""__________________________________________________________________"""'')
print("""                 SCRIPT BY""")
print(Fore.GREEN)
print(pyfiglet.figlet_format("Account Creater", font="slant"))
print("""__________________________________________________________________"""'')
client=amino.Client()
password="pagal0"
while True:
 email=client.register_new(nickname="Romeo", password=password)
 d={}
 with open ("newmail.txt","a") as f:
  d["email"]=str(email)
  d["password"]=str(password)
  t=json.dumps(d)
  f.write(t+',')
  print("Saved in File newmail.txt")