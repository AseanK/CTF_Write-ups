# Description
I wonder what this really is... `enc` 
".join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

`% cat enc` ==> 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ <br>
**tags: picoCTF 2021, Reserse Engineering**

## Notes
- `.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`
- << 8 => shift left by 8 bits
- ord ==> bits to character
- chr ==> char to bits 

### Prettified code
```For I in range( 0, len(flag), 2)
Ord(flag[i] << 8) + ord(flag[I + 1])
```

First two `i`s are "p" and "i" knowing flag format = picoCTF{}
Ord(flag[p] << 8) + ord(flag[i])

### Using ASCII :
p = 01110000 & i = 01101001
(01110000 << 8) + (01101001)
= 112                    = 105

Reference: http://sticksandstones.kstrom.com/appen.html

- Shifting 8 bits to left = 0111.0000.0000.0000 ( 16-bits)
28672 + 105  = 28777

Tried to find from ASCII but ASCII is 8-bit code ( `<< 8` makes it 16-bit ) <br>
UTF-16 is a 16-bit code
Looked up 28777 unicode character

Reference: https://www.compart.com/en/unicode/U+7069

**MATCH** `灩`
**It uses utf-16**

# Reverse Engineering
```flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"
ans = ""
for i in range(0, len(flag)):
    word = chr((ord(flag[i]) >> 8)) + chr(flag[i].encode('utf-16')[-1])
    ans += word
print(ans)
```

Everything seems good getting duplicated output for `chr(flag[i].encode('utf-16')[-1])`.
After digging for some time; Came across following article

Reference: https://bugs.python.org/issue25325

There are "three sub-flavors" for UTFs :
- BE : Big-Endian byte serialization (most significant byte first)
- LE : Little-Endian byte serialization (less significant byte first)
- unmarked (Big-Endian by default, but may include a order mark to indicate the actual byte serialization used)

Reference : https://www.unicode.org/glossary

Tried :

```flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"
ans = ""
for i in range(0, len(flag)):
    word = chr((ord(flag[i]) >> 8)) + chr(flag[i].encode('utf-16be')[-1])
    ans += word
print(ans)
```

**Flag found : `picoCTF{16_bits_inst34d_of_8_26684c20}`**

Also tried `utf-16le` to see if I get different result.
returns duplicated `ans` like the first one (Seems like `unmarked` used LE)

`utf-32be` gives valid flag. ( because uses significant bytes first?? )

Total time spent : ~7 hours
