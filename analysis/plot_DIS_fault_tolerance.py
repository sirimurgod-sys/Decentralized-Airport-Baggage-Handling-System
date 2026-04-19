import matplotlib.pyplot as plt
import numpy as np

# Data from Sheet 15: With S3 vs Without S3
scenarios = ['S1 (Normal)', 'S2 (Congestion)', 'S4 (Priority Burst)', 'S5 (Peak Load)', 'S6 (Recovery)']
without_s3 = [27.8, 46.6, 38.9, 52.7, 34.4]
with_s3 = [27.3, 47.0, 38.0, 53.6, 34.1]

x = np.arange(len(scenarios))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
bars1 = ax.bar(x - width/2, without_s3, width, label='Without S3 (No Node Failure)', color='#93C5FD', edgecolor='black')
bars2 = ax.bar(x + width/2, with_s3, width, label='With S3 (Node Failure)', color='#1E40AF', edgecolor='black')

# Add value labels
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f'{bar.get_height():.1f}s', ha='center', fontsize=9)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, f'{bar.get_height():.1f}s', ha='center', fontsize=9)

ax.set_xlabel('Scenario', fontsize=12, fontweight='bold')
ax.set_ylabel('Mean Transit Time (seconds)', fontsize=12, fontweight='bold')
ax.set_title('Figure 7: Fault Tolerance Analysis - Node Failure Impact (315 Trials)', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(scenarios)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('figure7_fault_tolerance.png', dpi=300, bbox_inches='tight')
plt.show()
print("✓ Figure 7 saved")
