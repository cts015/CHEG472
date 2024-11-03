import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate solute distribution between two phases (based on distribution ratio)
def calculate_distribution(c_s, D):
    c_o = D * c_s  # Solute concentration in organic phase
    return c_o

# Streamlit app interface
st.title("Liquid-Liquid Extraction: Tie-Line Diagram")

# Input section for solute concentration in aqueous phase and distribution ratio
st.header("Input Data for Liquid-Liquid Extraction")
c_s = st.number_input("Initial solute concentration in aqueous phase (mol/L)", value=0.1, min_value=0.01, max_value=1.0, step=0.01)
D = st.number_input("Distribution Ratio (D)", value=2.0, min_value=0.1, max_value=10.0, step=0.1)

# Generate solute concentrations in aqueous phase (x-axis)
c_s_range = np.linspace(0.01, 1.0, 100)  # Solute concentrations in aqueous phase
c_o_range = calculate_distribution(c_s_range, D)  # Corresponding concentrations in organic phase

# Plotting the tie-line diagram (c_s vs. c_o)
st.header("Tie-Line Diagram: Solute Distribution between Phases")
fig, ax = plt.subplots()

# Plot solute distribution in both phases
ax.plot(c_s_range, c_o_range, label="Tie Line", color='blue')

# Add labels and title
ax.set_xlabel("Solute Concentration in Aqueous Phase (mol/L)")
ax.set_ylabel("Solute Concentration in Organic Phase (mol/L)")
ax.set_title("Tie-Line Diagram: Liquid-Liquid Extraction")
ax.legend()

# Display the plot in Streamlit
st.pyplot(fig)

# Output the calculated solute concentrations for the given initial concentration
c_o = calculate_distribution(c_s, D)
st.write(f"For an initial solute concentration of {c_s:.2f} mol/L in the aqueous phase, the solute concentration in the organic phase is {c_o:.2f} mol/L.")

# Conclusion and analysis
st.write("""
This tie-line diagram illustrates the equilibrium distribution of a solute between two immiscible phases (aqueous and organic).
The slope of the line depends on the distribution ratio (D), which is the ratio of solute concentration in the organic phase to that in the aqueous phase.
A higher D indicates that the solute prefers the organic phase, while a lower D indicates preference for the aqueous phase.
""")
