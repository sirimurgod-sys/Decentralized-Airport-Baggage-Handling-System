import matplotlib.pyplot as plt

# Data
labels = ["Baseline (Centralized)", "Communication-Only", "Proposed (Distributed)"]
values = [0, 0, 100]

# Colors (flat, no gradients)
colors = ["lightgray", "#ADD8E6", "#003366"]  # light gray, light blue, dark blue

# Create figure
plt.figure(figsize=(8, 5), dpi=300)

# Plot bars
bars = plt.bar(labels, values, color=colors, edgecolor='black')

# Y-axis settings
plt.ylabel("Completion Rate (%)", fontsize=12, family='Arial')
plt.ylim(0, 100)

# Gridlines (Y-axis only)
plt.grid(axis='y', linestyle='--', linewidth=0.5)

# Value labels on top of bars
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, value + 2,
             f"{value}%", ha='center', fontsize=11)

# Horizontal dashed green line at 100%
plt.axhline(y=100, linestyle='--', linewidth=1)

# Title (note: for IEEE, better to move this as caption in paper)
plt.title("Figure 5: Fault Tolerance During Node Failure (S3)",
          fontsize=14, family='Arial')

# Clean layout
plt.tight_layout()

# Save outputs (IEEE preferred)
plt.savefig("figure5_fault_tolerance.png", dpi=300)
plt.savefig("figure5_fault_tolerance.pdf")  # vector format

# Show plot
plt.show()
