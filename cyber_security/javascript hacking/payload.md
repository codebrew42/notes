# payload
## def
- malicious code that an attacker injects into a web app to exploit its vulnerabilites
- usually in JS
- performs various actions when executed in the victim's browser

## example
 <script>alert('This site is vulnerable to XSS!');</script>
- attacker might submit a comment containing this payload
- using <script> tag
- alert(): simple popup alert
-> can be more harmful : stealing cookies, redirecting users to a malicious site
