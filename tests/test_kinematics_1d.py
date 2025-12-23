import math
from physics.kinematics.one_d import solve_final_position


def test_solve_final_position_constant_acceleration():
    """
    Given x0 = 0m , v0 = 5 m/s, a = 2 m/s^2, t = 3 s,
    the final position should be 24
    """
    x0 = 0.0
    v0 = 5.0
    a = 2.0
    t = 3.0
    
    
    result = solve_final_position(x0, v0, a, t)
    
    assert math.isclose(result, 24.0)