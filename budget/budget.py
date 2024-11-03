import streamlit as st

# Title of the app
st.title("Simple Budget Calculator")

# User input for income
st.header("Income")
income = st.number_input("Enter your monthly income ($):", min_value=0.0, step=100.0)

# User input for expenses
st.header("Expenses")
rent = st.number_input("Enter your rent expense ($):", min_value=0.0, step=50.0)
utilities = st.number_input("Enter your utilities expense ($):", min_value=0.0, step=10.0)
groceries = st.number_input("Enter your groceries expense ($):", min_value=0.0, step=20.0)
transport = st.number_input("Enter your transport expense ($):", min_value=0.0, step=10.0)
entertainment = st.number_input("Enter your entertainment expense ($):", min_value=0.0, step=10.0)
other_expenses = st.number_input("Enter any other expenses ($):", min_value=0.0, step=10.0)

# Calculate total expenses
total_expenses = rent + utilities + groceries + transport + entertainment + other_expenses

# Calculate remaining budget
remaining_budget = income - total_expenses

# Display the total expenses and remaining budget
st.header("Summary")
st.write(f"**Total Expenses:** ${total_expenses:.2f}")
st.write(f"**Remaining Budget:** ${remaining_budget:.2f}")

# Display a message based on the remaining budget
if remaining_budget > 0:
    st.success(f"You are within your budget! You have ${remaining_budget:.2f} left.")
elif remaining_budget == 0:
    st.warning("You have exactly used up your budget.")
else:
    st.error(f"You are over budget by ${abs(remaining_budget):.2f}. Try adjusting your expenses.")
