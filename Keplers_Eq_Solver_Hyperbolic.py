<<<<<<< HEAD
#Hunter Borwick
#3/18/2020
#Kepler's Equation Solver for Eccentric Anomaly (Hyperbolic Trajectories)

import math
if __name__ == "__main__":
    #User input for meal anomaly and eccentricity 
    M_h = float(input('Enter Hyperbolic Mean Anomaly: '))
    e = float(input('Enter Eccentricity: '))
    
    #Iteration Tolerance
    tol = 1E-8

    #Initial Guess at Hyperbolic Eccentric Anomaly
    F_h = M_h
    
    #Initial Conditions
    f = e*math.sinh(F_h) - F_h - M_h
    f_prime = e* math.cosh(F_h) - 1
    ratio = f / f_prime

    #Numerical interation for ratio compared to tolerance 
    while abs(ratio) > tol:
        f = e*math.sinh(F_h) - F_h - M_h
        f_prime = e* math.cosh(F_h) - 1
        ratio = f / f_prime

        if abs(ratio) > tol:
            F_h = F_h - ratio
        if abs(ratio) < tol:
            break

=======
#Hunter Borwick
#3/18/2020
#Kepler's Equation Solver for Eccentric Anomaly (Hyperbolic Trajectories)

import math
if __name__ == "__main__":
    #User input for meal anomaly and eccentricity 
    M_h = float(input('Enter Hyperbolic Mean Anomaly: '))
    e = float(input('Enter Eccentricity: '))
    
    #Iteration Tolerance
    tol = 1E-8

    #Initial Guess at Hyperbolic Eccentric Anomaly
    F_h = M_h
    
    #Initial Conditions
    f = e*math.sinh(F_h) - F_h - M_h
    f_prime = e* math.cosh(F_h) - 1
    ratio = f / f_prime

    #Numerical interation for ratio compared to tolerance 
    while abs(ratio) > tol:
        f = e*math.sinh(F_h) - F_h - M_h
        f_prime = e* math.cosh(F_h) - 1
        ratio = f / f_prime

        if abs(ratio) > tol:
            F_h = F_h - ratio
        if abs(ratio) < tol:
            break

>>>>>>> 2e1d33a9d1442a94d20bfb479c787427f4d52ad1
    print('Hyperbolic Eccentric Anomaly is:', F_h)