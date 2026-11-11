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
    estimation=math.log2((b-a)/eps)
    while (b-a)/2 >= eps:
        c=(a+b)/2
        fc=func(c)
        iterations +=1
        history.append(round(c,6))
        if fc == 0:
            return c, iterations, history, estimation
        if func(a)*fc < 0:
            b = c
        else:
            a = c
    root = (a+b)/2

    return root, iterations, history, estimation
root, iterations, history, estimation = bisections(target_function, 0.5, 1)
print("Корінь рівняння:", round(root, 6))

print(f"Оцінка кількості ітерацій: {estimation:.1f}, фактична кількість ітерацій: {iterations}")
print("---")
print("Історія ітерацій:")
for i, c in enumerate(history, 1):
    print(f"Ітерація {i}: x = {c}")
with open("results.txt", "w", encoding="utf-8") as file:
    file.write("Результати обчислень:\n")
    file.write(f"Корінь: {root:.6f}\n")
    file.write("Історія ітерацій:\n")
    file.write(f"Оцінка кількості ітерацій: {estimation:.1f}, фактична кількість ітерацій: {iterations}\n")
    for i, c in enumerate(history, 1):
        file.write(f"Ітерація {i}: x = {c}\n")
