# Project Overview

This calculator project provides a simple interface for calculating the area and perimeter of various geometric figures. It supports operations for circles, squares, and rectangles, allowing users to input dimensions and receive results based on mathematical formulas. The aim of this project is to provide an easy-to-use tool for geometric calculations.

# How to Use Calculator
1. Run `python calculate.py`
2. Enter the figure name. Available options are Circle, Square, Rectangle.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes: 
   - Radius for Circle
   - One side for Square
   - Two sides for Rectangle
5. Get the answer!

# Math Formulas

## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where `p` is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Function Descriptions

### `calc(fig, func, size)`
Calculates the area of the specified geometric figure.

**Parameters**:
- `fig`: The type of figure (e.g., "circle", "square", "rectangle").
- `func`: function of what we do(e.g., "area", "perimetr").
- `size`: The dimensions required to calculate the area (e.g., radius for Circle, side for Square).

**Example usage**:
```python
area_circle = calc_area("circle", radius=5)
print(area_circle)  # 78.54

area_square = calc_area("square", side=4)
print(area_square)  # 16
```
# The history of changing the project with the hashes of commits
1) **8ba9aeb** L-03: Circle and square added
2) **d078c8d** (**origin/main**, **origin/HEAD**, **main**) L-03: Docs added
3) **d080c78** L-04: Triangle added
4) **51c40eb** L-04: Doc updated for triangle
5) **d76db2a** L-04: Add calculate.py