# Завдання 1
import random

num = random.randint(1, 10)
print("Guess the number from 1 to 10")

while True:
    try:
        num_2 = int(input("Your option: "))
    except ValueError:
        print("Wrong value !!!")
        print("Try again")
        continue

    if (num > num_2):
        print("More")
    elif (num < num_2):
        print("Less")
    else:
        print("YOU WIN!")
        break

# Завдання 2
import random

num = random.randint(1, 50)
print("Guess the number from 1 to 50")
while True:
    try:
        num_2 = int(input("Your option: "))
    except ValueError:
        print("Wrong value !!!")
        print("Try again")
        continue

    if (num == num_2):
        print("Ти переміг!")
        break
    elif (-3 <= num - num_2 and num - num_2 <= 3):
        print("Дуже близько!")
    elif (-10 <= num - num_2 and num - num_2 <= 10):
        print("Близько")
    else:
        print("Далеко")

# Завдання 3
import random

secret_code = random.randint(1, 20)
attempts = 3

print("Вгадайте число від 1 до 20. У вас є 3 спроби, щоб його вгадати.")

while attempts > 0:
    try:
        guess = int(input("Введіть ваше припущення: "))

        if guess == secret_code:
            print("Ви перемогли!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Неправильно. У вас залишилося {attempts} спроб.")
            else:
                print("У вас закінчилися спроби. Ви програли.")
                print(f"Загадане число було: {secret_code}")
    except ValueError:
        print("Будь ласка, введіть ціле число.")

# Завдання 4
import random

def guess_the_pin():
    secret_pin = "".join([str(random.randint(0, 9)) for _ in range(4)])
    attempts = 5

    print("Ласкаво просимо до гри 'Вгадай PIN-код'!")
    print("Я згенерував чотиризначний PIN-код. У вас є 5 спроб, щоб його вгадати.")

    while attempts > 0:
        guess = input("Введіть ваш PIN-код: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Будь ласка, введіть рівно 4 цифри.")
            continue

        if guess == secret_pin:
            print("Вітаємо! Ви вгадали PIN-код.")
            return
        else:
            attempts -= 1
            correct_positions = sum(1 for i in range(4) if guess[i] == secret_pin[i])
            if attempts > 0:
                print(f"Невірно. Правильних цифр на правильних позиціях: {correct_positions}.")
                print(f"У вас залишилося {attempts} спроб.")
            else:
                print("У вас закінчилися спроби. Ви програли.")
                print(f"Секретний PIN-код був: {secret_pin}")

if __name__ == "__main__":
    guess_the_pin()

# Завдання 5
import random
import tkinter as tk
from tkinter import messagebox

def play_game():
    colors = {
        "червоний": "теплий",
        "жовтий": "теплий",
        "синій": "холодний",
        "зелений": "холодний",
        "фіолетовий": "холодний"
    }
    secret_color = random.choice(list(colors.keys()))
    attempts = 3

    def check_guess():
        nonlocal attempts
        guess = entry.get().strip().lower()

        if guess not in colors:
            messagebox.showerror("Помилка", "Будь ласка, оберіть колір із запропонованих: червоний, синій, зелений, жовтий, фіолетовий.")
            return

        if guess == secret_color:
            messagebox.showinfo("Перемога!", "Вітаємо! Ви вгадали колір.")
            root.destroy()
        else:
            attempts -= 1
            hint = colors[secret_color]
            if attempts > 0:
                messagebox.showinfo("Невірно", f"Невірно. Загаданий колір належить до категорії '{hint}'. У вас залишилося {attempts} спроб.")
            else:
                messagebox.showinfo("Програш", f"Ви програли. Загаданий колір був: {secret_color}")
                root.destroy()

    root = tk.Tk()
    root.title("Гра 'Вгадай колір'")

    tk.Label(root, text="Я загадав один із наступних кольорів: червоний, синій, зелений, жовтий, фіолетовий.").pack(pady=10)
    tk.Label(root, text="Спробуйте вгадати! У вас є 3 спроби.").pack(pady=5)

    entry = tk.Entry(root, width=20)
    entry.pack(pady=5)

    tk.Button(root, text="Вгадати", command=check_guess).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    play_game()

