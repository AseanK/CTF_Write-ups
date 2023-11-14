# Description

You will find the flag after decrypting this file Download the encrypted flag here.

**tags: Cryptography**

## Notes

- File is `.txt` file

`cat encrypted.txt`
```
xqkwKBN{z0bib1wv_l3kzgxb3l_4k71n5j0}
```

- Looks like it's encoded with Caesar cipher?
- We know that the flag format  `picoCTF{...}`
- x is 8 characters away from p so the key is 8
- Wrote a simple Python program

```py
enc = 'xqkwKBN{z0bib1wv_l3kzgxb3l_4k71n5j0}'

cha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ans = []
for i in enc:
    if i in cha:
        ind = cha.index(i)
        ans.append(cha[ind-8])
    else:
        ans.append(i)
print(''.join(ans))
```

- Run the program
```sh
$ python ans.py
picoKBN{r0tat1on_d3crypt3d_4c71f5b0}
```
- Notice the KBN has not decrypted because it's in cap
- Luckliy we know that "KBN" must be "CTF" and there's no other capitalized string

**Flag found: picoCTF{r0tat1on_d3crypt3d_4c71f5b0}**