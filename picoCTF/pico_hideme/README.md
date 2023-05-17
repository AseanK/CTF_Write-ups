# Description
Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.

**tags: Forensics, steganography**

## Notes
- Since it's steganography, ran `steghide info flag.png` command
output: `steghide: the file format of the file "flag.png" is not supported.`
- Ran `exiftool flag.png` command to see the details of the file
output :
```File Name                       : flag.png
Directory                       : .
File Size                       : 43 kB
File Modification Date/Time     : 2023:05:17 03:50:30-04:00
File Access Date/Time           : 2023:05:17 03:51:05-04:00
File Inode Change Date/Time     : 2023:05:17 03:50:30-04:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 512
Image Height                    : 504
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 512x504
Megapixels                      : 0.258
```

- Notice the `Warning: [minor] Trailer data after PNG IEND chunk`
- This means that there's something other than original png file attached after the trailer data
- Ran `hexeditor` and searched for `IEND`
output : ``00009B30  00 00 00 49  45 4E 44 AE   42 60 82 50  4B 03 04 0A  ...IEND.B`.PK...``
- Looks like there's PK (Package) file in it
- Pk file starts at hex-00009B3B, which converts to 39739 in decimal
- ran `dd if=flag.png of=answer.zip skip=39739 bs=1` to extract the package
reference: https://kalitut.com/dd-command/

- `answer.zip` file contains the `.png` file of the flag

**Flag found: picoCTF{Hiddinng_An_imag3_within_@n_ima9e_d55982e8}**
