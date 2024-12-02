# function :  `int(nbr, base)` 
-to convert a value to an integer. It can take one or two arguments
-base is optional, default is 10

## Syntax

```python
int(x=0, base=10)
```

## Parameters

1. **`x`** (optional): value you want to convert to an integer
   - A string (e.g., `'123'`, `'10'`, `'0b101'` for binary).
   - A floating-point number (e.g., `3.14`).
   - If no argument is provided, it defaults to `0`.

2. **`base`** (optional)

## Examples

1. **Converting a String to an Integer**:
   ```python
   num = int('123')  # the string '123' to the integer 123
   ```

2. **Converting a Floating-Point Number**:
   ```python
   num = int(3.14)  # Converts the float 3.14 to the integer 3 (truncates the decimal part 소수점 잘라)
   ```

3. **Using Base for Conversion**:
   - **Binary to Decimal**:
     ```python
     binary_num = '1010'
     decimal_num = int(binary_num, 2)  # Converts binary '1010' to decimal 10
     ```
   - **Hexadecimal to Decimal**:
     ```python
     hex_num = '1A'
     decimal_num = int(hex_num, 16)  # Converts hexadecimal '1A' to decimal 26
     ```

4. **Default Behavior**:
   ```python
   num = int()  # Defaults to 0
   ```

### Summary

The `int()` function is versatile and can be used to convert various types of values into integers, with the option to specify the base for string representations of numbers. This makes it particularly useful for handling different numeral systems in programming.