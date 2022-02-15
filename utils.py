from cmath import isclose
import math



def fact(n):
    factorial = 1
    if n >= 0:
        for i in range (1,n+1):
               factorial = factorial * i
        return factorial

    else : 
        print("operation impossible")

    


def roots(a, b, c):

    Delta = b*b-4*a*c 

    if Delta>0:
        x1 = (-b+ math.sqrt(Delta) )/(2*a)
        x2 = (-b- math.sqrt(Delta) )/(2*a)
        return x1, x2

    elif math.isclose (Delta, 0):
        x = -b/(2*a)

    else :
        print("pas de solutions")



    pass

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
        'lower' <= 'upper',
        'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
        of the specified 'function'.

    Hint: You can use the 'integrate' function of the module 'scipy' and
        you'll probably need the 'eval' function to evaluate the function
        to integrate given as a string.
    """
    pass

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 7, -12))
    print(integrate('x ** 2 - 1', -1, 1))
