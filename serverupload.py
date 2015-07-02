import getpass
from fabric.api import *
host=prompt("enter your host(user@ip):")#,default="*************") #like raw_input
port=prompt("enter your port:")
passwd=getpass.getpass()
env.hosts=host
env.port=port
env.password=passwd

local_path=prompt("Which file would you like to upload?(path):")
destination_path=prompt("And Where?:")

def run():
	put(local_path,destination_path,mode=0755)
