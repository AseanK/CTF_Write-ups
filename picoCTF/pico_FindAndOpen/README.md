# Decription

Someone might have hidden the password in the trace file. Find the key to unlock this file. This tracefile might be good to analyze.

**tags: Forensics**

# Notes

- Two files `dump.pcap` and `flag.zip`
- Looks like I have to analyze pcap file for the password

`wireshark dump.pcap`

- Packets looks interesting

```
0000   46 6c 79 69 6e 67 20 6f 6e 20 45 74 68 65 72 6e   Flying on Ethern
0010   65 74 20 73 65 63 72 65 74 3a 20 49 73 20 74 68   et secret: Is th
0020   69 73 20 74 68 65 20 66 6c 61 67                  is the flag
```

```
0000   69 42 77 61 57 4e 76 51 31 52 47 65 31 43 6f 75   iBwaWNvQ1RGe1Cou
0010   6c 64 20 74 68 65 20 66 6c 61 67 20 68 61 76 65   ld the flag have
0020   20 62 65 65 6e 20 73 70 6c 69 74 74 65 64 3f       been splitted?
```

```
0000   41 41 42 42 48 48 50 4a 47 54 46 52 4c 4b 56 47   AABBHHPJGTFRLKVG
0010   68 70 63 79 42 70 63 79 42 30 61 47 55 67 63 32   hpcyBpcyB0aGUgc2
0020   56 6a 63 6d 56 30 4f 69 42 77 61 57 4e 76 51 31   VjcmV0OiBwaWNvQ1
0030   52 47 65 31 49 7a 4e 45 52 4a 54 6b 64 66 54 45   RGe1IzNERJTkdfTE
0040   39 4c 5a 46 38 3d                                 9LZF8=
```

```
0000   50 42 77 61 57 55 76 51 31 52 47 65 31 4d 61 79   PBwaWUvQ1RGe1May
0010   62 65 20 74 72 79 20 63 68 65 63 6b 69 6e 67 20   be try checking 
0020   74 68 65 20 6f 74 68 65 72 20 66 69 6c 65         the other file
```

- VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
  - Base64 encrypted?
- It was encrypted message!
- Decrypted: This is the secret: picoCTF{R34DING_LOKd_
- Looks like I have to find the other half

```
0000   50 42 77 61 57 55 76 51 31 52 47 65 73 61 62 61   PBwaWUvQ1RGesaba
0010   62 61 62 6b 6a 61 41 53 4b 42 4b 53 42 41 43 56   babkjaASKBKSBACV
0020   56 41 56 53 44 44 53 53 53 53 44 53 4b 4a 42 4a   VAVSDDSSSSDSKJBJ
0030   53                                                S
```
- bababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
  - Nope
- iBwaWNvQ1RGe1
  - Nope
- PBwaWUvQ1RGe1
  - Nope
- The other half is in the `.zip`?
- Attempted `john the ripper` to crack the `.zip` file password

`zip2john flag.zip > file.txt`
`john -wordlist=/usr/share/wordlists/rockyou.txt file.txt`
```
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:01 DONE (2023-11-14 01:17) 0g/s 9691Kp/s 9691Kc/s 9691KC/s "2parrow"..*7¡Vamos!
Session completed.
```

- Seems like it's not working

`john -w=/usr/share/wordlists/rockyou.txt -ru file.hash`
```
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:48 DONE (2023-11-14 01:58) 0g/s 4836Kp/s 4836Kc/s 4836KC/s Anandrajsinghing..Aaaaaaaaaaaaing
Session completed.
```

- Nothing seems to be working
- After spending days I finally figured out the password is `picoCTF{R34DING_LOKd_`...
```
Archive:  flag.zip
[flag.zip] flag password: 
 extracting: flag
```
`cat flag`

**Flag found: picoCTF{R34DING_LOKd_fil56_succ3ss_494c4f32}**