import pexpect
from pexpect import pxssh
import getpass

try:
    shellLogin = pxssh.pxssh()
    hostname = input('hostname: ')
    username = input('username: ')
    password = getpass.getpass('password: ')
    shellLogin.login(hostname,username,password)
    shellLogin.sendline('uptime')
    shellLogin.prompt()
    print(shellLogin.before)
    shellLogin.sendline('ls -l')
    shellLogin.prompt()
    print(shellLogin.before)
    shellLogin.sendline('df')
    shellLogin.prompt()
    print(shellLogin.before)
    shellLogin.logout()

except pxssh.ExceptionPexpect:
    print ("pxssh failed on login.")

