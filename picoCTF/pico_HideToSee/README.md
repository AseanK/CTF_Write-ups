# Description
How about some hide and seek heh? Look at this image 'here'.


**tags: cryptography**

## Notes
- Contains `atbash.jpg` file
- Ran `exiftool atbash.jpg` to see the details about the file
```
File Name                       : atbash.jpg
Directory                       : .
File Size                       : 51 kB
File Modification Date/Time     : 2023:05:22 02:58:58-04:00
File Access Date/Time           : 2023:05:22 03:00:14-04:00
File Inode Change Date/Time     : 2023:05:22 02:58:58-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Image Width                     : 465
Image Height                    : 455
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 465x455
Megapixels                      : 0.212
```

- Notice the `X Resolution: 1` and `Y Resolution: 1` sometimes when you use steganography, the X and Y resolution changes to 1

- Ran `steghide info atbash.jpg` 

```
"atbash.jpg":
  format: jpeg
  capacity: 2.4 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "encrypted.txt":
    size: 31.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

- This indicates there's a embedded `encrypted.txt` file
- Also It bypassed the passphrase, It usually asks to enter a passphrase, which means the password is just empty
- Ran `steghide extract -sf  atbash.jpg` to extract the data.

```
Enter passphrase: 
wrote extracted data to "encrypted.txt".
```

- Left passphrase empty and extracted the file

To learn more about steghide : https://steghide.sourceforge.net/documentation.php


- The txt file contains what looks to be a encrypted flag with atbash `krxlXGU{zgyzhs_xizxp_92533667}` 
- atbash cypher is a simplistic cipher where you change A to Z, B to Y, C to X and so on
- Decrypted the flag using the online atbash converter

**Flag found: picoCTF{atbash_crack_92533667}**


Total time spent: ~ 10 minutes

