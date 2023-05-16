# Description
Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:27177/

**tags: Web Exploitation**

## Notes
- The name itself is `cookie` (assuming it's a cookie exploitation)
- The website has one input where user can enter a name of a cookie.

## Exploitation
- Opened up the developer tools and under storage category, There's a cookie selection.
- It's originally set to -1
- Changed to value of 1 and refreshed which then shows the chocolate chip cookie

## Burpsuite
- Sent the website response to the Intruder and Repeater
- Changed Intruder payload type to Brute forcer with intigers
- Ran the attack
- Response to the value 18 was 1265 which is shorter than others 1920 - 1970
- Changed the cookie value to 18 on the Repeater
<br>

**Flag found: picoCTF{3v3ry1_l0v3s_c00k135_064663be}**

Total time spent: ~ 15 minutes