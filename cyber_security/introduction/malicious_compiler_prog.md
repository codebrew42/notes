### proccess: basic

when putting a piece of sftware in a translator

cases: source ->  compiler -> object
	(1)	clean -> clean -> clean
	(2) dirty -> clean -> dirty
	(2) clean -> dirty -> dirty too !

solution 
	case(2): see the code

### ken thompson
computer scientist
contributions to the development of Unix, prog languages

## concept of malicious compiler
modified ver of a compiler
can 
	(1)insert vulnerabilities/backdoors into the code it compiles 
	(2)alter the behaviors of prog, making it a serious security risk
even without programmer's knowledge

highlighted this concern in 1984 talk @ ACM Turing award lecture
	: even compilers can be compromised, leading to potential security vulnerabilities in the final software products

### how to prevent

## to investigate the types of security safeguards that might reduce the pos of infected compilers

# compiler testing

- thorough testing can help identify some malicious behavior/bugs
- may not be very effective at detecting
- has a low probability of detecting

# tougher vendor contract requirements / impose contracts
- implementing stricter requirements for vendors
- includes regular audits, serc assessments, clear penalties for breaches
- effectiveness depends on how rigourously these requirements are enforced, monitored
- may not catch all instances of malicious behavior
- the most effective

# multiple compiler vendors

- provide some rebundancy, decrease the risk 
- the prob. of detecting: low
