# Description

How about some hide and seek heh?\
Download the file and find the flag.

**tags: Forensic, pcap**

- PCAP
  - Packet Capture, which is a file format used to store network packet data captured from a network interface

`wireshark trace.pcap`
| Source      | Destination | Protocol |
| ----------- | ----------- | -------- |
| 172.16.0.2  | 10.253.0.6  | FTP      |
| 127.0.0.1   | 127.0.0.1   | DNS      |
| 10.253.0.55 | 192.168.5.5 | FTP Data |

- Search string for 'pico' did not work
- Search hex value for 'pico' which is `70 69 63 6f` and was able to find the packet

| Sorce      | Destination | Protocol | Length | Info               |
| ---------- | ----------- | -------- | ------ | ------------------ |
| 172.16.0.2 | 10.253.0.6  | TCP      | 82     | TCP Retransmission |

- Relavant hex code is following
```
0000   45 00 00 52 00 01 00 00 40 06 c3 90 ac 10 00 02   E..R....@.......
0010   0a fd 00 06 00 14 00 15 00 00 00 00 00 00 00 00   ................
0020   50 02 20 00 d7 21 00 00 70 69 63 6f 43 54 46 7b   P. ..!..picoCTF{
0030   50 36 34 50 5f 34 4e 34 4c 37 53 31 53 5f 53 55   P64P_4N4L7S1S_SU
0040   35 35 33 35 35 46 55 4c 5f 34 36 32 34 61 38 62   55355FUL_4624a8b
0050   36 7d                                             6}
```

- Looks like the TCP connection is lost after the packet

**Flag found: picoCTF{P64P_4N4L7S1S_SU55355FUL_4624a8b6}**
