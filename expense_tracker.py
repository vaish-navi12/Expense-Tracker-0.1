import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Initialize session state
if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

if 'budget' not in st.session_state:
    st.session_state.budget = 0.0

def add_expense(date, category, amount, description):
    new_expense = pd.DataFrame([[date, category, amount, description]], columns=st.session_state.expenses.columns)
    st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)

def save_expenses():
    st.session_state.expenses.to_csv('expenses.csv', index=False)
    st.success("Expenses saved successfully!")

def load_expenses():
    uploaded_file = st.file_uploader("Choose a file", type=['csv'])
    if uploaded_file is not None:
        st.session_state.expenses = pd.read_csv(uploaded_file)
        st.success('Expenses loaded successfully!')

def visualize_expenses():
    if not st.session_state.expenses.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=st.session_state.expenses, x='Category', y='Amount', estimator=sum, ci=None, ax=ax)
        plt.xticks(rotation=45)
        plt.title('Total Expenses by Category')
        st.pyplot(fig)
    else:
        st.warning("No expenses to visualize.")

def remove_expense(index):
    st.session_state.expenses = st.session_state.expenses.drop(index).reset_index(drop=True)
    st.success("Expense removed successfully!")

def filter_expenses(period):
    if period == 'This Week':
        start_date = datetime.now() - timedelta(days=datetime.now().weekday())  # Start of current week
    elif period == 'This Month':
        start_date = datetime(datetime.now().year, datetime.now().month, 1)
    else:
        return st.session_state.expenses

    filtered = st.session_state.expenses[pd.to_datetime(st.session_state.expenses['Date']) >= start_date]
    return filtered

def visualize_monthly_spending():
    if not st.session_state.expenses.empty:
        df = st.session_state.expenses.copy()
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.to_period('M').astype(str)
        monthly_summary = df.groupby('Month')['Amount'].sum().reset_index()

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=monthly_summary, x='Month', y='Amount', ci=None, ax=ax)
        plt.xticks(rotation=45)
        plt.title('Month-wise Spending')
        st.pyplot(fig)
    else:
        st.warning("No expenses to visualize.")

# App Title
st.title("Your Personal Expense Tracker with Budget & Date Filters")

# Budget Section
st.header('Set Monthly Budget')
budget_input = st.number_input('Enter your monthly budget amount:', min_value=0.0, format="%.2f", value=st.session_state.budget)
if st.button('Set Budget'):
    st.session_state.budget = budget_input
    st.success(f'Budget set to Rs {st.session_state.budget:.2f}')

# Sidebar - Add Expense
with st.sidebar:
    st.header('Add Expense')
    date = st.date_input("Date")
    category = st.selectbox('Category', ['Food', 'Bills', 'Shopping', 'Travel', 'Entertainment', 'Misc'])
    amount = st.number_input('Amount', min_value=0.0, format="%.2f")
    description = st.text_input('Description')

    if st.button('Add'):
        add_expense(date, category, amount, description)
        st.success('Expense added successfully 😊')

    st.header('File Operations')
    if st.button('Save Expenses'):
        save_expenses()
    if st.button('Load Expenses'):
        load_expenses()

# Display Expenses
st.header('All Expenses')
st.write(st.session_state.expenses)

# Remove Expense
st.header('Remove Expense')
if not st.session_state.expenses.empty:
    options = [
        f"{i}: {row['Date']} | {row['Category']} | ${row['Amount']} | {row['Description']}"
        for i, row in st.session_state.expenses.iterrows()
    ]
    
    selected_expense = st.selectbox('Select an expense to remove', options)

    if st.button('Remove Selected Expense'):
        index_to_remove = int(selected_expense.split(":")[0])
        remove_expense(index_to_remove)
else:
    st.info("No expenses to remove.")

# Filter by Date Range
st.header('Filter Expenses')
period = st.selectbox('Show expenses from:', ['All Time', 'This Week', 'This Month'])
filtered_expenses = filter_expenses(period)
st.write(filtered_expenses)

total_spent = filtered_expenses['Amount'].sum() if not filtered_expenses.empty else 0.0
st.write(f"💸 Total Spent ({period}): Rs {total_spent:.2f}")

# Remaining Budget
remaining_budget = st.session_state.budget - st.session_state.expenses['Amount'].sum()
st.write(f"🏦 Monthly Budget: Rs {st.session_state.budget:.2f}")
st.write(f"💰 Remaining Budget: Rs {remaining_budget:.2f}")

# Visualization
st.header('Visualization')
if st.button('Visualize Expenses'):
    visualize_expenses()

if st.button('Visualize Month-wise Spending'):
    visualize_monthly_spending()
