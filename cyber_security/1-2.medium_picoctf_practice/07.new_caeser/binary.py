import string

binary1 = "{0:08b}".format(ord('c'))
#binary = "{1:08b}".format(ord('c')) #wrong
binary2 = "{0:08b}".format(ord('A'))
binary3 = "{0:08b}".format(ord('!'))
binary4 = "{0:07b}".format(ord('!'))
binary5 = "{0:06b}".format(ord('!'))
binary6 = "{0:05b}".format(ord('!'))

print(binary1)
print(binary2)
print(binary3)
print(binary4)
print(binary5)
print(binary6)

int = 5
formatted1 = "int is {:05}".format(int)

name = "Jin"
formatted2 = "{} is my name".format(name)

print("\n", formatted1)
print(formatted2)