import math

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

def solve_velocity_from_position(
    v0, 
    a, 
    x0, 
    x
    ) -> float:
    """
    use velocity squared function result to solve for velocity
    """
    return math.sqrt(solve_velocity_squared(v0, a, x0, x))
    
    
def solve_position_avg_velocity(
    x0: float,
    v0: float,
    v: float,
    t: float
    ) -> float:
    """
    Compute final postion using average velocity equation.
    
    Parameters
    ----------
    
    x0: float 
        initial position
    v0: float
        initial velocity
    v: float
        final velocity
    t: float
        final time
        
    Returns
    -------
    float
        Final position (m) at time (s)
    """
    return x0 + 0.5 * (v + v0) * t


def solve_time_linear_velocity(
    v: float,
    v0: float,
    a: float
) -> float:
    """
    Solve for time using the linear velocity equation:
        v = v0 + a * t
        
    Parameters
    ----------
    v : float 
        Final velocity (m/s)
    v0 : float 
        Initial velocity (m/s)
    a : float 
        Constant acceleration (m/s^2)
        
    Returns
    -------
    float
        time interval (s)
        
    Raises 
    ------ 
    ValueError
        If acceleration is zero (cannot solve for time).
    """
    if a == 0:
        raise ValueError("Cannot solve for time when acceleration is zero")
    
    return (v - v0) / a


def solve_time_quadratic_position(
    x: float,
    x0: float,
    v0: float,
    a: float
) -> tuple[float, float]:
    """
    Solve for time using the position equation:
        x = x0 + v0 * t + 1/2 * a * t**2
        
    Parameters
    ----------
    x: float 
        Final position (m)
    x0: float
        Initial position (m)
    v0: float 
        Initial velocity (m/s)
    a: float
        Constant acceleration (m/s^2)
        
    Returns
    -------
    tuple[float, float]
        Two possible time solutions (s)
        
    
    Raises
    ------
    ValueError
        If no real solution exists
    """
    
    if a == 0:
        raise ValueError(
            "Acceleration is zero; use linear time equation instead"
        )
    
    A = 0.5 * a
    B = v0
    C = x0 - x
    
    discriminant = B**2 - 4 * A * C
    
    if discriminant < 0:
        raise ValueError("No real time solution exists")
    
    sqrt_d = math.sqrt(discriminant)
    
    t1 = (-B + sqrt_d) / (2 * A)
    t2 = (-B - sqrt_d) / (2 * A)
    
    return t1, t2