from physics.kinematics.one_d import (
    solve_final_position, 
    solve_final_velocity, 
    solve_position_avg_velocity, 
    solve_velocity_from_position,
    solve_time_linear_velocity,
    solve_time_quadratic_position
)


RULES = [
    
    # --- Velocity rules --- 
    {
        "provides": "v",
        "requires": {"v0", "a", "t"},
        "fn": solve_final_velocity,
        "priority": 1,
        "kind": "linear",
    }, 
    {
        "provides": "v",
        "requires": {"v0", "a", "x0", "x"},
        "fn": solve_velocity_from_position,
        "priority": 2,
        "kind": "linear",   # v = sqrt(...)
    }, 
            
            
    # --- Position rules ---
    {
        "provides": "x",
        "requires": {"x0", "v0", "a", "t"},
        "fn": solve_final_position,
        "priority": 1,
        "kind": "linear", 
    }, 
    {
        "provides": "x",
        "requires": {"x0", "v0", "v", "t"},
        "fn": solve_position_avg_velocity,
        "priority": 2,
        "kind": "linear", 
    }, 
    
    
    # --- Time rules ---
    {
        "provides": "t",
        "requires": {"v", "v0", "a"},
        "fn": solve_time_linear_velocity,
        "priority": 1,
        "kind": "linear", 
    }, 
    {
        "provides": "t",
        "requires": {"x", "x0", "v0", "a"},
        "fn": solve_time_quadratic_position,
        "priority": 2,
        "kind": "quadratic", 
    }, 
]

def solve_kinematics_1d(
    knowns: dict[str, float],
    target: str
) -> float | tuple[float, float]:
    
    
    if target in knowns:
        return knowns[target]
    
    candidates = [
        rule for rule in RULES 
        if rule["provides"] == target 
        and rule["requires"].issubset(knowns.keys())
    ]
    
    if not candidates:
        raise ValueError("No solvable rule")
    
    rule = min(candidates, key=lambda r: r["priority"])
    kwargs = {k: knowns[k] for k in rule["requires"]}
    return rule["fn"](**kwargs)