# � Math Calculation Engine

A modular, extensible Python math engine that supports intuitive, dynamic, but strict calculations via a central `calculate()` function. Perfect for both programmatic use and interactive exploration!

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## ✨ Key Features

- 🎯 **Strict Argument Validation** - Enforces exact argument names per operation
- 🧩 **Modular Design** - Easy to extend with new operations and formulas  
- 🔢 **Multiple Interfaces** - CLI, interactive mode, Jupyter notebook, and programmatic API
- ⚡ **Fast & Reliable** - Comprehensive error handling and validation
- 📚 **Well Documented** - Complete examples and interactive tutorials
- 🎨 **Clean API** - Intuitive operation enum system

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/CalcModule.git
   cd CalcModule
   ```
2. **Install requirements (for notebook support):**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the engine:**
   - Demo: `python calc.py --demo`
   - Interactive: `python calc.py --interactive`
   - Notebook: `python calc.py --notebook`
   - List operations: `python calc.py --list`
   - Import in Python:
     ```python
     from core import calculate, Operation
     result = calculate(operation=Operation.ADD, a=2, b=3)
     ```

## 🎮 Usage Modes

### 1. Command Line Interface

```bash
# Run demonstration calculations
python calc.py

# Interactive calculation mode  
python calc.py --interactive

# Launch Jupyter notebook
python calc.py --notebook

# List all available operations
python calc.py --list

# Show help
python calc.py --help
```

### 2. Programmatic Usage

```python
from core import calculate, Operation, list_operations

# Perform calculations
result = calculate(operation=Operation.MULTIPLY, a=7, b=8)

# Get operation information
operations = list_operations()
for op in operations:
    print(f"{op['operation'].name}: {op['required_args']}")
```

### 3. Interactive Jupyter Notebook

Launch the interactive notebook for hands-on exploration:

```bash
python calc.py --notebook
```

## 📊 Supported Operations

### Arithmetic Operations
- `ADD` - Addition (a, b)
- `SUBTRACT` - Subtraction (a, b)  
- `MULTIPLY` - Multiplication (a, b)
- `DIVIDE` - Division (a, b)
- `POWER` - Exponentiation (num, power)
- `SQUARE_ROOT` - Square root (num)

### Geometry Operations  
- `AREA_CIRCLE` - Circle area (radius)
- `AREA_RECTANGLE` - Rectangle area (length, width)
- `AREA_TRIANGLE` - Triangle area (base, height)
- `CIRCUMFERENCE_CIRCLE` - Circle circumference (radius)
- `PERIMETER_RECTANGLE` - Rectangle perimeter (length, width)

## 🏗️ Project Structure

```
CalcModule/
├── calc.py                        # Main CLI entry point
├── main.py                        # Sample usage script
├── math_engine_notebook.ipynb     # Interactive Jupyter notebook
├── README.md                      # This documentation
├── LICENSE                        # MIT License
└── core/                          # Core engine modules
    ├── __init__.py               # Package initialization
    ├── calculate.py              # Main calculation dispatcher
    ├── operations.py             # Operation enum and mapping
    └── formulas/                 # Mathematical formulas
        ├── __init__.py
        ├── arithmetic.py         # Basic arithmetic operations
        └── geometry.py           # Geometric calculations
```

## 🔧 Architecture

### Core Components

#### 1. Operation Enum System
```python
from enum import Enum, auto

class Operation(Enum):
    ADD = auto()
    AREA_CIRCLE = auto()
    POWER = auto()
    # ... more operations
```

#### 2. Operation Mapping
```python
OPERATION_MAP = {
    Operation.ADD: {
        "func": add,
        "required": ["a", "b"]
    },
    Operation.AREA_CIRCLE: {
        "func": area_circle,
        "required": ["radius"]
    }
    # ... more mappings
}
```

#### 3. Central Calculate Function
```python
def calculate(*, operation, **kwargs):
    """
    Central calculation dispatcher with strict validation.
    
    Args:
        operation: Operation enum value
        **kwargs: Named arguments for the operation
        
    Returns:
        Calculation result
        
    Raises:
        ValueError: For missing/unexpected args or calculation errors
    """
    # Validation and dispatch logic
```

## 🛡️ Error Handling

The engine provides comprehensive error handling:

```python
# Missing required arguments
try:
    calculate(operation=Operation.ADD, a=5)  # Missing 'b'
except ValueError as e:
    print(e)  # "Missing required arguments: b"

# Unexpected arguments  
try:
    calculate(operation=Operation.ADD, a=5, b=3, c=1)  # 'c' unexpected
except ValueError as e:
    print(e)  # "Unexpected arguments: c"

# Mathematical errors
try:
    calculate(operation=Operation.DIVIDE, a=10, b=0)
except ValueError as e:
    print(e)  # "Calculation error: Division by zero is not allowed"
```

## 🔌 Extending the Engine

### Adding New Operations

1. **Create the function** in appropriate formula module:
```python
# In core/formulas/arithmetic.py
def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial of negative number undefined")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

2. **Add to Operation enum**:
```python
# In core/operations.py
class Operation(Enum):
    # ... existing operations
    FACTORIAL = auto()
```

