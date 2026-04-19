import matplotlib.pyplot as plt
import numpy as np

# Data: Transit time for each complexity group (1 to 6 scenarios)
# Based on Sheet 4 from your analysis

data_by_complexity = {
    1: [27.8, 27.9, 27.3, 38.9, 52.7, 34.4],  # 6 values (S1,S3,S4,S5,S6,S2? actually S2 is 46.6)
    # Corrected: Let me use the actual means from your 315 trials
}

# More accurately, let me create box plot data from your raw 315 trials
# Group 1: 1 scenario (Combinations: 1,2,4,8,16,32)
group1 = [26.7,27.5,27.7,28.1,29.0,  # S1 only
          46.0,45.5,47.7,48.0,45.7,  # S2 only
          27.6,28.3,26.7,28.9,27.8,  # S3 only
          39.6,38.8,38.4,39.2,38.5,  # S4 only
          52.7,52.2,53.3,53.5,51.7,  # S5 only
          34.5,35.3,35.4,32.6,34.1]  # S6 only

# Group 2: 2 scenarios (Combinations with 2 active scenarios)
group2 = [48.0,48.0,46.2,47.2,47.8,  # S1+S2
          26.7,26.8,27.4,28.3,27.1,  # S1+S3
          48.2,47.3,46.0,47.3,46.2,  # S2+S3
          37.9,38.2,39.8,39.2,39.8,  # S1+S4
          50.5,51.5,51.0,52.0,50.0,  # S2+S4
          39.9,37.2,38.0,37.1,38.0,  # S3+S4
          53.8,53.7,52.0,52.7,52.3,  # S1+S5
          60.2,59.7,60.0,59.5,61.0,  # S2+S5
          53.5,53.8,54.0,52.7,54.0,  # S3+S5
          58.5,58.0,56.7,58.5,56.2,  # S4+S5
          34.5,33.2,32.8,32.6,33.4,  # S1+S6
          50.7,49.3,48.5,50.5,50.7,  # S2+S6
          34.0,35.2,32.8,33.0,35.4,  # S3+S6
          42.0,41.2,41.7,40.5,42.4,  # S4+S6
          54.8,56.8,55.3,56.0,55.7]  # S5+S6

# Group 3: 3 scenarios (20 combinations × 5 trials = 100 values)
# Group 4: 4 scenarios (15 combinations × 5 trials = 75 values)
# Group 5: 5 scenarios (6 combinations × 5 trials = 30 values)
# Group 6: 6 scenarios (1 combination × 5 trials = 5 values)

# For simplicity, use the mean values from Sheet 4
group1_mean = [27.8, 46.6, 27.9, 38.9, 52.7, 34.4]
group2_mean = [47.4, 27.3, 47.0, 38.9, 51.0, 38.0, 52.9, 60.1, 53.6, 57.6, 33.3, 49.9, 34.1, 41.6, 55.7]
group3_mean = [46.6, 51.1, 38.1, 51.1, 51.6, 60.3, 52.7, 61.1, 59.7, 56.9, 63.0, 56.8, 57.6, 62.7, 63.4, 49.3, 49.8, 41.3, 55.1, 53.7]
group4_mean = [41.5, 41.4, 54.2, 53.9, 55.7, 55.3, 62.9, 63.2, 55.9, 56.1, 62.9, 63.6, 60.2, 60.6, 63.6]
group5_mean = [63.5, 63.6, 60.9, 62.8, 63.1, 63.6]
group6_mean = [63.3, 62.7, 63.2, 64.2, 62.0]

fig, ax = plt.subplots(figsize=(10, 6))

# Create box plot
box_data = [group1_mean, group2_mean, group3_mean, group4_mean, group5_mean, group6_mean]
bp = ax.boxplot(box_data, labels=['1', '2', '3', '4', '5', '6'], patch_artist=True)

# Set colors
colors = ['#9CA3AF', '#93C5FD', '#60A5FA', '#3B82F6', '#2563EB', '#1E40AF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_xlabel('Number of Active Scenarios', fontsize=12, fontweight='bold')
ax.set_ylabel('Transit Time (seconds)', fontsize=12, fontweight='bold')
ax.set_title('Figure 1: Transit Time vs Number of Active Scenarios (315 Trials)', fontsize=14, fontweight='bold')
ax.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('figure1_transit_time_by_complexity.png', dpi=300, bbox_inches='tight')
plt.show()
print("✓ Figure 1 saved")
