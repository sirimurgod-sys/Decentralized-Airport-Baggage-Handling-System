import matplotlib.pyplot as plt

# Data
labels = ["Baseline (Centralized)", "Communication-Only", "Proposed (Distributed)"]
values = [0, 0, 100]

# Colors
colors = ["lightgray", "#ADD8E6", "#003366"]

# Create figure
plt.figure(figsize=(8, 5), dpi=300)

# Plot bars
bars = plt.bar(labels, values, color=colors, edgecolor='black')

# Y-axis settings
plt.ylabel("Completion Rate (%)")
plt.ylim(0, 100)

# Gridlines (Y-axis only)
plt.grid(axis='y', linestyle='--', linewidth=0.5)

# Value labels
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, value + 2,
             f"{value}%", ha='center')

# Dashed line at 100%
plt.axhline(y=100, linestyle='--', linewidth=1)

# Title (optional for preview)
plt.title("Figure 5: Fault Tolerance During Node Failure (S3)")

# Layout
plt.tight_layout()

# Save files
plt.savefig("figure5_fault_tolerance.png", dpi=300)
plt.savefig("figure5_fault_tolerance.pdf")

# Show
plt.show()