3. **Update operation mapping**:
```python
# In core/operations.py
OPERATION_MAP = {
    # ... existing mappings
    Operation.FACTORIAL: {
        "func": factorial,
        "required": ["n"]
    }
}
```

4. **Import the function**:
```python
# In core/operations.py
from .formulas.arithmetic import add, subtract, ..., factorial
```

### Adding New Formula Categories

Create new modules in `core/formulas/` for different mathematical domains:

- `statistics.py` - Mean, median, standard deviation
- `trigonometry.py` - Sin, cos, tan functions  
- `calculus.py` - Derivatives, integrals
- `algebra.py` - Equation solving, matrix operations

## 📚 Examples

### Complex Calculations

```python
# Calculate compound interest
principal = 1000
rate = 1.05  # 5% annual interest
years = 10

# A = P(1 + r)^t  
amount = calculate(operation=Operation.MULTIPLY,
                  a=principal,
                  b=calculate(operation=Operation.POWER, num=rate, power=years))

print(f"Amount after {years} years: ${amount:.2f}")
```

### Geometric Problem Solving

```python
# Calculate garden area with walkway
garden_radius = 5
walkway_width = 2
total_radius = garden_radius + walkway_width

garden_area = calculate(operation=Operation.AREA_CIRCLE, radius=garden_radius)
total_area = calculate(operation=Operation.AREA_CIRCLE, radius=total_radius)
walkway_area = calculate(operation=Operation.SUBTRACT, a=total_area, b=garden_area)

print(f"Walkway area: {walkway_area:.2f} m²")
```

## 🧪 Testing

Run the built-in tests and demonstrations:

```bash
# Run demo calculations
python calc.py --demo

# Test with sample script
python main.py

# Interactive testing
python calc.py --interactive
```

## 📖 Learning Resources

1. **Interactive Notebook**: `python calc.py --notebook`
2. **CLI Help**: `python calc.py --help`  
3. **Sample Script**: `python main.py`
4. **Source Code**: Explore the `core/` directory

## 🤝 Contributing

Contributions are welcome! To add a new formula or feature:

1. Fork the repository and create a new branch.
2. Add your formula to the appropriate file in `core/formulas/`.
3. Add an entry to `core/operations.py` (enum and OPERATION_MAP).
4. Add a test or example in `main.py` or the notebook.
5. Submit a pull request with a clear description.

Please follow the code style and add docstrings for new functions.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python's powerful enum and dynamic dispatch capabilities
- Inspired by scientific computing libraries like NumPy and SciPy
- Designed for educational use and practical applications

## 📞 Support

- � **Issues**: [GitHub Issues](https://github.com/yourusername/CalcModule/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/CalcModule/discussions)  
- 📧 **Email**: your.email@example.com

---

**Happy Calculating!** 🧮✨

- ✅ Dynamic but strict `calculate()` function
- 📘 Clear, readable, and self-documenting syntax
- 🧩 Modular design using Enums and mapped operations
- 🛠️ Easily expandable with new operations
- 🧪 Built-in error handling for missing/extra parameters
- 🧠 Great for CLI tools, web apps, or educational tools

---

## 📦 Installation

Clone or download the repository:

```bash
git clone https://github.com/your-username/math-engine.git
cd math-engine
```

Run the engine:

```bash
python start.py
```

---

## 🧠 Usage Example

```python
from core.calculate import calculate
from core.operations import Operation

# Circle Area
result = calculate(operation=Operation.AREA_CIRCLE, radius=10)
print(result)  # ➝ 314.159...

# Power Calculation
print(calculate(operation=Operation.POWER, num=2, power=3))  # ➝ 8

# Addition
print(calculate(operation=Operation.ADD, a=4, b=6))  # ➝ 10
```

---

## 🎯 Supported Operations

| Operation Enum        | Required Args     | Example Call                                       |
|-----------------------|-------------------|----------------------------------------------------|
| `Operation.AREA_CIRCLE` | `radius`         | `calculate(operation=Operation.AREA_CIRCLE, radius=10)` |
| `Operation.POWER`       | `num`, `power`   | `calculate(operation=Operation.POWER, num=2, power=3)` |
| `Operation.ADD`         | `a`, `b`         | `calculate(operation=Operation.ADD, a=5, b=3)`         |

---

## 🧰 Project Structure

```
math_engine/
├── main.py                     # Demo usage
├── start.py                    # CLI entry point with help output
├── README.md                   # Documentation
├── core/
│   ├── calculate.py            # Core dispatcher
│   ├── operations.py           # Enum + operation map
│   └── formulas/
│       ├── arithmetic.py       # Arithmetic logic
│       └── geometry.py         # Geometry logic
```

---

## 🛠️ Adding New Operations

1. Create your function inside `core/formulas/`
2. Add it to the `OPERATION_MAP` in `core/operations.py`
3. Register its required arguments
4. Use `calculate()` with your new `Operation` Enum

---

## 🧑‍💻 Contributing

Pull requests are welcome! If you want to add more math categories (e.g. Trigonometry, Algebra, Statistics), feel free to fork and expand.

---

## 📄 License

MIT License. Use freely and contribute!

