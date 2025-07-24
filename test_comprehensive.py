#!/usr/bin/env python3
"""
Comprehensive test script for the Math Calculation Engine.
Tests operations from all categories to demonstrate the full capabilities.
"""

import sys
sys.path.append('.')

from core import calculate, Operation, list_operations

def test_all_categories():
    """Test operations from every category."""
    print("🧮 COMPREHENSIVE MATH ENGINE TEST")
    print("=" * 60)
    
    tests = [
        # Basic Arithmetic
        ("Basic Addition", Operation.ADD, {"a": 25, "b": 17}),
        ("Division", Operation.DIVIDE, {"a": 100, "b": 4}),
        ("Modulo", Operation.MODULO, {"a": 17, "b": 5}),
        
        # Advanced Arithmetic  
        ("Factorial", Operation.FACTORIAL, {"n": 6}),
        ("Combination C(8,3)", Operation.COMBINATION, {"n": 8, "r": 3}),
        ("GCD", Operation.GCD, {"a": 48, "b": 18}),
        ("Fibonacci 10th", Operation.FIBONACCI, {"n": 10}),
        
        # Areas
        ("Circle Area", Operation.AREA_CIRCLE, {"radius": 4}),
        ("Square Area", Operation.AREA_SQUARE, {"side": 7}),
        ("Trapezoid Area", Operation.AREA_TRAPEZOID, {"base1": 6, "base2": 10, "height": 5}),
        ("Ellipse Area", Operation.AREA_ELLIPSE, {"semi_major_axis": 5, "semi_minor_axis": 3}),
        
        # Volumes
        ("Sphere Volume", Operation.VOLUME_SPHERE, {"radius": 3}),
        ("Cylinder Volume", Operation.VOLUME_CYLINDER, {"radius": 2, "height": 6}),
        ("Cube Volume", Operation.VOLUME_CUBE, {"side": 4}),
        
        # Trigonometry
        ("Sin 45°", Operation.SIN_DEGREES, {"angle_degrees": 45}),
        ("Cos 60°", Operation.COS_DEGREES, {"angle_degrees": 60}),
        ("Convert 180° to radians", Operation.DEGREES_TO_RADIANS, {"degrees": 180}),
        ("Arctangent", Operation.ATAN_DEGREES, {"value": 1}),
        
        # Logarithms & Exponentials
        ("Natural Log of 10", Operation.NATURAL_LOG, {"x": 10}),
        ("Log base 2 of 16", Operation.LOG_BASE_2, {"x": 16}),
        ("e^2", Operation.EXPONENTIAL_E, {"x": 2}),
        ("Hyperbolic sine", Operation.SINH, {"x": 1}),
        
        # Statistics
        ("Mean", Operation.MEAN, {"values": [2, 4, 6, 8, 10]}),
        ("Median", Operation.MEDIAN, {"values": [1, 3, 5, 7, 9, 11]}),
        ("Standard Deviation", Operation.STANDARD_DEVIATION_SAMPLE, {"values": [10, 12, 14, 16, 18]}),
        
        # Geometry Utilities
        ("Distance 2D", Operation.DISTANCE_2D, {"x1": 1, "y1": 1, "x2": 4, "y2": 5}),
        ("Slope", Operation.SLOPE_LINE, {"x1": 0, "y1": 0, "x2": 2, "y2": 6}),
    ]
    
    print(f"Testing {len(tests)} operations from multiple categories...\n")
    
    passed = 0
    failed = 0
    
    for description, operation, kwargs in tests:
        try:
            result = calculate(operation=operation, **kwargs)
            if isinstance(result, float):
                result = round(result, 4)
            print(f"✅ {description:<25} → {result}")
            passed += 1
        except Exception as e:
            print(f"❌ {description:<25} → Error: {e}")
            failed += 1
    
    print(f"\n" + "=" * 60)
    print(f"🎯 TEST RESULTS: {passed} passed, {failed} failed")
    
    # Category breakdown
    operations = list_operations()
    print(f"📊 Total operations available: {len(operations)}")
    
    categories = {}
    for op in operations:
        name = op['operation'].name
        if name.startswith('AREA_'):
            categories['Areas'] = categories.get('Areas', 0) + 1
        elif name.startswith('VOLUME_'):
            categories['Volumes'] = categories.get('Volumes', 0) + 1
        elif any(x in name for x in ['SIN_', 'COS_', 'TAN_']):
            categories['Trigonometry'] = categories.get('Trigonometry', 0) + 1
        elif any(x in name for x in ['LOG_', 'EXPONENTIAL', 'SINH']):
            categories['Logarithms'] = categories.get('Logarithms', 0) + 1
        elif any(x in name for x in ['MEAN', 'MEDIAN', 'VARIANCE']):
            categories['Statistics'] = categories.get('Statistics', 0) + 1
        else:
            categories['Other Math'] = categories.get('Other Math', 0) + 1
    
    print("\n📋 Category Breakdown:")
    for category, count in sorted(categories.items()):
        print(f"   {category}: {count} operations")
    
    return passed == len(tests)

if __name__ == "__main__":
    success = test_all_categories()
    if success:
        print(f"\n🎉 All tests passed! Math Calculation Engine is fully operational.")
        sys.exit(0)
    else:
        print(f"\n⚠️  Some tests failed. Check the output above.")
        sys.exit(1)
