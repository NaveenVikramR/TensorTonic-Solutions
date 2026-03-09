def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    x = x0
    
    for i in range(steps):
        f = a*(x**2) + b*x + c      
        fd = 2*a*x + b             
        x = x - lr*fd               
        
    return x