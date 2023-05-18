# Description
about trying to match a regular expression
Additional details will be available after launching your challenge instance.

**tags: Web Exploitation**

## Notes
- Description says try to match a regular expression

You can learn more about regular expression: https://eloquentjavascript.net/09_regexp.html

- Open up the webpage and view page source
- Under the `<script>` tag:
```<script>
	function send_request() {
		let val = document.getElementById("name").value;
		// ^p.....F!?
		fetch(`/flag?input=${val}`)
			.then(res => res.text())
			.then(res => {
				const res_json = JSON.parse(res);
				alert(res_json.flag)
				return false;
			})
		return false;
	}

</script>
```

- What we're interested in is the `// ^p.....F!?` comment

`^p` = Starting from p

`.` = Replaces any single charater

`F` = Ends with F

`!` = Symbols treated as regular character

`?` = Can replace anything

Regular expression cheat sheet: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Cheatsheet


- With the information we gathered, simply search for `picoCTF{`

**Flag found: picoCTF{succ3ssfully_matchtheregex_c64c9546}**

Total time spent: ~ 10 minutes
