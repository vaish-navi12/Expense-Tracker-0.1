# Expense Tracker

A simple expense tracking web app built with **Streamlit**, **Pandas**, **Matplotlib**, and **Seaborn**. Add, view, filter, and visualize your expenses right from your browser.

🔗 **Live Demo:** [trac-expenses.onrender.com](https://trac-expenses.onrender.com)
## Features

- 📥 Add new expenses with date, category, amount, and description
- 📊 Visualize total expenses by category with bar charts
- 📅 Filter expenses by "This Week" or "This Month"
- 💾 Save expenses to a CSV file
- 📤 Upload and load a previously saved CSV of expenses
- 🗑️ Remove individual expenses
  

## Tech Stack

- [Streamlit](https://streamlit.io/) — web app framework
- [Pandas](https://pandas.pydata.org/) — data handling
- [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/) — data visualization

## Getting Started

### Prerequisites

- Python 3.9+ installed

### Installation

1. Clone the repository:
```bash
   git clone https://github.com/vaish-navi12/Expense-Tracker-0.1.git
   cd Expense-Tracker-0.1
```

2. Install the dependencies:
```bash
   pip install -r requirements.txt
```

3. Run the app:
```bash
   streamlit run expense_tracker.py
```

4. Open the URL shown in your terminal (usually `http://localhost:8501`) in your browser.

## Usage

1. Enter expense details (date, category, amount, description) and add them to your tracker.
2. Use the visualization option to see a bar chart of your spending by category.
3. Filter your expenses by week or month.
4. Save your expenses to `expenses.csv`, or upload an existing CSV to load past data.


