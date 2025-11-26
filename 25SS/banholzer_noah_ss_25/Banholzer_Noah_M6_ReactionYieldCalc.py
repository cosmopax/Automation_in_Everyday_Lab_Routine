#!/usr/bin/env python3

import argparse
import sys

def calculate_theoretical_yield(limiting_mass, limiting_molar_mass, product_molar_mass, molar_ratio=1.0):
    moles_limiting = limiting_mass / limiting_molar_mass
    moles_product = moles_limiting * molar_ratio
    theoretical_yield = moles_product * product_molar_mass
    return theoretical_yield

def calculate_percent_yield(theoretical_yield, actual_yield):
    if theoretical_yield <= 0:
        raise ValueError("Theoretical yield must be greater than 0.")
    if actual_yield < 0:
        raise ValueError("Actual yield cannot be negative.")
    return (actual_yield / theoretical_yield) * 100

def main():
    parser = argparse.ArgumentParser(
        description="Calculate percent yield based on limiting reagent and product masses."
    )

    parser.add_argument("limiting_mass", type=float, help="Mass of the limiting reagent (g)")
    parser.add_argument("limiting_molar_mass", type=float, help="Molar mass of the limiting reagent (g/mol)")
    parser.add_argument("product_molar_mass", type=float, help="Molar mass of the desired product (g/mol)")
    parser.add_argument("actual_yield", type=float, help="Mass of the isolated product (g)")
    parser.add_argument("--molar_ratio", type=float, default=1.0,
                        help="Molar ratio (product:limiting reagent) from the balanced equation (default: 1.0)")

    args = parser.parse_args()

    try:
        theoretical_yield = calculate_theoretical_yield(
            args.limiting_mass,
            args.limiting_molar_mass,
            args.product_molar_mass,
            args.molar_ratio
        )
        percent_yield = calculate_percent_yield(theoretical_yield, args.actual_yield)

        print(f"Theoretical Yield: {theoretical_yield:.2f} g")
        print(f"Percent Yield: {percent_yield:.2f}%")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
