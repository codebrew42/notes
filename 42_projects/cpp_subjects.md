# C++ Module 02: Ad-hoc Polymorphism, Operator Overloading, and the Orthodox Canonical Class Form

## Table of Contents

* [Introduction](#introduction)
* [General Rules](#general-rules)
* [New Rules: Orthodox Canonical Form](#new-rules-orthodox-canonical-form)
* [Exercise 00: My First Class in Orthodox Canonical Form](#exercise-00-my-first-class-in-orthodox-canonical-form)
* [Exercise 01: Towards a More Useful Fixed-Point Number Class](#exercise-01-towards-a-more-useful-fixed-point-number-class)
* [Exercise 02: Now We’re Talking (Operator Overloads)](#exercise-02-now-we%E2%80%99re-talking-operator-overloads)
* [Exercise 03: BSP (Point-in-Triangle Test)](#exercise-03-bsp-point-in-triangle-test)

---

## Introduction

C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C language. Module 02 introduces:

1. **Ad-hoc polymorphism** via operator overloading.
2. The **Orthodox Canonical Form** for classes (default ctor, copy ctor, copy assignment, destructor).
3. Building a **fixed-point** number class (`Fixed`) and a **Point** class, then using them in exercises.

*Standard:* C++98 (no C++11 or Boost).

---

## General Rules

* **Compilation flags:** `-Wall -Wextra -Werror` and `-std=c++98`.
* **Naming conventions:**

  * Directories: `ex00`, `ex01`, …
  * Class names: `UpperCamelCase` → files `ClassName.hpp` / `ClassName.cpp`.
* **Forbidden:**

  * C functions: `printf`, `malloc`, `free`.
  * `using namespace` and `friend` (unless stated).
  * STL containers and algorithms until Module 08.
* **Memory management:** No leaks; if `new` is used, ensure matching `delete`.
* **Header hygiene:** Include guards; no function definitions in headers (except templates).

---

## New Rules: Orthodox Canonical Form

All classes (unless noted) must implement:

1. **Default constructor**
2. **Copy constructor**
3. **Copy assignment operator**
4. **Destructor**

Split class into header (`.hpp`) and source (`.cpp`).

---

## Exercise 00: My First Class in Orthodox Canonical Form

**Goal:** Create a `Fixed` class representing a fixed-point number with 8 fractional bits.

### Requirements

* **Private members:**

  * `int _value;`  // raw fixed-point
  * `static const int _fractionalBits = 8;`
* **Public members:**

  * Default ctor → `_value = 0`
  * Copy ctor, copy assignment, destructor (Orthodox Form)
  * `int getRawBits() const;`
  * `void setRawBits(int raw);`

### Example Implementation

<details>
<summary><code>Fixed.hpp</code></summary>
```cpp
#ifndef FIXED_HPP
#define FIXED_HPP

class Fixed {
private:
int                 \_value;
static const int    \_fractionalBits = 8;
public:
Fixed();
Fixed(const Fixed& other);
Fixed& operator=(const Fixed& other);
\~Fixed();

```
int getRawBits() const;
void setRawBits(int raw);
```

};

\#endif // FIXED\_HPP

````
</details>

<details>
<summary><code>Fixed.cpp</code></summary>
```cpp
#include "Fixed.hpp"
#include <iostream>

Fixed::Fixed() : _value(0) {
    std::cout << "Default constructor called" << std::endl;
}

Fixed::Fixed(const Fixed& other) {
    std::cout << "Copy constructor called" << std::endl;
    *this = other;
}

Fixed& Fixed::operator=(const Fixed& other) {
    std::cout << "Copy assignment operator called" << std::endl;
    if (this != &other)
        _value = other.getRawBits();
    return *this;
}

Fixed::~Fixed() {
    std::cout << "Destructor called" << std::endl;
}

int Fixed::getRawBits() const {
    std::cout << "getRawBits member function called" << std::endl;
    return _value;
}

void Fixed::setRawBits(int raw) {
    _value = raw;
}
````

</details>

<details>
<summary><code>main.cpp</code></summary>
```cpp
#include <iostream>
#include "Fixed.hpp"

int main() {
Fixed a;
Fixed b(a);
Fixed c;
c = b;

```
std::cout << a.getRawBits() << std::endl;
std::cout << b.getRawBits() << std::endl;
std::cout << c.getRawBits() << std::endl;
return 0;
```

}

```
</details>

**Sample Output:**
```

Default constructor called
Copy constructor called
Copy assignment operator called
getRawBits member function called
0
getRawBits member function called
0
getRawBits member function called
0
Destructor called
Destructor called
Destructor called

````

---

## Exercise 01: Towards a More Useful Fixed-Point Number Class

**Enhancements:**
- **Constructors:**
  - `Fixed(int)` converts integer → fixed-point.
  - `Fixed(float)` converts float → fixed-point (use `roundf`).
- **Member functions:**
  - `float toFloat() const;`
  - `int toInt() const;`
- **Operator:**
  - Overload `<<` to output the float representation.

### Example Additions

```cpp
// In Fixed.hpp (inside class Fixed)
Fixed(int const intVal);
Fixed(float const floatVal);
float toFloat() const;
int toInt() const;

// Outside class
std::ostream& operator<<(std::ostream& os, Fixed const& fx);
````

```cpp
// In Fixed.cpp
#include <cmath>

Fixed::Fixed(int const intVal) {
    std::cout << "Int constructor called" << std::endl;
    _value = intVal << _fractionalBits;
}

Fixed::Fixed(float const floatVal) {
    std::cout << "Float constructor called" << std::endl;
    _value = roundf(floatVal * (1 << _fractionalBits));
}

float Fixed::toFloat() const {
    return static_cast<float>(_value) / (1 << _fractionalBits);
}

int Fixed::toInt() const {
    return _value >> _fractionalBits;
}

std::ostream& operator<<(std::ostream& os, Fixed const& fx) {
    os << fx.toFloat();
    return os;
}
```

**Usage Example:**

```cpp
Fixed a;
Fixed const b(10);
Fixed const c(42.42f);
Fixed const d(b);
a = Fixed(1234.4321f);

std::cout << "a is " << a << std::endl;
std::cout << "b is " << b << std::endl;
std::cout << "c is " << c << std::endl;
std::cout << "d is " << d << std::endl;

std::cout << "a is " << a.toInt() << " as integer" << std::endl;
```

**Expected Output:**

```
Int constructor called
Float constructor called
Copy constructor called
Copy assignment operator called
a is 1234.43
b is 10
c is 42.4219
d is 10
a is 1234 as integer
```

---

## Exercise 02: Now We’re Talking (Operator Overloads)

**Add to `Fixed` class:**

1. **Comparison operators:** `>`, `<`, `>=`, `<=`, `==`, `!=`.
2. **Arithmetic operators:** `+`, `-`, `*`, `/`.
3. **Increment/decrement:** pre- and post- `++`, `--`.
4. **Static min/max:**

   ```cpp
   static Fixed& min(Fixed& a, Fixed& b);
   static const Fixed& min(Fixed const& a, Fixed const& b);
   static Fixed& max(Fixed& a, Fixed& b);
   static const Fixed& max(Fixed const& a, Fixed const& b);
   ```

### Usage Example

```cpp
Fixed a;
Fixed const b(Fixed(5.05f) * Fixed(2));

std::cout << a << std::endl;    // 0
std::cout << ++a << std::endl;  // 0.00390625
std::cout << a << std::endl;    // 0.00390625
std::cout << a++ << std::endl;  // 0.00390625
std::cout << a << std::endl;    // 0.0078125

std::cout << b << std::endl;    // 10.1016
std::cout << Fixed::max(a, b) << std::endl; // 10.1016
```

> *Note:* Division by zero may crash.

---

## Exercise 03: BSP (Point-in-Triangle Test)

**Goal:** Determine if a point lies strictly inside a triangle (not on edges).

### `Point` Class (Orthodox Form)

```cpp
class Point {
private:
    Fixed const _x;
    Fixed const _y;
public:
    Point();
    Point(float x, float y);
    Point(Point const& other);
    Point& operator=(Point const& other);
    ~Point();

    Fixed getX() const;
    Fixed getY() const;
};
```

### `bsp` Function

```cpp
bool bsp(Point const a, Point const b, Point const c, Point const point);
```

Use barycentric technique or area comparisons:

```cpp
// Compute area of triangle
Fixed area = ...;
// Sum areas of sub-triangles and compare
```

### Test Example

```cpp
Point a(0, 0), b(10, 0), c(0, 10);
Point inside(3, 3);
Point outside(10, 10);

std::cout << std::boolalpha;
std::cout << bsp(a, b, c, inside)  << std::endl; // true
std::cout << bsp(a, b, c, outside) << std::endl; // false
```

