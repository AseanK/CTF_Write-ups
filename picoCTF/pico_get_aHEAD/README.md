## Description
Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:47967/

**tags: Binary Exploitation**

## NOTES
- The name itself is get a HEAD

## The website

```HTTP/1.1 200 OK

Content-type: text/html; charset=UTF-8

<!doctype html>
<html>
<head>
    <title>Blue</title>
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<style>body {background-color: blue;}</style>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:red">Red</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="GET">
								<input type="submit" value="Choose Red"/>
							</form>
						</div>
					</div>
				</div>
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:blue">Blue</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="POST">
								<input type="submit" value="Choose Blue"/>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
```

- Two buttons changes color of the background when pressed.
- Red button is using `GET` request method and the blue is using `POST`

## Burp Suite
- Used Proxy intercept and got following code when blue button is pressed

```POST /index.php HTTP/1.1
Host: mercury.picoctf.net:47967
Content-Length: 0
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://mercury.picoctf.net:47967
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://mercury.picoctf.net:47967/index.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
```

- Altered request type to `GET` using Repeater.
- Altered request type to `PUT` with `Content-Length: 128`
- Tried same thing for the red button
**Nothing was changed in the response**

- Changed request type to `HEAD`

**Flag found: `picoCTF{r3j3ct_th3_du4l1ty_cca66bd3}`**

- `HEAD` request `GET` information about the document without the body response. (often used by clients with cache to see if the document has changed)

Total time spent: ~1 hour