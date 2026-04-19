import matplotlib.pyplot as plt
import numpy as np

# Mean transit time by number of scenarios (from Sheet 4)
scenario_count = [1, 2, 3, 4, 5, 6]
mean_transit_by_count = [38.1, 44.7, 48.7, 53.2, 58.9, 63.1]
std_dev_by_count = [9.2, 8.9, 7.5, 6.8, 5.2, 0.8]

fig, ax = plt.subplots(figsize=(10, 6))

# Line plot with error bars
ax.errorbar(scenario_count, mean_transit_by_count, yerr=std_dev_by_count, 
            fmt='o-', color='#1E40AF', linewidth=2, markersize=10, capsize=5,
            label='Mean Transit Time ± Std Dev')

# Add quadratic trend line
z = np.polyfit(scenario_count, mean_transit_by_count, 2)
p = np.poly1d(z)
x_trend = np.linspace(0.5, 6.5, 100)
ax.plot(x_trend, p(x_trend), 'r--', linewidth=1.5, label=f'Trend: y = {z[0]:.2f}x² + {z[1]:.2f}x + {z[2]:.2f}')

ax.set_xlabel('Number of Active Scenarios', fontsize=12, fontweight='bold')
ax.set_ylabel('Mean Transit Time (seconds)', fontsize=12, fontweight='bold')
ax.set_title('Figure 6: Performance Degradation with Increasing Scenario Complexity', fontsize=14, fontweight='bold')
ax.set_xticks([1, 2, 3, 4, 5, 6])
ax.grid(axis='both', linestyle='--', alpha=0.3)
ax.legend()

# Add value labels on points
for i, (x, y) in enumerate(zip(scenario_count, mean_transit_by_count)):
    ax.annotate(f'{y:.1f}s', (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

plt.tight_layout()
plt.savefig('figure6_performance_degradation.png', dpi=300, bbox_inches='tight')
plt.show()
print("✓ Figure 6 saved")
