# Description
In RSA, a small e value can be problematic, but what about N? Can you decrypt this? `values`

**tags: Cryptography**

## Notes
```c: 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n: 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e: 65537 
```

- e is the encryption exponent (public / usually 65537)
- c is the cypher text
- n is the Public Key

- Simply searched RSA decrypter and entered values
Reference: https://www.dcode.fr/rsa-cipher

**Flag found: picoCTF{sma11_N_n0_g0od_23540368}**

## RSA
- Factor => Numbers you can multiply to get the original number
- Prime => Numbers with factor of  only itself (and 1)
- Semi-Prime => Numbers with factor of prime numbers (Prime * Prime)
- Modulo => Remainder division

1. Select two prime numbers => (a, b) 
2. Multiply them to get M value => (a * b) = M
3. Calculate Totient of the value => (a - 1) * (b - 1) = T
4. Select Public Key 
    - Must be a prime number
    - Must be less than Totient
    - Must NOT be a factor of the totient
5. Select Private Key
    - Private key * Public Key / Totient must have Modulo of 1

**Encryption**
Message^Public Key MOD M = Cipher

**Decryption**
Cipher^Private Key MOD M = Message

### Example
1. 7 , 19 = Two rime numbers
2. 133 = M
3. 108 = T
4. 29 = Public Key (Multiple choices)
5. 41 Private Key
6. Message = 60

**Encryption**
(60 ^ 26) MOD 133 = 86

**Decryption**
(86 ^ 41) MOD 133 = 60