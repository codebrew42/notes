# how to check ip address

```bash
ip addr
```

```bash
ip -4 addr
```

```bash
ipconfig getifaddr en0
ifconfig en0
```

# output: 'ipconfig'
````
(base) jieunpark@eng---macbook files % ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000 
	inet6 ::1 prefixlen 128 
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
	nd6 options=201<PERFORMNUD,DAD>
gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
stf0: flags=0<> mtu 1280
anpi0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether d6:f8:6a:1c:30:44 
	inet6 fe80::d4f8:6aff:fe1c:3044%anpi0 prefixlen 64 scopeid 0x4 
	nd6 options=201<PERFORMNUD,DAD>
	media: none
	status: inactive
anpi1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether d6:f8:6a:1c:30:45 
	inet6 fe80::d4f8:6aff:fe1c:3045%anpi1 prefixlen 64 scopeid 0x5 
	nd6 options=201<PERFORMNUD,DAD>
	media: none
	status: inactive
en3: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether d6:f8:6a:1c:30:24 
	nd6 options=201<PERFORMNUD,DAD>
	media: none
	status: inactive
en4: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether d6:f8:6a:1c:30:25 
	nd6 options=201<PERFORMNUD,DAD>
	media: none
	status: inactive
en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 36:a4:53:3b:26:80 
	media: autoselect <full-duplex>
	status: inactive
en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
	options=460<TSO4,TSO6,CHANNEL_IO>
	ether 36:a4:53:3b:26:84 
	media: autoselect <full-duplex>
	status: inactive
ap1: flags=8802<BROADCAST,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether e2:95:6d:3f:c6:70 
	media: autoselect
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6463<RXCSUM,TXCSUM,TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether c0:95:6d:3f:c6:70 
	inet6 fe80::82d:c005:74f9:db76%en0 prefixlen 64 secured scopeid 0xb 
	inet 192.168.0.215 netmask 0xffffff00 broadcast 192.168.0.255
	inet6 2a02:8109:9f12:e200:10f0:1698:d19f:81a1 prefixlen 64 autoconf secured 
	inet6 2a02:8109:9f12:e200:3536:5844:9840:1721 prefixlen 64 autoconf temporary 
	inet6 2a02:8109:9f12:e200::f693 prefixlen 64 dynamic 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
	ether 36:a4:53:3b:26:80 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x0
	member: en1 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 8 priority 0 path cost 0
	member: en2 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 9 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: <unknown type>
	status: inactive
awdl0: flags=8843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6463<RXCSUM,TXCSUM,TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether 0e:74:da:cb:70:56 
	inet6 fe80::c74:daff:fecb:7056%awdl0 prefixlen 64 scopeid 0xd 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
llw0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=400<CHANNEL_IO>
	ether 0e:74:da:cb:70:56 
	inet6 fe80::c74:daff:fecb:7056%llw0 prefixlen 64 scopeid 0xe 
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: inactive
utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::376d:fa99:d404:a85%utun0 prefixlen 64 scopeid 0xf 
	nd6 options=201<PERFORMNUD,DAD>
utun1: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 2000
	inet6 fe80::583:fa3b:4b05:da1d%utun1 prefixlen 64 scopeid 0x10 
	nd6 options=201<PERFORMNUD,DAD>
utun2: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1000
	inet6 fe80::ce81:b1c:bd2c:69e%utun2 prefixlen 64 scopeid 0x11 
	nd6 options=201<PERFORMNUD,DAD>
utun3: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::edea:b501:62bc:a088%utun3 prefixlen 64 scopeid 0x12 
	nd6 options=201<PERFORMNUD,DAD>
utun4: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1380
	inet6 fe80::3d24:ca29:4a10:6505%utun4 prefixlen 64 scopeid 0x13 
	nd6 options=201<PERFORMNUD,DAD>
```
## keysection
### interface names: lo0, en0, en1, utun0, awdl0
- different network interfaces
- lo0: loopback interface (for internall communication within the machine, e.g., 127.0.0.1)
- en0: primary Ethernet or wifi interface
- en1: secondary wifi interface
- utun0: tunnel interface (often used for VPN connections)
- awdl0: Apple Wireless Direct Link (used for wireless communication between devices: AirDrop...)

### en0
- en0 shows 192.168.0.215 as its IPv4 address, meaning this is your device's local IP address on your home network.
- Understanding this helps you identify entry points for penetration testing.

### Flags : UP, BROADCAST, SMART, RUNNING, SIMPLEX, MULTICAST
- UP: interface is up and running (active)
- BROADCAST: interface is operating in broadcast mode
- SMART: interface is using the TCP/IP protocol suite
- RUNNING: interface is in an active state
- SIMPLEX: interface is not a point-to-point connection
- MULTICAST: interface supports multicast communication (multicast packest) which can be used in streaming or broadcasting

-> UP and Running : These are the ones you can interact with or exploit if there are vulnerabilities.

### IP address
- inet 192.168.0.215 : This is the IPv4 address of the interface. It's the address you'd use to connect to the internet from your home network.
- inet6 fe80::82d:c005:74f9:db76%en0 : This is the IPv6 address of the interface. (=local IPv6 address)
- netmask 0xffffff00 : This is the subnet mask. It defines which part of the IP address is used for the network and which part is used for the host. (decimal form : 255.255.255.0)
- broadcast 192.168.0.255 : This is the broadcast address for the network. It's used to send messages/packets to all devices on the same network.

-> 192.168.x.x : this range is private, it indicates that you are on a local network.

-> broadcast address : 192.168.0.255 : it can be used for network scanning tools like nmap.
	- what is *nmap*? nmap is a network scanner that can be used to scan the network for open ports, services, and other information.

### MAC address
- ether c0:95:6d:3f:c6:70 : This is the (physical) MAC address of the interface 'en0'. It's a unique identifier for the network interface card (NIC) on your device.
- MAC address is used to identify the device on the network. It is unique to each network device.

-> macchanger : you can spoof a MAC address to hide your device's identity on the network.

### MTU (Maximum Transmission Unit) : mtu 1500
- this defines the maximum size of the packet that can be sent on the network.
- smaller MTU can cause fragmentation of packets, which can degrade network performance.
- default MTU for most networks is 1500 bytes.
- Adjusting MTU can be useful for troubleshooting network issues or optimizing performance, but it should be done with caution as incorrect settings can disrupt network connectivity.

-> some hacker exploits involve manipulating the MTU value to disrupt network communications or gain unauthorized access, making them harder to inspect by firewall or IDS(Intrusion Detection System).

### inet6 (IPv6 address)
- modern systems uses IPv6 address, which creates more challenges for network security tools that are designed to work with IPv4 due to its complexity.

-> tools like *nmap*, *Wireshark*, and *Metasploit* have been updated to support IPv6, but they may still have limitations or require specific configurations to fully utilize IPv6 scanning and exploitation capabilities.

