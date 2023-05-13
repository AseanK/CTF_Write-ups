# Description
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: `this`

**tags Forensics**

## Notes
- A jpg formetted file

`exiftool dolls.jpg `<br>
`Warning: [minor] Trailer data after PNG IEND chunk`
- This suggest that there's something embeded in the file<br>

`steghide info dolls.jpg`
Returns :
`steghide: the file format of the file "dolls.jpg" is not supported.`<br>

`hexdump -C dolls.jpg`
- Began investigating Hexidecimal formet
```00042890  6D 61 67 65  73 2F 32 5F   63 2E 6A 70  67 55 54 09  mages/2_c.jpgUT.```
- `mages/2_c.jpgUT` looks suspicious; Maybe another jpg is embeded
- 00042890 + 10 bytes = 0004289A which converts to 272538
`dd if=dolls.jpg of=answer.jpg skip=272538 bs=1`<br>
Parameter: <br>
**if**: indicates the source, i.e. to where we copy from. Specifies a file that can be either a regular file or a device file.<br>

**of**: indicates the destination file. The same thing, we can write both in a regular file and directly in the device.<br>

**bs**: the number of bytes to be written at a time. You can think of this argument as the size of the piece of data that will be written or read, and the number of pieces is regulated by the next parameter.<br>

Reference:<br>
https://kalitut.com/dd-command/

Hexidecimal Converter:<br>
https://www.rapidtables.com/convert/number/hex-to-decimal.html<br>

- Saved the file but it was corrupted
- Tried using different `bs` and index; Nothing worked
- After digging for some time I found [This](https://www.w3.org/TR/PNG-Structure.html)
- It states "One notable restriction is that IHDR must appear first and IEND must appear last; thus the IEND chunk serves as an end-of-file marker."<br>

`hexdump -C dolls.jpg | grep IEND`
returns:<br>
```00042860  00 00 00 00  49 45 4E 44   AE 42 60 82  50 4B 03 04  ....IEND.B`.PK..
```
- Looks like package file is embeded
- 00042860 + 12 bytes = 0004286C which converts to 272492

`dd if=dolls.jpg of=answer.zip skip=272492 bs=1`
- .zip because `PK`<br>
- Hexeditor might help finding indices<br>

- Un-corrupted `.zip` file
- After Extracting it, there's another `.zip` file
- Repeat `dd`
- After repeating 5 times, `.txt` file is in the `.zip` file <br>

**Flag-found: picoCTF{336cf6d51c9d9774fd37196c1d7320ff}**
<br>
total time spent: ~ 4 hours