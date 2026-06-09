import tkinter as tk
from tkinter import messagebox

def esepteu():
    try:
        san = float(entry.get())

        kvadrat = san ** 2
        kub = san ** 3

        natizhe.config(
            text=f"Квадраты: {kvadrat}\nКубы: {kub}"
        )

    except ValueError:
        natizhe.config(text="Қате: Сан енгізіңіз!")
        messagebox.showerror("Қате", "Сан енгізіңіз!")

# Терезе құру
window = tk.Tk()
window.title("Санның квадратын және кубын есептеу")
window.geometry("350x250")

# Жазулар
label = tk.Label(window, text="Санды енгізіңіз:", font=("Arial", 12))
label.pack(pady=10)

# Енгізу өрісі
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=5)

# Батырма
button = tk.Button(window, text="Есептеу", font=("Arial", 12), command=esepteu)
button.pack(pady=10)

# Нәтиже
natizhe = tk.Label(window, text="Нәтиже:", font=("Arial", 12))
natizhe.pack(pady=10)

# Бағдарламаны іске қосу
window.mainloop()