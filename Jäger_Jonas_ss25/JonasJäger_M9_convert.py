"""
Unit Conversion Tool

A command-line utility for converting between different units using the Pint library.
Supports a wide variety of physical units including length, mass, volume, temperature, etc.

Usage:
    python JonasJäger_M9_convert.py <value> <from_unit> <to_unit> [--precision <digits>]
    python JonasJäger_M9_convert.py -p  # to list all available units
    python JonasJäger_M9_convert.py -h  # to show help

Examples:
    python JonasJäger_M9_convert.py 500 mL L
    python JonasJäger_M9_convert.py 5 feet meters
    python JonasJäger_M9_convert.py 123.456 km mi --precision 2
"""

import sys
from pint import UnitRegistry
from difflib import get_close_matches


def print_units():
    """Print all available units in the Pint unit registry."""
    ureg = UnitRegistry()
    print("Available units:")
    # Iterate through all units in the registry and print them alphabetically
    for unit in sorted(ureg):
        print(unit)


def print_help():
    """Print detailed help information."""
    print("Unit Conversion Tool")
    print("===================")
    print()
    print("Usage:")
    print("  python JonasJäger_M9_convert.py <value> <from_unit> <to_unit> [--precision <digits>]")
    print("  python JonasJäger_M9_convert.py -p  # List all available units")
    print("  python JonasJäger_M9_convert.py -h  # Show this help")
    print()
    print("Examples:")
    print("  python JonasJäger_M9_convert.py 500 mL L")
    print("  python JonasJäger_M9_convert.py 100 celsius fahrenheit")
    print("  python JonasJäger_M9_convert.py 5 feet meters")
    print("  python JonasJäger_M9_convert.py 123.456 km mi --precision 2")
    print()
    print("Options:")
    print("  --precision <digits>  Number of decimal places in output (default: auto)")
    print("  -p                    List all available units")
    print("  -h                    Show this help message")


def suggest_units(invalid_unit, ureg):
    """Suggest similar units when an invalid unit is provided."""
    all_units = [str(unit) for unit in ureg]
    suggestions = get_close_matches(invalid_unit, all_units, n=5, cutoff=0.6)
    if suggestions:
        print(f"Did you mean one of these units?")
        for suggestion in suggestions:
            print(f"  - {suggestion}")
    else:
        print("Use 'python JonasJäger_M9_convert.py -p' to see all available units.")

def main():
    """Main function to handle command line arguments and perform unit conversion."""
    # Check if user wants help
    if '-h' in sys.argv or '--help' in sys.argv:
        print_help()
        sys.exit(0)
    
    # Check if user wants to print available units
    if '-p' in sys.argv:
        print_units()
        sys.exit(0)

    # Check for precision flag
    precision = None
    args = sys.argv[1:]  # Remove script name
    if '--precision' in args:
        try:
            precision_index = args.index('--precision')
            precision = int(args[precision_index + 1])
            # Remove precision arguments from args list
            args = args[:precision_index] + args[precision_index + 2:]
        except (IndexError, ValueError):
            print("Error: --precision requires a valid integer")
            sys.exit(1)

    # Validate command line arguments (should have exactly 3 args after removing precision)
    if len(args) != 3:
        print("Usage: python JonasJäger_M9_convert.py <value> <from_unit> <to_unit> [--precision <digits>]")
        print("Example: python JonasJäger_M9_convert.py 500 mL L")
        print("Use -h for help or -p to list all available units")
        sys.exit(1)

    try:
        # Parse command line arguments
        value_str, from_unit, to_unit = args
        
        # Validate numeric input
        try:
            value = float(value_str)
        except ValueError:
            print(f"Error: '{value_str}' is not a valid number")
            sys.exit(1)

        # Create unit registry and perform conversion
        ureg = UnitRegistry()
        
        try:
            quantity = value * ureg(from_unit)  # Create quantity with original unit
        except Exception as e:
            print(f"Error: Invalid unit '{from_unit}'")
            suggest_units(from_unit, ureg)
            sys.exit(1)
            
        try:
            result = quantity.to(to_unit)       # Convert to target unit
        except Exception as e:
            print(f"Error: Cannot convert from '{from_unit}' to '{to_unit}'")
            print(f"These units may be incompatible (different dimensions)")
            suggest_units(to_unit, ureg)
            sys.exit(1)

        # Format and output the result
        if precision is not None:
            magnitude = round(result.magnitude, precision)
        else:
            magnitude = round(result.magnitude, 3)  # Default to 3 decimal places
            
        print(f"{magnitude} {result.units}")
        
    except Exception as e:
        # Handle any unexpected errors
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
