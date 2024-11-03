## XSS : cross-site scripting
## 1.def
- sec vulnerability that allow attackers to inject malicious scripts into web pages views by users

- using your own script

## 2. how it works
- attacker inject javascript code into a web app, often through user input files or URL parameters
-> this code executes in the context of the users browser

## 3. types
### 3-1.stored xss
- malicious script is stored on the server (database, ...) -> served to users who access that page
### 3-2. reflected xss
- script is reflected off a web server
- usually in response to an user action
### 3-3. DOM-based xss
- attak occurs in the browser when malicious cript modifies the DOM of the page without needing a server response


## 4. consequences
### 4-1.data theft
### 4-2. malware distribution
### 4-3. defacement
- manipulate the content disp-ed on a web, can damage the site's reputation
### 4-4. phshing
- scripts create fake login forms -> trick users into entering their credentioals
### 4-5. reputation damage

## 5. mitigation strategies
### 5-1. input validation
- validate&sanitize user inputs -> ensure they don't contain harmful scripts
### 5-2. output encoding
- encode data before rendering it in the browser to prevent scripts from executing
- for example: convert '<' to '&lt;', '>' to '&gt;'
### 5-3. CSP: content secu. policy
- implement CSP headers to restrict where scripts can be loaded from -> reduce rsik of inline script executing
### 5-4. use HTTP only and secure flags
- set flags on cookies to prevent JS froom accessing them
-> ensure they're sent over HTTPS
### 5-5. regular secu. audits
- conduct regular secu- assessments -> identify&remediate vulnerabilities

