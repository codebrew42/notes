# ssh

## how to ssh? 
### ssh command
ssh ctf-player@titan.picoctf.net -p 65118
	username@hostname + specifies the port (-p)

## SSH (secure shell) protocol
### def
- cryptographic network protocol 

### purpose
- to secure communication btw two netwroked devices
- often used for remote logins, file transfers

### security mechanism
- uses (1)encryption to protect data
- (2)authentification to verify identities
- (3) integrity checks to ensure data isn't tempered with during transmission

### public key
- server's fingerprint = hash of its public key
-> by storing it locally in 'known_hosts', SSH prevents "man in the middle attack" 
- uses public key cryptogrphy to verify the identity of the server you're connecting to


### possible warnings
	“The authenticity of host '[titan.picoctf.net]:65118' can't be established.” 
-> computer has never connected to the host before, and it doesn't have the host's public key in its 'known_hosts' file

## Fingerprint
### ED25519 key fingerprint
- unique identifier/fingerprint for the server's key
-> if you type yes, it confirms you trust the server
-> the fingerprint will be added to 'known_hosts'file

- can be trade-off: you accept the risk based on your trust in the server's identity