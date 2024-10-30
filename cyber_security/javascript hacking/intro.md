# process

## steps
### 1. identify user input fields
- login, registration, feedback forms where users submit data
- URL parameters : query strings in URLs(?id=1)  -> can be manipulated

### 2. inspect the source code
- view page source : browser's feature
-> see page's structure
- developer tools : f12
-> see network requests, dynamic content

### 3. check for reflected input
- enter simple text in input fields
-> see if it gets reflected back on the page

### 4. object references
- guess IDs: if URLs contain IDs or object references, try to change them
- id=2 -> id=2

### 5. automated tools
- OWASP ZAP or Burp Suite
-> discover potential vulnerabilities
- or firefox(hacker friendly)

