""" 
1D kinematics for constant acceleration.

All motion is assumed to occur along a single axis with constant acceleration.
"""



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
        Initial velocity (m/s).
    a : float
        Constant acceleration (m/s^2).
    t: float 
        Time interval (s).
    
    Returns
    -------
        Final velocity (m/s) after time t.
    """
    return v0 + a * t
    
    
def solve_final_position(
    x0: float, 
    v0: float,
    a: float,
     t: float
) -> float:
    """
    Compute final position for constant acceleration.
    
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
    Compute final veolcity squared using the no-time equation.
    
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
        Final velocity squared (m^2/s^2) at position x.
    """
    return v0**2 + 2 * a * (x - x0)
    