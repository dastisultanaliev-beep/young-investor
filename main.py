import customtkinter as ctk
import sqlite3
import random

conn = sqlite3.connect('invest.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        year INTEGER,
        capital REAL
    )
""")
conn.commit()

capital = 100000
year = 0

cursor.execute("SELECT year, capital FROM history ORDER BY id DESC LIMIT 1")
last_record = cursor.fetchone()
if last_record:
    year, capital = last_record

deposit_result_text = 'Пока нет результата'
stock_result_text = 'Пока нет результата'
crypto_result_text = 'Пока нет результата'

BG = '#131a26'
CARD = '#1c2536'
BORDER = '#2a3550'
TEXT = '#e8ecf4'
MUTED = '#8b95ab'
GREEN = '#3ddc97'
RED = '#ff6b6b'
BLUE = '#5b8cff'
ORANGE = '#ffb454'


def format_money(value):
    return f'{round(value):,}'.replace(',', ' ') + ' ₽'


def read_number(entry):
    text = entry.get().replace(' ', '').replace(',', '.')
    if text == '':
        return 0
    return float(text)


def save_history():
    global year
    global capital

    cursor.execute("""
        INSERT INTO history (year, capital)
        VALUES (?, ?)
    """, (year, capital))
    conn.commit()


def next_year():
    global capital
    global year
    global deposit_result_text
    global stock_result_text
    global crypto_result_text

    try:
        deposit = read_number(deposit_entry)
        stocks = read_number(stocks_entry)
        crypto = read_number(crypto_entry)
    except ValueError:
        result_label.configure(text='Введите числа!', text_color=RED)
        return

    if deposit < 0 or stocks < 0 or crypto < 0:
        result_label.configure(text='Числа не могут быть отрицательными!', text_color=RED)
        return

    total_invested = deposit + stocks + crypto
    if total_invested > capital:
        result_label.configure(text='У тебя столько нет!', text_color=RED)
        return

    cash = capital - total_invested

    deposit_percent = 0.05
    deposit_after = deposit * (1 + deposit_percent)

    stocks_percent = random.uniform(-0.20, 0.30)
    stocks_after = stocks * (1 + stocks_percent)

    crypto_percent = random.uniform(-0.70, 1.50)
    crypto_after = crypto * (1 + crypto_percent)

    deposit_result_text = f'{format_money(deposit)} → {format_money(deposit_after)}   +5%'
    stock_result_text = f'{format_money(stocks)} → {format_money(stocks_after)}   {round(stocks_percent * 100):+}%'
    crypto_result_text = f'{format_money(crypto)} → {format_money(crypto_after)}   {round(crypto_percent * 100):+}%'

    old_capital = capital
    capital = cash + deposit_after + stocks_after + crypto_after
    year = year + 1
    save_history()

    deposit_entry.delete(0, 'end')
    stocks_entry.delete(0, 'end')
    crypto_entry.delete(0, 'end')

    capital_label.configure(text=format_money(capital))
    year_label.configure(text=f'Год: {year}')

    deposit_result_label.configure(text=deposit_result_text, text_color=GREEN if deposit > 0 else MUTED)
    stocks_result_label.configure(text=stock_result_text, text_color=GREEN if stocks_percent >= 0 else RED)
    crypto_result_label.configure(text=crypto_result_text, text_color=GREEN if crypto_percent >= 0 else RED)

    color = GREEN if capital >= old_capital else RED
    result_label.configure(text=f'Год {year} завершен! Теперь у тебя {format_money(capital)}', text_color=color)


def show_history():
    cursor.execute("""
        SELECT year, capital
        FROM history
        ORDER BY year
    """)

    records = cursor.fetchall()
    if not records:
        result_label.configure(text='История пока пуста', text_color=MUTED)
        return

    history_text = 'Последние годы:\n\n'
    for record in records[-8:]:
        saved_year = record[0]
        saved_capital = record[1]
        history_text += f'Год {saved_year}  |  {format_money(saved_capital)}\n'
    result_label.configure(text=history_text, text_color=TEXT)


def reset_game():
    global capital
    global year

    cursor.execute("DELETE FROM history")
    conn.commit()

    capital = 100000
    year = 0

    capital_label.configure(text=format_money(capital))
    year_label.configure(text='Год: 0')
    deposit_result_label.configure(text='Пока нет результата', text_color=MUTED)
    stocks_result_label.configure(text='Пока нет результата', text_color=MUTED)
    crypto_result_label.configure(text='Пока нет результата', text_color=MUTED)
    result_label.configure(text='Распредели свои 100 000 рублей', text_color=MUTED)


def create_card(title, subtitle, color):
    card = ctk.CTkFrame(app, fg_color=CARD, corner_radius=14, border_width=1, border_color=BORDER)
    card.pack(fill='x', padx=30, pady=6)

    header = ctk.CTkFrame(card, fg_color='transparent')
    header.pack(fill='x', padx=16, pady=(12, 0))

    ctk.CTkLabel(header, text=title, font=('Arial', 17, 'bold'), text_color=TEXT).pack(side='left')
    ctk.CTkLabel(header, text=subtitle, font=('Arial', 12), text_color=color).pack(side='right')

    result = ctk.CTkLabel(card, text='Пока нет результата', font=('Arial', 13), text_color=MUTED)
    result.pack(anchor='w', padx=16, pady=(2, 4))

    entry = ctk.CTkEntry(
        card,
        placeholder_text='Сколько вложить?',
        height=36,
        font=('Arial', 14),
        fg_color=BG,
        border_color=BORDER,
        text_color=TEXT
    )
    entry.pack(fill='x', padx=16, pady=(0, 14))

    return result, entry


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.title('Юный инвестор')
app.geometry('600x820')
app.resizable(False, False)
app.configure(fg_color=BG)

title_label = ctk.CTkLabel(app, text='Юный инвестор 🤓', font=('Arial', 28, 'bold'), text_color=TEXT)
title_label.pack(pady=(22, 4))

capital_label = ctk.CTkLabel(app, text=format_money(capital), font=('Arial', 34, 'bold'), text_color=GREEN)
capital_label.pack()

year_label = ctk.CTkLabel(app, text=f'Год: {year}', font=('Arial', 16), text_color=MUTED)
year_label.pack(pady=(0, 12))

deposit_result_label, deposit_entry = create_card('Банковский вклад', 'Без риска, +5%', GREEN)
stocks_result_label, stocks_entry = create_card('Акции', 'Риск: от −20% до +30%', BLUE)
crypto_result_label, crypto_entry = create_card('Криптовалюта', 'Риск: от −70% до +150%', ORANGE)

next_year_button = ctk.CTkButton(
    app,
    text='Промотать 1 год',
    command=next_year,
    height=48,
    font=('Arial', 17, 'bold'),
    fg_color=BLUE,
    hover_color='#4574e6',
    corner_radius=12
)
next_year_button.pack(fill='x', padx=30, pady=(18, 8))

buttons_frame = ctk.CTkFrame(app, fg_color='transparent')
buttons_frame.pack(fill='x', padx=30)

history_button = ctk.CTkButton(
    buttons_frame,
    text='Показать историю',
    command=show_history,
    height=38,
    font=('Arial', 14),
    fg_color=CARD,
    hover_color=BORDER,
    border_width=1,
    border_color=BORDER,
    corner_radius=12
)
history_button.pack(side='left', expand=True, fill='x', padx=(0, 5))

reset_button = ctk.CTkButton(
    buttons_frame,
    text='Новая игра',
    command=reset_game,
    height=38,
    font=('Arial', 14),
    fg_color=CARD,
    hover_color=BORDER,
    border_width=1,
    border_color=BORDER,
    corner_radius=12
)
reset_button.pack(side='left', expand=True, fill='x', padx=(5, 0))

result_label = ctk.CTkLabel(app, text='Распредели свои 100 000 рублей', font=('Arial', 15), text_color=MUTED, justify='left')
result_label.pack(pady=16)

app.bind('<Return>', lambda event: next_year())

app.mainloop()
conn.close()
