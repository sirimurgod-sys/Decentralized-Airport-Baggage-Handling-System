import matplotlib.pyplot as plt
import numpy as np

# Data reconstructed from your histogram
data = [160, 165, 170, 175, 215]  # Represents frequencies: 2,2,0,0,0,1

# Define bins exactly as specified
bins = [160, 170, 180, 190, 200, 210, 220]

# Create figure
plt.figure(figsize=(8, 5), dpi=300)

# Plot histogram
plt.hist(data, bins=bins, edgecolor='black')

# Labels
plt.xlabel("Negotiation Latency (milliseconds)", fontsize=12, family='serif')
plt.ylabel("Frequency", fontsize=12, family='serif')

# Axis limits
plt.xlim(150, 250)
plt.ylim(0, 3)

# Gridlines (Y-axis only)
plt.grid(axis='y', linestyle='--', linewidth=0.5)

# Mean line
mean_val = 177
plt.axvline(mean_val, linestyle='--')
plt.text(mean_val + 1, 2.5, "Mean = 177 ms", rotation=0)

# Clean layout
plt.tight_layout()

# Save figure (IEEE preferred formats)
plt.savefig("figure4_latency_distribution.png", dpi=300)
plt.savefig("figure4_latency_distribution.pdf")  # Vector format

# Show plot
plt.show()
