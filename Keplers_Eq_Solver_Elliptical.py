<<<<<<< HEAD
#Hunter Borwick
#3/18/2020
#Kepler's Equation Solver for Eccentric Anomaly (Elliptical Orbits)

import math
if __name__ == "__main__":
    #User input for meal anomaly and eccentricity 
    M_e = float(input('Enter Mean Anomaly: '))
    e = float(input('Enter Eccentricity: '))
    
    #Iteration Tolerance
    tol = 1E-8

    #Initial Guess at Eccentric Anomaly
    if M_e < math.pi:
        E = M_e + (e / 2)
    if M_e > math.pi:
        E = M_e - (e / 2)
    
    #Initial Conditions
    f = E - e*math.sin(E) - M_e
    f_prime = 1 - e*math.cos(E)
    ratio = f / f_prime

    #Numerical interation for ratio compared to tolerance 
    while abs(ratio) > tol:
        f = E - e*math.sin(E) - M_e
        f_prime = 1 - e*math.cos(E)
        ratio = f / f_prime

        if abs(ratio) > tol:
            E = E - ratio
        if abs(ratio) < tol:
            break

    print('Eccentric Anomaly is:', E)
=======
#Hunter Borwick
#3/18/2020
#Kepler's Equation Solver for Eccentric Anomaly (Elliptical Orbits)

import math
if __name__ == "__main__":
    #User input for meal anomaly and eccentricity 
    M_e = float(input('Enter Mean Anomaly: '))
    e = float(input('Enter Eccentricity: '))
    
    #Iteration Tolerance
    tol = 1E-8

    #Initial Guess at Eccentric Anomaly
    if M_e < math.pi:
        E = M_e + (e / 2)
    if M_e > math.pi:
        E = M_e - (e / 2)
    
    #Initial Conditions
    f = E - e*math.sin(E) - M_e
    f_prime = 1 - e*math.cos(E)
    ratio = f / f_prime

    #Numerical interation for ratio compared to tolerance 
    while abs(ratio) > tol:
        f = E - e*math.sin(E) - M_e
        f_prime = 1 - e*math.cos(E)
        ratio = f / f_prime

        if abs(ratio) > tol:
            E = E - ratio
        if abs(ratio) < tol:
            break

    print('Eccentric Anomaly is:', E)
>>>>>>> 2e1d33a9d1442a94d20bfb479c787427f4d52ad1
