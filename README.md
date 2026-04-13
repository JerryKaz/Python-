# Modern Scientific Calculator

A sleek, high-performance scientific calculator built with Python, featuring a modern dark-themed user interface.
This application leverages **CustomTkinter** for a polished look and the built-in **math module** for accurate scientific computations.

---

##  Features

* **Modern UI**
  Dark mode interface with rounded buttons and smooth hover effects.

* **Scientific Functions**
  Includes:

  * Trigonometry: `sin`, `cos`, `tan`
  * Logarithms (`log`)
  * Square roots (`√`)
  * Exponents (`^`)

* **Smart Trigonometry**
  Automatically converts degrees to radians for intuitive results.

* **Error Handling**
  Gracefully handles:

  * Division by zero
  * Invalid expressions

* **Responsive Design**
  Compact, clean layout optimized for desktop use (non-resizable window).

---

##  UI Preview

**Theme:** Deep Charcoal

**Color Coding:**

* Gray → Numeric digits
* Orange → Basic arithmetic operators
* Blue → Scientific functions
* Red → Clear/Delete
* Green → Equals/Result

---

##  Installation

### 1. Prerequisites

Ensure you have **Python 3.7 or higher** installed.

### 2. Install Dependencies

Install the required library using pip:

```bash
pip install customtkinter
```

---

## Usage

Run the application with:

```bash
python calculator.py
```

---

## Functionality Guide

| Button          | Function                                   |
| --------------- | ------------------------------------------ |
| sin / cos / tan | Trigonometric calculations (degrees input) |
| log             | Base-10 logarithm                          |
| ^               | Power function (e.g., 2 ^ 3 = 8)           |
| √               | Square root                                |
| π               | Constant Pi (~3.14159)                     |
| C               | Clear entire display                       |
| DEL             | Delete last character                      |

---

## Built With

* **CustomTkinter** – Modern UI components
* **Math Module** – Core mathematical logic

---

## License

This project is licensed under the **MIT License**.
See the `LICENSE` file for details.

---

## Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the project and submit a pull request.

---
