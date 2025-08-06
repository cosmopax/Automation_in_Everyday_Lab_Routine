# Chemical Data Fetcher

A cross-platform (macOS, Ubuntu) Python utility to fetch chemical compound data, generate structures, and log details into an Excel sheet.

---

## Features

1. **Interactive CLI**

   - Run anywhere—script directory is dynamic.
   - Input compound name or CAS number.
   - Exit with `Ctrl+C` or by typing `exit`.

2. **Google & PubChem Lookup**

   - Searches Google for CAS or PubChem CID.
   - Fallback to direct PubChem query.
   - Fetches:
     - SMILES
     - IUPAC name
     - Molar mass (numeric)
     - Molecular formula
     - Synonyms
   - Manual SMILES override for known compounds (e.g., homotaurine).

3. **Structure Generation**

   - 3D `.pdb` and `.mol` files (optimized, H’s removed for ACS 1996 style).
   - 2D PNG depiction.
   - Output directories default to `ligands/`, `chemdraw/`, `images/` under script's location.

4. **Excel Logging**

   - Logs in `neurochem.xlsx` under script directory by default:
     - **Laufnummer** (entry number)
     - 2D image
     - Colloquial & IUPAC names
     - Molar mass
     - Formula
     - Melting point (°C)
     - NMR & MS file links
     - Synonyms
   - Skips duplicates.

5. **Logging & Robustness**

   - Detailed logs for each step.
   - Error handling for fetch, generation, and file operations.

---

## Installation

```bash
# Clone or download this script
cd /path/to/script

# Create virtual env (optional)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install pubchempy rdkit-pypi googlesearch-python openpyxl
```

## Usage

```bash
python chemical_data_fetcher.py [options]
```

### Options

| Flag              | Description                    | Default            |
| ----------------- | ------------------------------ | ------------------ |
| `-e`, `--excel`   | Path to Excel log file         | `./neurochem.xlsx` |
| `-p`, `--pdb_dir` | Output directory for PDB files | `./ligands`        |
| `-m`, `--mol_dir` | Output directory for MOL files | `./chemdraw`       |
| `-i`, `--img_dir` | Output directory for 2D images | `./images`         |

### Example

```bash
# Default locations
python chemical_data_fetcher.py

# Custom paths
python chemical_data_fetcher.py -e ~/data/chem.xlsx -p ~/data/pdbs -m ~/data/mols -i ~/data/imgs
```

Once running, type a compound name or CAS (e.g., `taurine`), then press Enter. The script fetches data, creates structure files, draws a PNG, and logs everything in Excel.

---

## Platform Support

- **macOS**: Tested on macOS 12+.
- **Ubuntu**: Tested on Ubuntu 18.04+.

Dependencies are cross-platform.

---

## License & Citation

Free to use and modify. Please cite this script in your work if helpful. 
# www.GitHub.com/cosmopax

