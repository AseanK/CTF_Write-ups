# Description

Try reversing this file? Can ya? I forgot the password to this file. Please find it for me?

**tags: Reverse Engineering**

## Notes

- File is a `.elf` file

`file ret`
```
ret: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=64856d07d138e412faf30b9722d92f507e3b5c9c, for GNU/Linux 3.2.0, not stripped
```

- Tried running file with `sudo chmod +x ret` and `./ret`

`Enter the password to unlock this file:`

- Looks like we need the password

```
Enter the password to unlock this file: asd
You entered: asd
Access denied
```

`hexdump -C ret | grep pico`
```
000011e0  45 f8 31 c0 48 b8 70 69  63 6f 43 54 46 7b 48 ba  |E.1.H.picoCTF{H.|
00002060  20 73 65 65 20 66 6c 61  67 3a 20 70 69 63 6f 43  | see flag: picoC|
```

- Looks like we got the location to the flag!

`hexeditor ret` and go to offset to `0x2060`
```
20 73 65 65  20 66 6C 61   67 3A 20 70  69 63 6F 43   see flag: picoC
00002070  54 46 7B 33  6C 66 5F 72   33 76 33 72  35 69 6E 67  TF{3lf_r3v3r5ing
00002080  5F 73 75 63  63 65 35 35   66 75 6C 5F  64 37 62 31  _succe55ful_d7b1
00002090  34 64 34 33  7D 00 41 63   63 65 73 73  20 64 65 6E  4d43}.Access den
000020A0  69 65 64 00  01 1B 03 3B   40 00 00 00  07 00 00 00  ied....;@.......
```

**Flag found: picoCTF{3lf_r3v3r5ing_succe55ful_d7b14d43}**