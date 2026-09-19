# 💰 Young Investor

A simple investment simulator built with **Python**, **CustomTkinter**, and **SQLite**.

The goal of the game is to manage your virtual capital by distributing money between a bank deposit, stocks, and cryptocurrency.

## ✨ Features

* 💵 Start with **100,000 ₽**
* 🏦 Invest in a bank deposit
* 📈 Invest in stocks with random returns
* 🪙 Invest in cryptocurrency with higher risk
* 📊 Simulate one year at a time
* 💾 Save game history using SQLite
* 📜 View previous years and capital
* 🔄 Reset the game and start over
* 🌙 Dark modern interface
* ⌨️ Press `Enter` to simulate the next year

## 🎯 Investment Types

| Investment        | Return        |
| ----------------- | ------------- |
| 🏦 Bank Deposit   | +5%           |
| 📈 Stocks         | -20% to +30%  |
| 🪙 Cryptocurrency | -70% to +150% |

The returns for stocks and cryptocurrency are randomly generated for each year.

## 🛠️ Technologies

* **Python 3**
* **CustomTkinter** — graphical user interface
* **SQLite** — saving game history
* **random** — generating investment returns

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/young-investor.git
cd young-investor
```

Install the required package:

```bash
pip install customtkinter
```

Run the program:

```bash
python main.py
```

## 📁 Project Structure

```text
young-investor/
│
├── main.py
├── invest.db
└── README.md
```

> `invest.db` is created automatically when the program starts if it doesn't already exist.

## 🎮 How to Play

1. Start with **100,000 ₽**.
2. Enter how much money you want to invest in each category.
3. Click **"Промотать 1 год"**.
4. Your investments will change according to their returns.
5. Check your new capital.
6. Use **"Показать историю"** to see previous years.
7. Use **"Новая игра"** to reset everything.

## 📚 What I Learned

This project helped me practice:

* Python functions
* Global variables
* Classes and GUI programming concepts
* SQLite databases
* SQL queries
* Exception handling
* Working with random numbers
* Input validation
* GUI layouts with CustomTkinter
* Saving and loading application data

## 🔮 Possible Improvements

Future versions could include:

* 📊 Investment charts
* 📅 More detailed statistics
* 📰 Random economic events
* 🏆 Achievements
* 🎯 Investment goals
* 📈 More types of investments
* 💼 Different difficulty levels
* 🎨 More UI animations

## 📄 License

This project is for educational purposes.
