# nmap (Network Mapper)
## definition
- nmap is a powerful network scanner that can be used to discover hosts and services on a network, as well as perform security audits and network mapping.

## basic scanning
### scan a single host
```bash
nmap 192.168.0.215 #nmap <target-ip>
```

### scan a range of hosts
```bash
nmap 192.168.0.0/24 #nmap <target-ip>/<subnet-mask>
```
### operating system detection
```bash
nmap -O 192.168.0.215 #nmap -O <target-ip>
```

### vulnerability detection
```bash
nmap -sV 192.168.0.215 #nmap -sV <target-ip>
```

### firewall and IDS testing
```bash
# scan a host with a stealth scan
nmap -sS 192.168.0.215 #nmap -sS <target-ip>
# scan for firewall rules : determine if a host is protected by a firewall
nmap -sA 192.168.0.215 #nmap -sA <target-ip>

```

## outcome : nmap
### example
```bash
(base) jieunpark@eng---macbook files % nmap -F 192.168.0.1
Starting Nmap 7.95 ( https://nmap.org ) at 2024-11-19 09:31 CET
Nmap scan report for kabelbox.local (192.168.0.1)
Host is up (0.0032s latency).
Not shown: 95 closed tcp ports (conn-refused)
PORT    STATE    SERVICE
22/tcp  filtered ssh
23/tcp  filtered telnet
53/tcp  open     domain
80/tcp  open     http
111/tcp filtered rpcbind
````
### port details
```bash
PORT	STATE	SERVICE	DESCRIPTION

22/tcp	Filtered	SSH	The port is filtered, meaning it might be blocked by a firewall or access control. SSH is often used for secure remote access to devices.

23/tcp	Filtered	Telnet	Similar to port 22, this port is filtered. Telnet is less secure than SSH and rarely used on modern systems due to its vulnerabilities.

53/tcp	Open	Domain (DNS)	This indicates a DNS service is running. This is normal for routers or devices acting as DNS servers.

80/tcp	Open	HTTP	A web server is running on this port. It might be hosting an admin panel or other web services.

111/tcp	Filtered	RPCBind	RPCBind is used by certain remote procedure call (RPC) services. Its filtered state suggests it’s being protected by a firewall.