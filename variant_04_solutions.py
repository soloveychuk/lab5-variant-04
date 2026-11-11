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
        history.append((iterations, a, b, c, fc))
        if fc == 0:
            return c, iterations, history, estimation
        if func(a)*fc < 0:
            b = c
        else:
            a = c
    root = (a+b)/2

    return root, iterations, history, estimation



def save_results_to_file(root, iterations, history, estimation):
    with open("results.txt", "w", encoding="utf-8") as file:
        file.write(f"Корінь: {root:.6f}\n")
        file.write(f"Оцінка ітерацій: {estimation:.1f}\n")
        file.write(f"Кількість ітерацій: {iterations}\n")
        file.write(f'{"Історія ітерацій:":^50}\n')

        for i, a, b, c, fc in history:
            file.write(f"{i}: a={a:.6f}, b={b:.6f}, c={c:.6f}, f(c)={fc:.6f}\n")


def main():
    a = 0.7
    b = 1
    eps = 0.00003

    root, iterations, history, estimation = bisections(target_function, a, b, eps)

    print("Корінь рівняння:", round(root, 6))
    print(f"Оцінка кількості ітерацій: {estimation:.1f}")
    print(f"Фактична кількість ітерацій: {iterations}")
    print("Історія ітерацій:")

    for i, a, b, c, fc in history:
        print(f"{i}: a={a:.6f}, b={b:.6f}, c={c:.6f}, f(c)={fc:.6f}")

    save_results_to_file(root, iterations, history, estimation)


if __name__ == "__main__":
    main()
