# 6.00 Problem Set 2
#
# Successive Approximation
#

def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    
    count=0
    ans=0.0;
    for i in poly:
        ans=ans+i*(x**count)
        count +=1
    return ans    

  


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    
    count=1
    poly1=()
    for i in poly[1:]:
        a=i*count
        count =count+1
        poly1+=(a,)
    return poly1

        

def compute_root(poly, x_0, epsilon):
    root = x_0
    counter = 1
    while abs(evaluate_poly(poly, root)) >= epsilon:
        root = (root - evaluate_poly(poly, root) /
                evaluate_poly(compute_deriv(poly), root))
        counter += 1
    return [root, counter]
    
poly = (-13.39, 0.0, 17.5, 3.0, 1.0)   # - 13.39 + 17.5x^2 + 3x^3 + x^4
x_0 = 0.1
epsilon = .0001
print compute_root(poly, x_0, epsilon)
