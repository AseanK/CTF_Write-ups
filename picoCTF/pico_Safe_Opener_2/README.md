# Description

What can you do with this file?\
I forgot the key to my safe but this file is supposed to help me with retrieving the lost key.\
Can you help me unlock my safe?

**tags: Reverse Engineering**

## Notes

- File content

`file SafeOpener.class`
```SafeOpener.class: compiled Java class data, version 52.0 (Java 1.8)
```

- Ran file

`java SafeOpener`
```
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Enter password for the safe:
```

- Random password

```
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Enter password for the safe: sd
c2Q=
Password is incorrect

You have  2 attempt(s) left
Enter password for the safe: ds
ZHM=
Password is incorrect

You have  1 attempt(s) left
Enter password for the safe: a
YQ==
Password is incorrect

You have  0 attempt(s) left
```

- Used hexdump

`hexdump SafeOpener.class`
```
...
00000170  6a 61 76 61 2f 75 74 69  6c 2f 42 61 73 65 36 34  |java/util/Base64|
00000180  24 45 6e 63 6f 64 65 72  3b 01 00 0a 65 6e 63 6f  |$Encoder;...enco|
00000190  64 65 64 6b 65 79 01 00  12 4c 6a 61 76 61 2f 6c  |dedkey...Ljava/l|
000001a0  61 6e 67 2f 53 74 72 69  6e 67 3b 01 00 03 6b 65  |ang/String;...ke|
000001b0  79 01 00 01 69 01 00 01  49 01 00 0d 53 74 61 63  |y...i...I...Stac|
000001c0  6b 4d 61 70 54 61 62 6c  65 07 00 2a 07 00 44 07  |kMapTable..*..D.|
000001d0  00 63 07 00 64 01 00 0a  45 78 63 65 70 74 69 6f  |.c..d...Exceptio|
000001e0  6e 73 07 00 65 01 00 08  6f 70 65 6e 53 61 66 65  |ns..e...openSafe|
000001f0  01 00 15 28 4c 6a 61 76  61 2f 6c 61 6e 67 2f 53  |...(Ljava/lang/S|
00000200  74 72 69 6e 67 3b 29 5a  01 00 08 70 61 73 73 77  |tring;)Z...passw|
00000210  6f 72 64 01 00 0a 53 6f  75 72 63 65 46 69 6c 65  |ord...SourceFile|
00000220  01 00 0f 53 61 66 65 4f  70 65 6e 65 72 2e 6a 61  |...SafeOpener.ja|
00000230  76 61 0c 00 1e 00 1f 01  00 16 6a 61 76 61 2f 69  |va........java/i|
00000240  6f 2f 42 75 66 66 65 72  65 64 52 65 61 64 65 72  |o/BufferedReader|
00000250  01 00 19 6a 61 76 61 2f  69 6f 2f 49 6e 70 75 74  |...java/io/Input|
00000260  53 74 72 65 61 6d 52 65  61 64 65 72 07 00 66 0c  |StreamReader..f.|
00000270  00 67 00 68 0c 00 1e 00  69 0c 00 1e 00 6a 07 00  |.g.h....i....j..|
00000280  6b 0c 00 6c 00 6d 01 00  00 0c 00 6e 00 6f 01 00  |k..l.m.....n.o..|
00000290  1d 45 6e 74 65 72 20 70  61 73 73 77 6f 72 64 20  |.Enter password |
000002a0  66 6f 72 20 74 68 65 20  73 61 66 65 3a 20 07 00  |for the safe: ..|
000002b0  70 0c 00 71 00 72 0c 00  73 00 74 07 00 64 0c 00  |p..q.r..s.t..d..|
000002c0  75 00 76 0c 00 77 00 78  0c 00 79 00 72 0c 00 3e  |u.v..w.x..y.r..>|
000002d0  00 3f 01 00 17 6a 61 76  61 2f 6c 61 6e 67 2f 53  |.?...java/lang/S|
000002e0  74 72 69 6e 67 42 75 69  6c 64 65 72 01 00 0a 59  |tringBuilder...Y|
000002f0  6f 75 20 68 61 76 65 20  20 0c 00 7a 00 7b 0c 00  |ou have  ..z.{..|
00000300  7a 00 7c 01 00 10 20 61  74 74 65 6d 70 74 28 73  |z.|... attempt(s|
00000310  29 20 6c 65 66 74 0c 00  7d 00 74 01 00 2c 70 69  |) left..}.t..,pi|
00000320  63 6f 43 54 46 7b 53 41  66 33 5f 30 70 33 6e 33  |coCTF{SAf3_0p3n3|
00000330  72 72 5f 79 30 75 5f 73  6f 6c 76 33 64 5f 69 74  |rr_y0u_solv3d_it|
00000340  5f 35 62 66 62 64 36 66  31 7d 0c 00 7e 00 7f 01  |_5bfbd6f1}..~...|
00000350  00 0b 53 65 73 61 6d 65  20 6f 70 65 6e 01 00 16  |..Sesame open...|
00000360  50 61 73 73 77 6f 72 64  20 69 73 20 69 6e 63 6f  |Password is inco|
00000370  72 72 65 63 74 0a 01 00  0a 53 61 66 65 4f 70 65  |rrect....SafeOpe|
00000380  6e 65 72 01 00 10 6a 61  76 61 2f 6c 61 6e 67 2f  |ner...java/lang/|
00000390  4f 62 6a 65 63 74 01 00  18 6a 61 76 61 2f 75 74  |Object...java/ut|
000003a0  69 6c 2f 42 61 73 65 36  34 24 45 6e 63 6f 64 65  |il/Base64$Encode|
000003b0  72 01 00 10 6a 61 76 61  2f 6c 61 6e 67 2f 53 74  |r...java/lang/St|
000003c0  72 69 6e 67 01 00 13 6a  61 76 61 2f 69 6f 2f 49  |ring...java/io/I|
000003d0  4f 45 78 63 65 70 74 69  6f 6e 01 00 10 6a 61 76  |OException...jav|
000003e0  61 2f 6c 61 6e 67 2f 53  79 73 74 65 6d 01 00 02  |a/lang/System...|
000003f0  69 6e 01 00 15 4c 6a 61  76 61 2f 69 6f 2f 49 6e  |in...Ljava/io/In|
00000400  70 75 74 53 74 72 65 61  6d 3b 01 00 18 28 4c 6a  |putStream;...(Lj|
00000410  61 76 61 2f 69 6f 2f 49  6e 70 75 74 53 74 72 65  |ava/io/InputStre|
00000420  61 6d 3b 29 56 01 00 13  28 4c 6a 61 76 61 2f 69  |am;)V...(Ljava/i|
00000430  6f 2f 52 65 61 64 65 72  3b 29 56 01 00 10 6a 61  |o/Reader;)V...ja|
00000440  76 61 2f 75 74 69 6c 2f  42 61 73 65 36 34 01 00  |va/util/Base64..|
00000450  0a 67 65 74 45 6e 63 6f  64 65 72 01 00 1c 28 29  |.getEncoder...()|
00000460  4c 6a 61 76 61 2f 75 74  69 6c 2f 42 61 73 65 36  |Ljava/util/Base6|
00000470  34 24 45 6e 63 6f 64 65  72 3b 01 00 03 6f 75 74  |4$Encoder;...out|
00000480  01 00 15 4c 6a 61 76 61  2f 69 6f 2f 50 72 69 6e  |...Ljava/io/Prin|
00000490  74 53 74 72 65 61 6d 3b  01 00 13 6a 61 76 61 2f  |tStream;...java/|
000004a0  69 6f 2f 50 72 69 6e 74  53 74 72 65 61 6d 01 00  |io/PrintStream..|
...
```

- Noitice 0x320

```
00000310  29 20 6c 65 66 74 0c 00  7d 00 74 01 00 2c 70 69  |) left..}.t..,pi|
00000320  63 6f 43 54 46 7b 53 41  66 33 5f 30 70 33 6e 33  |coCTF{SAf3_0p3n3|
00000330  72 72 5f 79 30 75 5f 73  6f 6c 76 33 64 5f 69 74  |rr_y0u_solv3d_it|
00000340  5f 35 62 66 62 64 36 66  31 7d 0c 00 7e 00 7f 01  |_5bfbd6f1}..~...|
```

**Flag found: picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_5bfbd6f1}**