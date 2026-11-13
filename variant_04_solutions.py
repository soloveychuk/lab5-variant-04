"""
Лабораторна робота: Варіант 4
Студент: Бучак Олег
Група: EIP30
"""
# Функція, корінь якої потрібно знайти
import math 
def target_function(x):
    return math.tan(x) - 1/x

# Пошук кореня методом ділення навпіл
def bisections(func, a, b, eps = 0.00003):
    iterations = 0 #змінна для к-сті ітерацій
    history = [] #список для збереження історії обчислень
    estimation=math.log2((b-a)/eps) #оцінка кількості ітерацій
    while (b-a)/2 >= eps:
        c=(a+b)/2 #точка середини інтервалу
        fc=func(c) #значення функції в точці с
        iterations +=1
        history.append((iterations, a, b, c, fc)) #зберігаємо дані ітерації
        if fc == 0: #якщо fc=0, то ми знайшли точний корінь
            return c, iterations, history, estimation
        if func(a)*fc < 0: #скорочуємо інтервал пошуку у 2 рази, в залежності від знаку дивимося яка частина нас цікавть,права чи ліва
            b = c
        else:
            a = c
    root = (a+b)/2 #приблизне значення кореня

    return root, iterations, history, estimation #повертаємо корінь, к-сть ітерацій, історію ітерацій і оцінку



def save_results_to_file(root, iterations, history, estimation):
    with open("results_variant_04.txt", "w", encoding="utf-8") as file:
        file.write(f"Корінь: {root:.6f}\n")
        file.write(f"Оцінка ітерацій: {estimation:.1f}\n")
        file.write(f"Кількість ітерацій: {iterations}\n")
        file.write(f'{"Історія ітерацій:":^64}\n')

        file.write("-" * 62 + "\n")
        file.write(f"| {'N':^3} | {'a':^10} | {'b':^10} | {'c':^10} | {'f(c)':^12} |\n")
        file.write("-" * 62 + "\n")

        for i, a, b, c, fc in history:
            file.write(f"| {i:^3} | {a:>10.6f} | {b:>10.6f} | {c:>10.6f} | {fc:>12.6f} |\n")

        file.write("-" * 62 + "\n")


def main(): #головна ф-ція програми
    #початкові умови
    a = 0.5
    b = 1
    eps = 0.00003

 #викликаємо метод бісекцій і отримуємо результати
    root, iterations, history, estimation = bisections(target_function, a, b, eps)

    print("Корінь рівняння:", round(root, 6))
    print(f"Оцінка кількості ітерацій: {estimation:.1f}")
    print(f"Фактична кількість ітерацій: {iterations}")
    print("Історія ітерацій:")

    #перебираємо ітерації і дял кожної записуємо дані в окремий рядок
    for i, a, b, c, fc in history:
        print(f"{i}: a={a:.6f}, b={b:.6f}, c={c:.6f}, f(c)={fc:.6f}")

    save_results_to_file(root, iterations, history, estimation) #записуємо результати у файл

#запускаємо головну функцію при запуску файлу
if __name__ == "__main__":
    main()
