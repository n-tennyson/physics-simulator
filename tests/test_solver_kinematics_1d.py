import pytest

from physics.kinematics.solver_1d import solve_kinematics_1d


def test_solver_velocity_from_time():
    knowns = {"v0": 5.0, "a": 2.0, "t": 3.0}
    result = solve_kinematics_1d(knowns, "v")
    
    assert result == 11.0


def test_solver_position_from_time():
    knowns = {"x0": 0.0, "v0": 5.0, "a": 2.0, "t": 3.0}
    result = solve_kinematics_1d(knowns, "x")
    
    assert result == 24.0
    

def test_solver_velocity_priority():
    knowns = {
        "v0": 5.0,
        "a": 2.0, 
        "t": 3.0,
        "x0": 0.0,
        "x": 24.0,
    }
    
    result = solve_kinematics_1d(knowns, "v")
    
    assert result == 11.0 # uses v = v0 + at
    


def test_solver_time_linear():
    knowns = {"v": 11.0, "v0": 5.0, "a": 2.0}
    result = solve_kinematics_1d(knowns, "t")
    
    assert result == 3.0
    
    
def test_solver_time_quadratic():
    knowns = {"x": 24.0, "x0": 0.0, "v0": 5.0, "a": 2.0}
    t1, t2 = solve_kinematics_1d(knowns, "t")
    
    assert t1 != t2
    assert 3,0 in (t1, t2)
    
    
def test_solver_no_solution(): 
    knowns = {"v0": 5.0}
    with pytest.raises(ValueError):
        solve_kinematics_1d(knowns, "x")
    
