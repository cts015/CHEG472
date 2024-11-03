import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the dissolved oxygen level iteratively
def calculate_do(do, t, otr, consumption_rate):
    # Iteratively calculate DO at each time step
    dt = t[1] - t[0]  # Time step
    for i in range(1, len(t)):
        # Oxygen transfer rate (OTR) - Oxygen consumption rate
        ddo = otr * (1 - do[i-1]/9.0) - consumption_rate
        do[i] = do[i-1] + ddo * dt  # Update DO based on OTR and consumption
        # DO can't fall below zero
        if do[i] < 0:
            do[i] = 0
    return do

# Streamlit app interface
st.title("Wastewater Treatment: Dissolved Oxygen Profile in Aeration Tank")

# Display a fancy wastewater treatment image
st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Wastewater_Treatment_2.jpg", caption="Aeration Tank in Wastewater Treatment", use_column_width=True)

# Input parameters for simulation
st.sidebar.header("Oxygen Transfer and Consumption Parameters")
ote = st.sidebar.slider("Oxygen Transfer Efficiency (OTE, %)", 0, 100, 20)  # Oxygen transfer efficiency
otr = ote / 100  # Convert to a fraction for OTR calculation
consumption_rate = st.sidebar.slider("Oxygen Consumption Rate (mg/L/min)", 0.0, 1.0, 0.1)
initial_do = st.sidebar.slider("Initial Dissolved Oxygen (DO, mg/L)", 0.0, 9.0, 2.0)  # Initial DO level

# Time array for simulation (minutes)
t = np.linspace(0, 120, 120)

# Initialize DO array with initial value
do = np.zeros_like(t)
do[0] = initial_do

# Calculate DO profile
do_profile = calculate_do(do, t, otr, consumption_rate)

# Plot the results
st.header("Dissolved Oxygen Profile in the Aeration Tank")
fig, ax = plt.subplots()
ax.plot(t, do_profile, label="DO Level", color='blue')
ax.axhline(y=2.0, color='red', linestyle='--', label="Minimum DO Threshold (2 mg/L)")
ax.set_xlabel("Time (minutes)")
ax.set_ylabel("Dissolved Oxygen (mg/L)")
ax.set_title("DO Concentration Over Time in Aeration Tank")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Display DO levels over time
st.write(f"Final Dissolved Oxygen Level: {do_profile[-1]:.2f} mg/L")

# Explanation of the simulation
st.write("""
### Oxygen Transfer in Wastewater Treatment
This simulation models the dissolved oxygen (DO) concentration over time in an aeration tank during wastewater treatment. Oxygen is transferred into the water to support microbial processes that consume oxygen to break down organic material.

- **Oxygen Transfer Efficiency (OTE)**: The percentage of oxygen that is effectively transferred into the water.
- **Oxygen Consumption Rate**: The rate at which oxygen is consumed by the microbes.
- **Initial Dissolved Oxygen (DO)**: The starting concentration of DO in the tank.

You can adjust these parameters to see how they affect the DO profile in the aeration tank.
""")
