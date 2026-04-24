import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import ImageTk, Image
from matplotlib.figure import Figure


root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#060a2c")






rasxodi = {
        'Переводы': 30000,
        'Фастфуд': 15000,
        'Такси': 20000,
        'Кино': 5000,
        # 'key3':'Фастфуд',
        # 'key4':'Продукты' 
        }




def Okno_rasxodi():
    window = tk.Toplevel()
    window.geometry("600x600")
    window.configure(bg="gray")

    rasxod = list(rasxodi.keys())
    count = list(rasxodi.values())

    # 3. Создание фигуры Matplotlib
    fig = plt.figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)

    # 4. Построение гистограммы
    ax.bar(rasxod, count)

    ax.set_title("Расходы за месяц")
    ax.set_xlabel("Категории")
    ax.set_ylabel("Рублей")

    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=window, )
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    # btn = Button(window, text="ррр")
    # btn.pack()


    pass





def Okno_analitika():
    # Пример данных
    # doxod = {'Зарплата': 80000, 'Подработка': 15000, 'Кэшбек': 3000}
    # rasxodi = {'Еда': 20000, 'Жилье': 35000, 'Развлечения': 10000, 'Транспорт': 7000, 'Подписки': 2500}

    # --- Расчёты ---
    total_income = sum(doxod.values())
    total_expense = sum(rasxodi.values())
    balance = total_income - total_expense
    savings_rate = (balance / total_income * 100) if total_income > 0 else 0

    # Топ расходов
    sorted_expenses = sorted(rasxodi.items(), key=lambda x: x[1], reverse=True)
    top_expense_name, top_expense_value = sorted_expenses[0] if sorted_expenses else ("Нет данных", 0)

    # Формируем выводы
    insights = []

    if balance > 0:
        insights.append(f"Ты в плюсе на {balance:,.0f} ₽")
    elif balance < 0:
        insights.append(f"Ты в минусе на {abs(balance):,.0f} ₽")
    else:
        insights.append("Доходы и расходы равны")

    if savings_rate >= 20:
        insights.append(f"Хороший темп накоплений: {savings_rate:.1f}%")
    elif savings_rate > 0:
        insights.append(f"Накопления есть, но пока умеренные: {savings_rate:.1f}%")
    else:
        insights.append("Накоплений за период нет")

    if sorted_expenses:
        share = (top_expense_value / total_expense * 100) if total_expense > 0 else 0
        insights.append(f"Самая большая статья расходов — {top_expense_name} ({share:.1f}%)")

    # --- Окно ---
    window = tk.Toplevel()
    window.title("Вся аналитика")
    window.geometry("1100x700")
    window.configure(bg="#060a2c")

    # Стили ttk
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Card.TFrame", background="#11163d")
    style.configure("Main.TFrame", background="#060a2c")
    style.configure("Title.TLabel", background="#060a2c", foreground="#E6E9FF", font=("Arial", 20, "bold"))
    style.configure("CardTitle.TLabel", background="#11163d", foreground="#AAB0FF", font=("Arial", 11))
    style.configure("CardValue.TLabel", background="#11163d", foreground="#FFFFFF", font=("Arial", 18, "bold"))
    style.configure("Section.TLabel", background="#060a2c", foreground="#E6E9FF", font=("Arial", 14, "bold"))
    style.configure("Text.TLabel", background="#11163d", foreground="#E6E9FF", font=("Arial", 11))
    style.configure("Insight.TLabel", background="#11163d", foreground="#E6E9FF", font=("Arial", 10))

    # Главный контейнер
    main = ttk.Frame(window, style="Main.TFrame", padding=15)
    main.pack(fill="both", expand=True)

    # Заголовок
    title = ttk.Label(main, text="Вся аналитика", style="Title.TLabel")
    title.pack(anchor="w", pady=(0, 15))

    # --- Верхние карточки ---
    cards_frame = ttk.Frame(main, style="Main.TFrame")
    cards_frame.pack(fill="x", pady=(0, 15))

    def create_card(parent, title_text, value_text):
        card = ttk.Frame(parent, style="Card.TFrame", padding=15)
        card.pack(side="left", fill="both", expand=True, padx=6)
        ttk.Label(card, text=title_text, style="CardTitle.TLabel").pack(anchor="w")
        ttk.Label(card, text=value_text, style="CardValue.TLabel").pack(anchor="w", pady=(8, 0))
        return card

    create_card(cards_frame, "Общий доход", f"{total_income:,.0f} ₽")
    create_card(cards_frame, "Общий расход", f"{total_expense:,.0f} ₽")
    create_card(cards_frame, "Остаток", f"{balance:,.0f} ₽")
    create_card(cards_frame, "Накопления", f"{savings_rate:.1f}%")

    # --- Средняя часть: графики + аналитика ---
    content_frame = ttk.Frame(main, style="Main.TFrame")
    content_frame.pack(fill="both", expand=True)

    left_frame = ttk.Frame(content_frame, style="Card.TFrame", padding=10)
    left_frame.pack(side="left", fill="both", expand=True, padx=(0, 8))

    right_frame = ttk.Frame(content_frame, style="Card.TFrame", padding=15)
    right_frame.pack(side="right", fill="y", padx=(8, 0))

    # --- Графики ---
    fig = Figure(figsize=(8, 5), dpi=100)
    fig.patch.set_facecolor("#11163d")

    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.set_facecolor("#11163d")
    ax2.set_facecolor("#11163d")

    # Диаграмма доходов
    if total_income > 0:
        ax1.pie(
            doxod.values(),
            labels=doxod.keys(),
            autopct='%1.1f%%',
            startangle=90
        )
    ax1.set_title("Источники доходов", color="white", fontsize=12)

    # Диаграмма расходов
    if total_expense > 0:
        ax2.pie(
            rasxodi.values(),
            labels=rasxodi.keys(),
            autopct='%1.1f%%',
            startangle=90
        )
    ax2.set_title("Структура расходов", color="white", fontsize=12)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=left_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # --- Правая панель аналитики ---
    ttk.Label(right_frame, text="Выводы", style="Section.TLabel").pack(anchor="w", pady=(0, 10))

    for text in insights:
        ttk.Label(right_frame, text=f"• {text}", style="Insight.TLabel", wraplength=260, justify="left").pack(anchor="w", pady=4)

    ttk.Label(right_frame, text="", style="Text.TLabel").pack()

    ttk.Label(right_frame, text="Топ расходов", style="Section.TLabel").pack(anchor="w", pady=(15, 10))

    if sorted_expenses:
        for i, (name, value) in enumerate(sorted_expenses[:3], start=1):
            percent = (value / total_expense * 100) if total_expense > 0 else 0
            ttk.Label(
                right_frame,
                text=f"{i}. {name} — {value:,.0f} ₽ ({percent:.1f}%)",
                style="Text.TLabel",
                wraplength=260,
                justify="left"
            ).pack(anchor="w", pady=3)
    else:
        ttk.Label(right_frame, text="Нет данных по расходам", style="Text.TLabel").pack(anchor="w")

    ttk.Label(right_frame, text="", style="Text.TLabel").pack()

    ttk.Label(right_frame, text="Краткая статистика", style="Section.TLabel").pack(anchor="w", pady=(15, 10))

    avg_expense = total_expense / len(rasxodi) if rasxodi else 0
    ttk.Label(right_frame, text=f"Средний расход по категории: {avg_expense:,.0f} ₽", style="Text.TLabel", wraplength=260, justify="left").pack(anchor="w", pady=3)
    ttk.Label(right_frame, text=f"Категорий дохода: {len(doxod)}", style="Text.TLabel").pack(anchor="w", pady=3)
    ttk.Label(right_frame, text=f"Категорий расхода: {len(rasxodi)}", style="Text.TLabel").pack(anchor="w", pady=3)

    # plt.show()





    pass

