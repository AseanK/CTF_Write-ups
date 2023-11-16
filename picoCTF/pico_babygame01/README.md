# Description

Get the flag and reach the exit.\
Welcome to BabyGame! Navigate around the map and see what you can find! The game is available to download. There is no source available, so you'll have to figure your way around the map. You can connect with it using `nc saturn.picoctf.net 55144`

**tags: Binary Exploitation, game**

## Notes

- `game` files does not have extension

`file game`
```
game: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=02a3bb43121b1f6fbc2ab9154ab38a9427e19149, for GNU/Linux 3.2.0, not stripped
```
- It's an ELF file, ran the file with `sudo chmod +x game` and `./game`

```
Player position: 3 4
End tile position: 29 89
Player has flag: 0
..........................................................................................
..........................................................................................
..........................................................................................
....e.....................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
.........................................................................................X
```

- Tried arrow key, w,a,s,d, numbers
- w, a, s, d seems to move the e value
- Looks like I can enter multiple keys at once, i.g. `dddddd` will move to right 6 times
- When the player `e` gets to the goal `X` the program exits with `You win!`
- `player = X` input will automatically move the player to position of `X`
  - Commands work!
- Looks like any kinds of command works the same way

`readelf -a game`
```
  ELF Header:
  Magic:   7f 45 4c 46 01 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF32
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Intel 80386
  Version:                           0x1
  Entry point address:               0x8049100
  Start of program headers:          52 (bytes into file)
  Start of section headers:          14468 (bytes into file)
  Flags:                             0x0
  Size of this header:               52 (bytes)
  Size of program headers:           32 (bytes)
  Number of program headers:         11
  Size of section headers:           40 (bytes)
  Number of section headers:         29
  Section header string table index: 28
  ...
```

- flag seems not to be hard coded
- While playing it around, ran out of bound and the output shows that I now hav 46 flags
```
Player has flag: 46
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
..........................................................................................
```
- Then I ran `player = flag` and the output shows
```
You win!
flage
flag.txt not found in current directory
```
- Maybe the key's in the server?
- Tried to do same but when I go out of bound nothing happends
  - I have to get to the certain point to get the flag
- At top left if you go out of bound to only `'a'`s (left) you get the flag but the program exits
- Tried going left one at a time and at the fourth move you get the flag and the program is still running
- Then ran `player = flag`

**Flag found: picoCTF{gamer_m0d3_enabled_e282d353}**