# Description
Help us test the form by submiting the username as test and password as test!
Additional details will be available after launching your challenge instance.

**tags: Web Exploitation**

## Notes
- When first connected to the website, it directs to the `/login`
- Before logging in, started BurpSuite and connected intercept and saved it tp `repeater`
- When logging in as `username= test& password= test!` notice the `next-page id`
```<p>Found. Redirecting to 
    <a href="/next-page/id=cGljb0NURntwcm94aWVzX2Fs">
    /next-page/id=cGljb0NURntwcm94aWVzX2Fs</a>
</p>
```
- Looks like it's encryted data
- Decrypted data using base64 decryption turns out to be the first part of the flag `picoCTF{proxies_al`
- After processing the login, notice the `next-page id` under `Referer` is different than what we had previous
`Referer: http://saturn.picoctf.net:55618/next-page/id=bF90aGVfd2F5XzNkOWUzNjk3fQ==`
- Decrypted data with base64 is the last half of the flag `l_the_way_3d9e3697}`


**Flag found: picoCTF{proxies_all_the_way_3d9e3697}**

Total time spent: ~ 5 minutes