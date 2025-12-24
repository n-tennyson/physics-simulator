import math
from physics.kinematics.one_d import solve_final_velocity, solve_final_position, solve_velocity_squared


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
    

def test_solve_final_velocity_constant_acceleration():
    """
    Given v0 = 5 m/s, a = 2 m/s^2, t = 3 s,
    the final velocity should be  m/s
    """
    v0 = 5.0
    a = 2.0
    t = 3.0
    
    
    result = solve_final_velocity(v0, a, t)
    
    assert math.isclose(result, 11.0)
    

def test_solve_velocity_squared_constant_acceleration():
    """
    Given v0 = 2 m/s, a = 5 m/s^2, x0 = 0 m, x = 10 m,
    the final velocity square should be 104 m^2/s^2
    """
    v0 = 2.0
    a = 5.0
    x0 = 0.0
    x = 10.0
    
    
    result = solve_velocity_squared(v0, a, x0, x)
    
    assert math.isclose(result, 104.0)
    