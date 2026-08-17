# Tower of Hanoi Solver

A recursive implementation of the classic Tower of Hanoi puzzle, returning
a step-by-step trace of every disk move required to solve it for `n` disks.

## Features
- Recursive algorithm solving the puzzle for any number of disks
- Tracks and returns the state of all three rods after every move
- Demonstrates understanding of recursion and problem decomposition

## Example
```python
print(hanoi_solver(3))
```

Outputs the state of all three rods after each move, showing the full
sequence of steps from the initial stack to the solved state.

## What I'd add next
- A move counter to show total moves taken (should equal 2^n - 1)
- Input validation for n <= 0
