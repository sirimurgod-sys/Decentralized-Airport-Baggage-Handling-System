import matplotlib.pyplot as plt

# Data
labels = ["Baseline (Centralized)", "Communication-Only", "Proposed (Distributed)"]
values = [98, 156, 342]

# Colors
colors = ["lightgray", "#ADD8E6", "#003366"]

# Create figure
plt.figure(figsize=(8, 5), dpi=300)

# Plot bars
bars = plt.bar(labels, values, color=colors, edgecolor='black')

# Y-axis settings
plt.ylabel("Message Bytes per Trial")
plt.ylim(0, 400)

# Gridlines (Y-axis only)
plt.grid(axis='y', linestyle='--', linewidth=0.5)

# Value labels on bars
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, value + 8,
             f"{value} B", ha='center')

# Percentage increase labels
plt.text(bars[1].get_x() + bars[1].get_width()/2, values[1] + 30,
         "+59%", ha='center')
plt.text(bars[2].get_x() + bars[2].get_width()/2, values[2] + 30,
         "+249%", ha='center')

# Horizontal dashed line (ESP32 RAM limit)
plt.axhline(y=520, linestyle='--', linewidth=1)
plt.text(1, 380, "ESP32 RAM Limit (520KB)", ha='center')

# Title (optional for preview)
plt.title("Figure 6: Message Overhead Comparison")

# Layout
plt.tight_layout()

# Save files
plt.savefig("figure6_message_overhead.png", dpi=300)
plt.savefig("figure6_message_overhead.pdf")

# Show
plt.show()
