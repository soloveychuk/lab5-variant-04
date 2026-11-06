"""
Лабораторна робота: Варіант 4
Студент: Бучак Олег
Група: EIP30
"""
#використовувати метод ділення навпіл; ε = 0.00003.
import math 
def target_function(x):
    return math.tan(x) - 1/x
def bisections(func, a, b, eps = 0.00003):
    iterations = 0
    history = []
    while (b-a)/2 >= eps:
        c=(a+b)/2
        fc=func(c)
        iterations +=1
        history.append(round(c,6))
        if fc == 0:
            return c, iterations, history  
        if func(a)*fc < 0:
            b = c
        else:
            a = c
    root = (a+b)/2
    return root, iterations, history 
