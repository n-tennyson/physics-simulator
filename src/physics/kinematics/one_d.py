""" 
1D kinematics for constant acceleration.

All motion is assumed to occur along a single axis with constant acceleration.
"""

from typing import Optional


def solve_final_velocity (
    v0: float,
    a: float,
    t: float
) -> float:
    """ 
    Compute final velocity for constant acceleration.
    
    Parameters
    ----------
    v0 : float 
        Intial velocity (m/s).
    a : float
        Constant acceleration (m/s^2).
    t: float 
        Time interval (s).
    
    Returns
    -------
        Final velocity (m/s) after time t.
    """
    pass
    
    
def solve_final_position(
    x0: float, 
    v0: float,
    a: float,
     t: float
) -> float:
    """
    Compute final position for constatn acceleration.
    
    Parameters
    ----------
    x0 : float 
        Initial position (m).
    v0 : float
        Initial velocity (m/s).
    a : float
        Constant acceleration (m/s^2).
    t : float
        Time interval (s).
        
    Returns
    -------
    float
        Final position (m) after time t.
    """
    return x0 + v0 * t + 0.5 * a * t**2

    
def solve_velocity_squared(
    v0: float, 
    a: float,
    x0: float,
    x: float
) -> float:
    """
    Compute final veolcity magnitude using the no-time equation.
    
    Parameters
    ----------
    
    v0 : float 
        Initial velocity (m/s).
    a : float
        Constant acceleration (m/s^2).
    x0 : float 
        initial position (m).
    x : float 
        Final position (m).
    
    Returns
    -------
    float
        Final velocity (m/s) at position x.
    """
    pass
    