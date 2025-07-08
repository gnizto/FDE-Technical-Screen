# FDE Technical Screen

The code sorts packages one of the following stacks:

- **STANDARD**: If the package is not **heavy** or **bulky**;
- **SPECIAL**: If the package is either **heavy** or **bulky**;
- **REJECTED**: If the package is both **heavy** and **bulky**.

## Criteria

- **Bulky**: A package is considered bulky if:
    - The volume is greater than or equal to 1,000,000 cm3;
    - Or, at least one of its dimensions is greater or equal to 150 cm.
- **Heavy**: A package is considered heavy if its mass is greater or equal to 20 kg.

## Requirements

- Python 3.11 or higher
- `pip` installed

## Installation

Clone the repository:

```bash
git clone https://github.com/gnizto/FDE-Technical-Screen.git
```


## How to Run

Enter the directory created:

```bash
cd FDE-Technical-Screen
```

Run the main program:

```bash
python main.py
```

This is going to process some tests. More can be added inside the `main.py` file following the pattern:

```python
packages = [
    {
        "id": 1,
        "expected": "STANDARD",
        "input": {
            "width": 50,
            "height": 40,
            "length": 30,
            "mass": 10
        }
    }
]
```

This is going to generete a log like the following:

```text
#1 {'width': 50, 'height': 40, 'length': 30, 'mass': 10}: [True] Expected=STANDARD returned=STANDARD
```

## How to Run Tests

Using Python’s built-in `unittest` module, run:

```bash
python -m unittest test_sort.py
```
