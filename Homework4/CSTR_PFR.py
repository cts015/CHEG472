import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Functions to calculate reactor volumes
def cstr_volume(F, k, X):
    """Calculate CSTR volume"""
    if X == 1:
        return np.inf
    return (F / k) * (X / (1 - X))

def pfr_volume(F, k, X):
    """Calculate PFR volume"""
    if X == 1:
        return np.inf
    return (F / k) * np.log(1 / (1 - X))

# Function to plot conversion profile along PFR length
def pfr_conversion_profile(F, k, X, n_points=100):
    """Generate conversion profile for a PFR"""
    length = np.linspace(0, pfr_volume(F, k, X), n_points)
    conversion = 1 - np.exp(-k * length / F)
    return length, conversion

# Streamlit App
st.title("CSTR vs PFR Reactor Volume Calculator")

# Input fields
F = st.number_input("Feed rate (mol/s)", value=1.0, min_value=0.1, step=0.1)
k = st.number_input("Reaction rate constant (1/s)", value=0.1, min_value=0.01, step=0.01)
X = st.slider("Target conversion", min_value=0.0, max_value=0.99, value=0.80, step=0.01)

# Calculate volumes
V_CSTR = cstr_volume(F, k, X)
V_PFR = pfr_volume(F, k, X)

# Display results
st.subheader("Results")
st.write(f"**CSTR Volume:** {V_CSTR:.2f} m³")
st.write(f"**PFR Volume:** {V_PFR:.2f} m³")

# Compare performance
st.subheader("Comparison of Reactor Volumes")
st.write("For the same conversion, the CSTR requires a larger volume than the PFR.")

# Plot PFR conversion profile
st.subheader("PFR Conversion Profile Along Reactor Length")
length, conversion = pfr_conversion_profile(F, k, X)
fig, ax = plt.subplots()
ax.plot(length, conversion, label="Conversion Profile")
ax.set_xlabel("Reactor Length (m)")
ax.set_ylabel("Conversion")
ax.set_title("PFR Conversion Profile")
ax.legend()
st.pyplot(fig)

# Plot CSTR conversion vs. reactor volume
st.subheader("CSTR Conversion vs. Reactor Volume")
volumes = np.linspace(0.01, V_CSTR, 100)
conversions = volumes / (volumes + (F / k))
fig2, ax2 = plt.subplots()
ax2.plot(volumes, conversions, label="Conversion vs Volume")
ax2.set_xlabel("Reactor Volume (m³)")
ax2.set_ylabel("Conversion")
ax2.set_title("CSTR Conversion vs Reactor Volume")
ax2.legend()
st.pyplot(fig2)