doxod = {
    'Фриланс': 30000,
    'Подработка в кафе': 15000,
    'Основная работа': 60000,
    }

def Okno_Doxod():
    window = tk.Toplevel()
    window.geometry("600x600")
    window.configure(bg="#060a2c")

    rasxod = list(doxod.keys())
    count = list(doxod.values())

    # fig = plt.figure(figsize=(5, 4), dpi=100)
    # ax = fig.add_subplot(111)

    # 4. Построение гистограммы
    # ax.bar(rasxod, count)

    total = sum(doxod.values())

    def func(pct):
        # pct - это процент, который Matplotlib считает сам
        absolute = int(round(pct / 100. * total))
        return f"{absolute} руб\n({pct:.1f}%)"

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111)
    plt.pie(doxod.values(), labels=doxod.keys(), autopct=func)
    plt.title('Доход за месяц ')

    # ax.bar(rasxod, count)

    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=window,  )
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    pass

# def Okno_category():
#     window = tk.Toplevel()
#     window.geometry("600x300")
#     window.configure(bg="gray")

    # btn = Button(window, text="")


s = Style()

s.configure('TButton', font = ('calibri', 18 , 'bold') )
s.map('TButton', foreground = [('active', '!disabled', 'black')],
                     background = [('active', 'black')])

style = ttk.Style()
style.configure("Bold.TLabel",
                foreground="white",
                background="#060a2c",
                font=("Helvetica", 28, "bold"))

canvas = tk.Canvas(root, width=500, height=550, highlightthickness=0, bg="#060a2c")
canvas.place(x = 110, y = 100)

img = ImageTk.PhotoImage(Image.open("money4.png"))
canvas.create_image(200, 200, image=img)


l = ttk.Label(root, text="Распределитель доходов", style="Bold.TLabel")
l.pack(pady=40)

btn = Button(root, text="Вся аналитика", command=Okno_analitika, width=15)
btn.place(x = 500, y = 150)

btn2 = Button(root, text="Расходы", command=Okno_rasxodi, width=15)
btn2.place(x = 500, y = 275)

btn3 = Button(root, text="Доходы", command=Okno_Doxod, width=15)
btn3.place(x = 500, y = 400)

# btn4 = Button(root, text="Категории", command=Okno_category)
# btn4.place(x = 400, y = 350)




root.mainloop()