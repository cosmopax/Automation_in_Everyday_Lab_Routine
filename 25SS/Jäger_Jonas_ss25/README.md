# 🧪 Unit Conversion Tool

A Python command-line utility for converting between physical units using the [Pint](https://pint.readthedocs.io/) library.  
Supports conversions for length, mass, volume, temperature, and more.

---

## 📦 Requirements

- Python 3.6+
- Pint library  
Install it using:

```bash
pip install pint
```

---

## 🚀 Usage

```bash
python convert.py <value> <from_unit> <to_unit> [--precision <digits>]
```

### 📋 Options

- `--precision <digits>` Set decimal places for output (default: auto)
- `-p`        List all available units
- `-h`        Show help and usage

---

## ✅ Examples

```bash
python JonasJäger_M9_convert.py 500 mL L
# → 0.5 liter

python JonasJäger_M9_convert.py 5 feet meters
# → 1.524 meter

python JonasJäger_M9_convert.py 123.456 km mi --precision 2
# → 76.71 mile
```

---

## 🔍 View All Units

To see a list of all supported unit names:

```bash
python JonasJäger_M9_convert.py -p
```

---

## ❗ Error Handling

- Invalid unit names will suggest similar valid units.
- Incompatible units (e.g., trying to convert time to mass) will show a descriptive error.
- Precision errors or syntax issues will print helpful messages.

---

## 📝 License

MIT License

---

## 👨‍💻 Author

Created by [Your Name].  
Inspired by practical needs in science, engineering, and everyday conversions.
