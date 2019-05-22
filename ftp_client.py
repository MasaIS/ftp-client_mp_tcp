from ftplib import FTP
from getpass import getpass

#server_ip = '192.168.183.220'
server_ip = '134.160.38.1'

ftp = FTP(server_ip)
user = input('FTP user ?:')
password = getpass('FTP password ?:')

ftp.login(user, password)

#files = ftp.nlst('/disk1/Mantle/Anime/')
#print(files)

#ftp.cwd('/disk1/Mantle/Anime/')
ftp.cwd('/Linux/centos/7/os/x86_64/')
#files = ftp.retrlines('LIST')
files = ftp.mlsd()

for filename, facts in files:
    if facts['type'] == 'file':
        print(filename, facts['modify'])

ftp.quit()