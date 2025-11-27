#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

def plot_csv_data(csv_path, output_path=None):
    try:
        df = pd.read_csv(csv_path)

        if df.shape[1] < 2:
            raise ValueError("CSV must contain at least two columns.")

        # Detect X and Y columns (with units in header)
        x_column_full = df.columns[0]
        y_column_full = df.columns[1]

        # Extract labels and units
        def extract_label_unit(column_header):
            if '(' in column_header and ')' in column_header:
                label = column_header.split('(')[0].strip()
                unit = column_header.split('(')[1].split(')')[0].strip()
                return f"{label} ({unit})"
            return column_header.strip()

        x_label = extract_label_unit(x_column_full)
        y_label = extract_label_unit(y_column_full)
        title = f"{y_label} vs {x_label}"

        if not output_path:
            base = os.path.splitext(os.path.basename(csv_path))[0]
            output_path = f"{base}_plot.png"

        plt.figure(figsize=(8, 6))
        plt.plot(df[x_column_full], df[y_column_full], marker='o', linestyle='-', color='blue')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(True)
        plt.tight_layout()

        plt.savefig(output_path)
        print(f"Plot saved as: {output_path}")
        print(f"Title: {title}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Automatically plot the first two columns of a CSV file, including units, and save as a PNG image."
    )
    parser.add_argument("csv_file", help="Path to the input CSV file")
    parser.add_argument("--output", help="Optional: Output image path (default: auto-named *.png)")

    args = parser.parse_args()
    plot_csv_data(args.csv_file, args.output)

if __name__ == "__main__":
    main()
