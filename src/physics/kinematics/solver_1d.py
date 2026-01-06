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

        "equation": "v = v₀ + at",
        "rearranged_equation": "v = v₀ + at",

        "algebra_steps": [
            "Start with the kinematic equation v = v₀ + at",
            "The equation is already solved for v",
        ],

        "evaluation_steps": [
            "Substitute v₀ = {v0}, a = {a}, t = {t}",
            "v = {v0} + ({a})({t})",
        ],
    }, 
    {
        "provides": "v",
        "requires": {"v0", "a", "x0", "x"},
        "fn": solve_velocity_from_position,
        "priority": 2,
        "kind": "quadratic",

        "equation": "v² = v₀² + 2a(x − x₀)",
        "rearranged_equation": "v = √(v₀² + 2a(x − x₀))",

        "algebra_steps": [
            "Start with the kinematic equation v² = v₀² + 2a(x − x₀)",
            "Take the square root of both sides to solve for v",
        ],

        "evaluation_steps": [
            "Substitute v₀ = {v0}, a = {a}, x₀ = {x0}, x = {x}",
            "v = √({v0}² + 2·{a}·({x} − {x0}))",
        ],
    }, 
            
            
    # --- Position rules ---
    {
        "provides": "x",
        "requires": {"x0", "v0", "a", "t"},
        "fn": solve_final_position,
        "priority": 1,
        "kind": "linear",

        "equation": "x = x₀ + v₀t + ½at²",
        "rearranged_equation": "x = x₀ + v₀t + ½at²",

        "algebra_steps": [
            "Start with the kinematic equation x = x₀ + v₀t + ½at²",
            "The equation is already solved for x",
        ],

        "evaluation_steps": [
            "Substitute x₀ = {x0}, v₀ = {v0}, a = {a}, t = {t}",
            "x = {x0} + ({v0})({t}) + ½({a})({t})²",
        ],
    }, 
    {
        "provides": "x",
        "requires": {"x0", "v0", "v", "t"},
        "fn": solve_position_avg_velocity,
        "priority": 2,
        "kind": "linear",

        "equation": "x = x₀ + ½(v₀ + v)t",
        "rearranged_equation": "x = x₀ + ½(v₀ + v)t",

        "algebra_steps": [
            "Use the average velocity formula v_avg = ½(v₀ + v)",
            "Substitute into x = x₀ + v_avg t",
        ],

        "evaluation_steps": [
            "Substitute x₀ = {x0}, v₀ = {v0}, v = {v}, t = {t}",
            "x = {x0} + ½({v0} + {v})({t})",
        ],
    }, 
    
    
    # --- Time rules ---
    {
        "provides": "t",
        "requires": {"v", "v0", "a"},
        "fn": solve_time_linear_velocity,
        "priority": 1,
        "kind": "linear",

        "equation": "v = v₀ + at",
        "rearranged_equation": "t = (v − v₀)/a",

        "algebra_steps": [
            "Start with the kinematic equation v = v₀ + at",
            "Subtract v₀ from both sides",
            "Divide both sides by a",
        ],

        "evaluation_steps": [
            "Substitute v = {v}, v₀ = {v0}, a = {a}",
            "t = ({v} − {v0}) / {a}",
        ],
    }, 
    {
        "provides": "t",
        "requires": {"x", "x0", "v0", "a"},
        "fn": solve_time_quadratic_position,
        "priority": 2,
        "kind": "quadratic",

        "equation": "x = x₀ + v₀t + ½at²",
        "rearranged_equation": "½at² + v₀t + (x₀ − x) = 0",

        "algebra_steps": [
            "Start with x = x₀ + v₀t + ½at²",
            "Rearrange into standard quadratic form",
            "Solve using the quadratic formula",
        ],

        "evaluation_steps": [
            "Substitute x = {x}, x₀ = {x0}, v₀ = {v0}, a = {a}",
            "Solve the resulting quadratic equation for t",
        ],
    }, 
]

def solve_kinematics_1d(
    knowns: dict[str, float],
    target: str
) -> dict:
    
    
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
    
    result = rule["fn"](**kwargs)
    
    evaluation_steps = [
        step.format(**knowns)
        for step in rule.get("evaluation_steps", [])
    ]

    return {
        "result": result,
        "equation": rule.get("equation"),
        "rearranged_equation": rule.get("rearranged_equation"),
        "algebra_steps": rule.get("algebra_steps", []),
        "evaluation_steps": evaluation_steps,
    }

