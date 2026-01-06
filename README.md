# Physics Simulator – 1D Kinematics Solver

A rule-based solver for 1D constant-acceleration kinematics problems. Given known variables, the solver selects the appropriate equation and solves for a requested target variable.

## Example
```python
solve_kinematics_1d(
    {"v0": 5.0, "a": 2.0, "t": 3.0},
    "v"
)
# 11.0
```