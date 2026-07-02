"""
CodeAlpha_StockPortfolioTracker
--------------------------------
A console-based Stock Portfolio Tracker.

Features:
- Hardcoded live-style stock price dictionary
- Add multiple stocks with quantity to your portfolio
- Auto-validates stock symbols against available list
- Calculates total investment + per-stock breakdown
- Shows percentage allocation of each stock in portfolio
- Saves a nicely formatted report to a .txt AND .csv file
- Clean menu-driven interface with error handling

Key Concepts Used: dictionary, input/output, arithmetic, file handling, loops
Author: Aryan
"""

import csv
from datetime import datetime

# ---------------- Hardcoded Stock Price Data ----------------
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 415,
    "NFLX": 610,
    "META": 480,
    "NVDA": 890,
    "INFY": 1550,   # Indian stock example (in INR)
    "TCS": 3800,
    "RELIANCE": 2950,
    "HDFC": 1650,
}

portfolio = {}  # {symbol: quantity}


def show_banner():
    print("=" * 55)
    print("        📈  STOCK PORTFOLIO TRACKER  📉")
    print("=" * 55)


def show_available_stocks():
    print("\nAvailable Stocks & Current Prices:")
    print("-" * 35)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<10}₹/$ {price}")
    print("-" * 35)


def add_stock():
    symbol = input("\nEnter stock symbol (e.g. AAPL): ").strip().upper()

    if symbol not in STOCK_PRICES:
        print(f"❌ '{symbol}' not found in our stock list. Try again.")
        return

    try:
        qty = int(input(f"Enter quantity of {symbol} to buy: "))
        if qty <= 0:
            print("❌ Quantity must be a positive number.")
            return
    except ValueError:
        print("❌ Please enter a valid whole number.")
        return

    portfolio[symbol] = portfolio.get(symbol, 0) + qty
    print(f"✅ Added {qty} share(s) of {symbol} to your portfolio.")


def view_portfolio():
    if not portfolio:
        print("\n⚠️ Your portfolio is empty. Add some stocks first!")
        return None

    total_value = sum(STOCK_PRICES[sym] * qty for sym, qty in portfolio.items())

    print("\n" + "=" * 55)
    print(f"{'Symbol':<10}{'Qty':<8}{'Price':<10}{'Value':<12}{'% of Portfolio'}")
    print("-" * 55)

    breakdown = []
    for sym, qty in portfolio.items():
        value = STOCK_PRICES[sym] * qty
        percent = (value / total_value) * 100
        breakdown.append((sym, qty, STOCK_PRICES[sym], value, percent))
        print(f"{sym:<10}{qty:<8}{STOCK_PRICES[sym]:<10}{value:<12}{percent:.1f}%")

    print("-" * 55)
    print(f"💰 TOTAL INVESTMENT VALUE: {total_value}")
    print("=" * 55)
    return total_value, breakdown


def save_report(total_value, breakdown):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Save as TXT
    txt_filename = f"portfolio_report_{timestamp}.txt"
    with open(txt_filename, "w") as f:
        f.write("STOCK PORTFOLIO REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write("=" * 45 + "\n")
        f.write(f"{'Symbol':<10}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
        for sym, qty, price, value, percent in breakdown:
            f.write(f"{sym:<10}{qty:<8}{price:<10}{value:<10}({percent:.1f}%)\n")
        f.write("-" * 45 + "\n")
        f.write(f"TOTAL INVESTMENT: {total_value}\n")

    # Save as CSV
    csv_filename = f"portfolio_report_{timestamp}.csv"
    with open(csv_filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price", "Value", "Percent"])
        for sym, qty, price, value, percent in breakdown:
            writer.writerow([sym, qty, price, value, f"{percent:.1f}%"])
        writer.writerow([])
        writer.writerow(["TOTAL", "", "", total_value, ""])

    print(f"\n📁 Report saved as:\n   - {txt_filename}\n   - {csv_filename}")


def main():
    show_banner()
    while True:
        print("\n1. View Available Stocks")
        print("2. Add Stock to Portfolio")
        print("3. View Portfolio & Total Investment")
        print("4. Save Report (.txt + .csv)")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_available_stocks()
        elif choice == "2":
            add_stock()
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            result = view_portfolio()
            if result:
                save_report(*result)
        elif choice == "5":
            print("\n👋 Thanks for using Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select between 1-5.")


if __name__ == "__main__":
    main()