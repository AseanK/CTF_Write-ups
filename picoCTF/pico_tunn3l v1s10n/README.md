# Description

We found this file. Recover the flag.

**tags: Forensics**

## Notes

Contanined file does not hav any extensions (data formatted)

`cat tunn3l_v1s10n`

outputs gibberish

`hexeditor tunn3l_v1s10n`

- The first 4 bytes are **42 4D 8E 26** which is **BM.&** in ASCII
- First 2 bytes BM indicates that the file is .bmp (Bitmap Image) file
- Changed it's extention to .bmp `tunn3l_v1s10n.bmp`
- Used `gimp` to open
- File can not be opened with error in the header

**BMP file header format**
| Offset hex | Size    | Purpose                                                                                                |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------ |
| 00         | 2 bytes | Used to identify the BMP and DIB file                                                                  |
| 02         | 4 bytes | The size of the BMP file in bytes                                                                      |
| 06         | 4 bytes | Reserved; actual value depends on the applicarion that creates the image, can be 0 if created manually |
| 0A         | 4 bytes | The offset, i.e. starting address of the byte where the bitmap image data can be found                 |

- Size 8E 26 2C 00 = 0x(00)2C268E = 2,893,454 - Correct
- Reserved 00 00 00 00 = Manually created - Correct
- Offset BA D0 00 00 = 0x0000D0BA - offset D0BA does not exist in the file
- Turns out pixel data comes after the info header which is 40 bytes in total [BMP format](http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm)
  - 14 (header) + 40 (info header) = 54 = 0x0036
- File still can not be opened with error in header

**info header format**
| Offset hex | Size    | Purpose                              |
| ---------- | ------- | ------------------------------------ |
| 0E         | 4 bytes | Size of infoHeader which is 40 bytes |
| 12         | 4 bytes | Horizontal width                     |
| 16         | 4 bytes | Vertical height                      |
| 1A         | 2 bytes | Number of planes (=1)                |
| 1C         | 2 bytes | Bits per Pixel                       |

- Size BA D0 = 0xD0BA = 53434 bytes - Incorrect!
- Size must be 40 bytes = 0x28 - 28 00 00 00
- Successfully loaded image but the content contains `noflag{sorry}`
- Width = 6E 04 00 00 = 0x46E = 1134
- Height = 32 01 00 00 = 0x132 = 306
- Planes = 01 00 = 1
- Bits per pixel = 18 00 = 0x18 = 24 bits per pixel
- Width * Height * 24 bits has to be equal to the size of the file (2,893,454 bytes)
  - 1134 * 306 * 24 = 9,180,000 bits
  - 8 bits per byte 9,180,000 / 8 = 1,147,500 bytes
- Actual size of the file is bigger than what's in the header
- Size of the file has to be either
  - (2,893,454 * 8) / 24 / 1134 (width) = height = 850.52
  - (2,893,454 * 8) / 24 / 306 (height) = width = 3151.91
- Height of ~851 is 0x353 = 53 03

**Flag found: picoCTF{qu1t3_a_v13w_2020}**