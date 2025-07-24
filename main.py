#!/usr/bin/env python3
"""
Sample script demonstrating the Math Calculation Engine usage.
Shows how to use the calculate() function programmatically.
"""

from core import calculate, Operation, list_operations


def main():
    """Main demonstration function."""
    print("🧮 Math Calculation Engine - Sample Usage")
    print("=" * 50)
    
    # Basic arithmetic examples
    print(f"\n📊 ARITHMETIC OPERATIONS")
    print(f"-" * 25)
    
    try:
        # Addition
        result = calculate(operation=Operation.ADD, a=25, b=17)
        print(f"25 + 17 = {result}")
        
        # Subtraction  
        result = calculate(operation=Operation.SUBTRACT, a=100, b=23)
        print(f"100 - 23 = {result}")
        
        # Multiplication
        result = calculate(operation=Operation.MULTIPLY, a=7, b=8)
        print(f"7 × 8 = {result}")
        
        # Division
        result = calculate(operation=Operation.DIVIDE, a=144, b=12)
        print(f"144 ÷ 12 = {result}")
        
        # Power
        result = calculate(operation=Operation.POWER, num=2, power=8)
        print(f"2^8 = {result}")
        
        # Square root
        result = calculate(operation=Operation.SQUARE_ROOT, num=81)
        print(f"√81 = {result}")
        
    except Exception as e:
        print(f"Arithmetic error: {e}")
    
    # Geometry examples
    print(f"\n📐 GEOMETRY OPERATIONS")
    print(f"-" * 22)
    
    try:
        # Circle area
        radius = 7.5
        area = calculate(operation=Operation.AREA_CIRCLE, radius=radius)
        print(f"Circle area (r={radius}): {area:.2f}")
        
        # Circle circumference
        circumference = calculate(operation=Operation.CIRCUMFERENCE_CIRCLE, radius=radius)
        print(f"Circle circumference (r={radius}): {circumference:.2f}")
        
        # Rectangle area
        length, width = 12, 8
        area = calculate(operation=Operation.AREA_RECTANGLE, length=length, width=width)
        print(f"Rectangle area ({length}×{width}): {area}")
        
        # Rectangle perimeter
        perimeter = calculate(operation=Operation.PERIMETER_RECTANGLE, length=length, width=width)
        print(f"Rectangle perimeter ({length}×{width}): {perimeter}")
        
        # Triangle area
        base, height = 10, 6
        area = calculate(operation=Operation.AREA_TRIANGLE, base=base, height=height)
        print(f"Triangle area (b={base}, h={height}): {area}")
        
    except Exception as e:
        print(f"Geometry error: {e}")
    
    # Error handling examples
    print(f"\n⚠️  ERROR HANDLING EXAMPLES")
    print(f"-" * 26)
    
    # Missing argument
    try:
        calculate(operation=Operation.ADD, a=5)  # Missing 'b'
    except ValueError as e:
        print(f"Missing argument: {e}")
    
    # Unexpected argument
    try:
        calculate(operation=Operation.ADD, a=5, b=3, c=1)  # 'c' not expected
    except ValueError as e:
        print(f"Unexpected argument: {e}")
    
    # Division by zero
    try:
        calculate(operation=Operation.DIVIDE, a=10, b=0)
    except ValueError as e:
        print(f"Division by zero: {e}")
    
    # Negative radius
    try:
        calculate(operation=Operation.AREA_CIRCLE, radius=-5)
    except ValueError as e:
        print(f"Invalid input: {e}")
    
    # List available operations
    print(f"\n📋 AVAILABLE OPERATIONS")
    print(f"-" * 22)
    operations = list_operations()
    print(f"Total operations available: {len(operations)}")
    
    for op in operations[:5]:  # Show first 5
        print(f"• {op['operation'].name}: {', '.join(op['required_args'])}")
    
    if len(operations) > 5:
        print(f"... and {len(operations) - 5} more operations")
    
    print(f"\n✅ Sample script completed successfully!")
    print(f"💡 Try running: python calc.py --interactive")


if __name__ == "__main__":
    main()
