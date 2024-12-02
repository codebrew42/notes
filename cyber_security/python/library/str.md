# Key Features of the `string` Module

## String Constants

The `string` module includes several useful constants:

- **`string.ascii_letters`**: A string containing all ASCII letters (both lowercase and uppercase).
- **`string.ascii_lowercase`**: A string containing all lowercase ASCII letters (`'abcdefghijklmnopqrstuvwxyz'`).
- **`string.ascii_uppercase`**: A string containing all uppercase ASCII letters (`'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`).
- **`string.digits`**: A string containing all decimal digits (`'0123456789'`).
- **`string.punctuation`**: A string containing all punctuation characters.
- **`string.printable`**: A string containing all printable characters, including digits, letters, punctuation, and whitespace.

```python
import string

ALPHA_LOWER = string.ascii_lowercase[:16] #abcdefghijklmnop
DIGITS = string.digits[:16] #output: 0123456789abcdef
PRINTABLE = string.printable[:16] #0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

## converts char to binary : "{0:08b}".format(ord(c))
```python
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c)) #converts the character to its binary representation
		enc += ALPHABET[int(binary[:4], 2)] #the 1st 4 bits(msb), base 2
		enc += ALPHABET[int(binary[4:], 2)] #the last 4 bits(lsb)
	return enc


print("{0:08b}".format(ord('c'))) #01100011
print("{0:20b}".format(ord('c'))) #000000000001100011 *00000 ... is not shown
print("{0:05b}".format(ord('c'))) #11000011 *just truncates the leftmost bits 0
```
### explanation
- this code takes a string and encodes it in base16
- "{0:08b}".format(ord(c)) converts the character to its binary representation
	- why 0:08b? 0 is the character, 08 is the width, and b is the binary format
	- width? the width of the binary representation
	- why 8? because the character is 8 bits long



### Useful Functions

While the `string` module provides constants, Python also has built-in functions that are often used in conjunction with strings. Here are a couple of important ones:

#### 1. `ord()`

- **Description**: The `ord()` function takes a single character (a string of length 1) and returns its Unicode code point (an integer).
- **Usage**:
    ```python
    char = 'a'
    code_point = ord(char)  # Returns 97
    ```

#### 2. `format()`

- **Description**: The `format()` function is used to format strings. It allows you to embed expressions inside string literals, using curly braces `{}` as placeholders.
- **Usage**:
    ```python
    name = "Alice"
    age = 30
    formatted_string = "My name is {} and I am {} years old.".format(name, age)
	print(f'hi i am {name}')
    ```

### Example Usage

Here’s a simple example that demonstrates the use of the `string` module along with `ord()` and `format()`:

```python
import string

# Using string constants
alphabet = string.ascii_lowercase
print("Lowercase Alphabet:", alphabet)

# Using ord() to get the Unicode code point
for char in alphabet:
    print(f"The Unicode code point of '{char}' is {ord(char)}.")

# Using format() to create a formatted string
formatted_message = "The first letter of the alphabet is {}.".format(alphabet[0])
print(formatted_message)
```
