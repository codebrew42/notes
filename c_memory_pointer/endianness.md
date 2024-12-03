# endianness

## little endian
### definition
- the least significant value(the rightmost one) will be stored first(the lowest address)

### example
- Let's say we have a 4-byte integer: 0x12345678
- Adress:	0x00	0x01	0x02	0x03
- Value:	78		56		34		12

## big endian
### definition
- the most significant value(the leftmost one) will be stored first(the lowest address)

### example
- Let's say we have a 4-byte integer: 0x12345678
- Adress:	0x00	0x01	0x02	0x03
- Value:	12		34		56		78

## why is it important?
- it affects the way we access the memory
- in C, the endianness of the machine can be checked by `#include <endian.h>`

## Any pros and cons?
- little endian is more common because most modern CPUs are little endian
- big endian is used in some special cases, such as networking protocols

## Why little endian is more common?
- This can make it easier for certain operations, like incrementing a number, because the least significant byte is accessed first. However, when interpreting the entire number, it may seem less intuitive since the most significant byte is at a higher address.