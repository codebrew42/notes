#`output.append()` and `output +=` 
- the choice depends on the datatype
## 1. `output.append()`
- **Usage**: This method is used with **lists**.
- **Functionality**: It adds a single element to the end of the list.
- **Example**:
    ```python
    output = []
    output.append('a')  # output is now ['a']
    output.append('b')  # output is now ['a', 'b']
    ```

## 2. `output +=`
- **Usage**: This operator can be used with **strings**, **lists**, and other iterable types.
- **Functionality**: It concatenates the right-hand operand to the left-hand operand. For strings, it combines them into a new string. For lists, it extends the list with elements from the iterable on the right.
- **Example with Strings**:
    ```python
    output = "Hello"
    output += " World"  # output is now "Hello World"
    ```
- **Example with Lists**:
    ```python
    output = [1, 2]
    output += [3, 4]  # output is now [1, 2, 3, 4]
    ```

## Key Differences
- **Data Type**: 
  - `append()` is specific to lists, while `+=` can be used with strings, lists, and other iterable types.
  
- **Return Value**:
  - `append()` modifies the list in place and returns `None`.
  - `+=` modifies the original object (string or list) in place and does not return a new object.

- **Performance**:
  - Using `append()` in a loop is generally more efficient for lists than using `+=` because `+=` creates a new list each time it is called.
  - For strings, using `+=` is often less efficient in a loop because strings are immutable in Python, and each concatenation creates a new string. In such cases, it is better to use a list to collect parts and then join them at the end.

## Conclusion
- Use `output.append()` when you are working with lists
- Use `output +=` when you are working with strings or a list with multiple elements