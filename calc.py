#!/usr/bin/env python3
"""
Math Calculation Engine - CLI Entry Point
==================================================

This is the main entry point for the Math Calculation Engine.
It provides both CLI functionality and optional Jupyter notebook launcher.

Usage:
    python calc.py                  # Run demo calculations
    python calc.py --notebook       # Launch Jupyter notebook
    python calc.py --help          # Show help information
    python calc.py --interactive   # Interactive mode

The engine can also be imported as a module:
    from core import calculate, Operation
    result = calculate(operation=Operation.ADD, a=5, b=3)
"""

import argparse
import sys
import subprocess
from pathlib import Path

# Import our calculation engine
from core import calculate, Operation, list_operations


def run_demo():
    """Run demonstration calculations to show engine capabilities."""
    print("🧮 Math Calculation Engine - Demo")
    print("=" * 50)
    
    demos = [
        # Basic Arithmetic
        {
            "description": "Basic Addition",
            "operation": Operation.ADD,
            "kwargs": {"a": 15, "b": 27}
        },
        {
            "description": "Power Calculation",
            "operation": Operation.POWER,
            "kwargs": {"num": 2, "power": 10}
        },
        {
            "description": "Factorial",
            "operation": Operation.FACTORIAL,
            "kwargs": {"n": 6}
        },
        
        # Geometry - Areas
        {
            "description": "Circle Area",
            "operation": Operation.AREA_CIRCLE,
            "kwargs": {"radius": 5}
        },
        {
            "description": "Trapezoid Area",
            "operation": Operation.AREA_TRAPEZOID,
            "kwargs": {"base1": 8, "base2": 12, "height": 5}
        },
        {
            "description": "Triangle Area (Heron's Formula)",
            "operation": Operation.AREA_TRIANGLE_HERON,
            "kwargs": {"a": 3, "b": 4, "c": 5}
        },
        
        # Volumes
        {
            "description": "Sphere Volume",
            "operation": Operation.VOLUME_SPHERE,
            "kwargs": {"radius": 3}
        },
        {
            "description": "Cylinder Volume",
            "operation": Operation.VOLUME_CYLINDER,
            "kwargs": {"radius": 2, "height": 8}
        },
        
        # Trigonometry
        {
            "description": "Sine 30 degrees",
            "operation": Operation.SIN_DEGREES,
            "kwargs": {"angle_degrees": 30}
        },
        {
            "description": "Convert 90° to Radians",
            "operation": Operation.DEGREES_TO_RADIANS,
            "kwargs": {"degrees": 90}
        },
        
        # Logarithms
        {
            "description": "Natural Logarithm of e",
            "operation": Operation.NATURAL_LOG,
            "kwargs": {"x": 2.718281828}
        },
        {
            "description": "Log Base 2 of 8",
            "operation": Operation.LOG_BASE_2,
            "kwargs": {"x": 8}
        },
        
        # Statistics
        {
            "description": "Mean of Dataset",
            "operation": Operation.MEAN,
            "kwargs": {"values": [10, 15, 20, 25, 30]}
        },
        {
            "description": "Standard Deviation (Sample)",
            "operation": Operation.STANDARD_DEVIATION_SAMPLE,
            "kwargs": {"values": [2, 4, 6, 8, 10]}
        },
        
        # Advanced Math
        {
            "description": "Combination C(10,3)",
            "operation": Operation.COMBINATION,
            "kwargs": {"n": 10, "r": 3}
        },
        {
            "description": "Distance Between Points",
            "operation": Operation.DISTANCE_2D,
            "kwargs": {"x1": 0, "y1": 0, "x2": 3, "y2": 4}
        }
    ]
    
    for demo in demos:
        try:
            result = calculate(operation=demo["operation"], **demo["kwargs"])
            if isinstance(result, float):
                result = round(result, 4)
            print(f"\n✅ {demo['description']}")
            print(f"   Operation: {demo['operation'].name}")
            print(f"   Input: {demo['kwargs']}")
            print(f"   Result: {result}")
        except Exception as e:
            print(f"\n❌ {demo['description']} - Error: {e}")
    
    operations = list_operations()
    print(f"\n🎉 Demo completed! The engine now supports {len(operations)} operations across multiple categories:")
    
    categories = {
        "Arithmetic": 0,
        "Geometry": 0, 
        "Trigonometry": 0,
        "Statistics": 0,
        "Logarithms": 0,
        "Volumes": 0
    }
    
    for op in operations:
        op_name = op['operation'].name
        if any(x in op_name for x in ['ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'POWER', 'FACTORIAL', 'COMBINATION']):
            categories["Arithmetic"] += 1
        elif any(x in op_name for x in ['AREA_', 'PERIMETER_', 'CIRCUMFERENCE', 'DISTANCE', 'SLOPE']):
            categories["Geometry"] += 1
        elif any(x in op_name for x in ['SIN_', 'COS_', 'TAN_', 'SEC_', 'CSC_', 'COT_', 'ASIN', 'ACOS', 'ATAN']):
            categories["Trigonometry"] += 1
        elif any(x in op_name for x in ['MEAN', 'MEDIAN', 'MODE', 'VARIANCE', 'STANDARD_DEVIATION', 'QUARTILE']):
            categories["Statistics"] += 1
        elif any(x in op_name for x in ['LOG_', 'NATURAL_LOG', 'EXPONENTIAL', 'SINH', 'COSH', 'TANH']):
            categories["Logarithms"] += 1
        elif any(x in op_name for x in ['VOLUME_', 'SURFACE_AREA']):
            categories["Volumes"] += 1
    
    for category, count in categories.items():
        if count > 0:
            print(f"   📊 {category}: {count} operations")


def launch_notebook():
    """Launch the Jupyter notebook for interactive exploration."""
    notebook_path = Path("math_engine_notebook.ipynb")
    
    if not notebook_path.exists():
        print("📓 Creating interactive notebook...")
        create_notebook()
    
    print("🚀 Launching Jupyter notebook...")
    try:
        subprocess.run(["jupyter", "notebook", str(notebook_path)], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to launch Jupyter. Make sure it's installed:")
        print("   pip install jupyter")
    except FileNotFoundError:
        print("❌ Jupyter not found. Install it with:")
        print("   pip install jupyter")


def create_notebook():
    """Create the interactive Jupyter notebook."""
    print("📓 Notebook already exists: math_engine_notebook.ipynb")
    print("💡 If you need to recreate it, delete the existing file first.")


def interactive_mode():
    """Run in interactive mode for custom calculations."""
    print("🔢 Interactive Math Calculation Engine")
    print("=" * 40)
    print("Available operations:")
    
    operations = list_operations()
    for i, op_info in enumerate(operations, 1):
        print(f"{i:2d}. {op_info['operation'].name} - requires: {', '.join(op_info['required_args'])}")
    
    print(f"\nType 'quit' or 'exit' to end session.")
    
    while True:
        try:
            print(f"\n--- New Calculation ---")
            op_choice = input("Enter operation name (or number): ").strip().upper()
            
            if op_choice in ['QUIT', 'EXIT', 'Q']:
                print("👋 Goodbye!")
                break
                
            # Handle numeric choice
            if op_choice.isdigit():
                op_num = int(op_choice)
                if 1 <= op_num <= len(operations):
                    operation = operations[op_num - 1]['operation']
                else:
                    print(f"❌ Invalid choice. Pick 1-{len(operations)}")
                    continue
            else:
                # Handle operation name
                try:
                    operation = Operation[op_choice]
                except KeyError:
                    print(f"❌ Unknown operation: {op_choice}")
                    continue
            
            # Get operation info
            op_info = next(info for info in operations if info['operation'] == operation)
            required_args = op_info['required_args']
            
            # Collect arguments
            kwargs = {}
            print(f"Operation: {operation.name}")
            print(f"Required arguments: {', '.join(required_args)}")
            
            for arg in required_args:
                while True:
                    try:
                        value = input(f"Enter {arg}: ").strip()
                        kwargs[arg] = float(value)
                        break
                    except ValueError:
                        print(f"❌ Please enter a valid number for {arg}")
            
            # Execute calculation
            result = calculate(operation=operation, **kwargs)
            print(f"✅ Result: {result}")
            
        except KeyboardInterrupt:
            print(f"\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


def show_help():
    """Show help information."""
    help_text = """
🧮 Math Calculation Engine Help
===============================

This is a modular, extensible Python math engine that supports both
programmatic use and interactive exploration.

COMMAND LINE OPTIONS:
  python calc.py                  Run demonstration calculations
  python calc.py --demo          Run demonstration calculations  
  python calc.py --notebook      Launch interactive Jupyter notebook
  python calc.py --interactive   Enter interactive calculation mode
  python calc.py --list          List all available operations
  python calc.py --help          Show this help message

PROGRAMMATIC USAGE:
  from core import calculate, Operation
  
  # Basic arithmetic
  result = calculate(operation=Operation.ADD, a=10, b=5)
  
  # Geometry
  area = calculate(operation=Operation.AREA_CIRCLE, radius=5)
  
  # Power calculations  
  power_result = calculate(operation=Operation.POWER, num=2, power=8)

FEATURES:
✅ Strict argument validation
✅ Extensible operation system
✅ Interactive Jupyter notebook
✅ CLI and programmatic interfaces
✅ Comprehensive error handling

For more information, see README.md
"""
    print(help_text)


def list_all_operations():
    """List all available operations with details."""
    print("📋 Available Operations")
    print("=" * 50)
    
    operations = list_operations()
    for op_info in operations:
        print(f"\n🔹 {op_info['operation'].name}")
        print(f"   Function: {op_info['function_name']}")
        print(f"   Required: {', '.join(op_info['required_args'])}")
        if op_info['docstring']:
            print(f"   Description: {op_info['docstring'].strip()}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Math Calculation Engine - Modular Python Math Library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python calc.py                    # Run demo calculations
  python calc.py --notebook         # Launch Jupyter notebook  
  python calc.py --interactive      # Interactive mode
  python calc.py --list            # List operations
        """
    )
    
    parser.add_argument(
        '--notebook', 
        action='store_true',
        help='Launch interactive Jupyter notebook'
    )
    
    parser.add_argument(
        '--interactive', '-i',
        action='store_true', 
        help='Run in interactive calculation mode'
    )
    
    parser.add_argument(
        '--demo', '-d',
        action='store_true',
        help='Run demonstration calculations (default)'
    )
    
    parser.add_argument(
        '--list', '-l',
        action='store_true',
        help='List all available operations'
    )
    
    args = parser.parse_args()
    
    try:
        if args.notebook:
            launch_notebook()
        elif args.interactive:
            interactive_mode()
        elif args.list:
            list_all_operations()
        elif args.demo or len(sys.argv) == 1:
            run_demo()
        else:
            show_help()
            
    except KeyboardInterrupt:
        print(f"\n👋 Operation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()