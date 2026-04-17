import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 11
plt.rcParams['figure.dpi'] = 300

# ============================================================
# DATA FOR 90 TRIALS
# ============================================================

# S2 - Congestion (5 trials each)
baseline_s2 = [61.0, 64.0, 63.0, 63.0, 64.0]
comm_s2 = [54.0, 56.0, 53.0, 55.0, 52.0]
proposed_s2 = [31.0, 29.0, 30.0, 31.0, 30.0]

# S4 - Priority Burst (5 trials each)
baseline_s4 = [44.0, 45.0, 47.0, 45.0, 46.0]
comm_s4 = [38.0, 43.0, 40.0, 39.0, 41.0]
proposed_s4 = [28.0, 29.0, 28.0, 26.0, 27.0]

# S5 - Peak Load (5 trials each)
baseline_s5 = [79.0, 75.0, 78.0, 73.0, 79.0]
comm_s5 = [65.0, 67.0, 71.0, 68.0, 66.0]
proposed_s5 = [47.0, 47.0, 41.0, 44.0, 45.0]

# Latency data (Proposed system - all scenarios)
latency_data = [173, 169, 170, 171, 168,  # S1
                202, 172, 194, 165, 177,  # S2
                163, 186, 167, 192, 209,  # S3
                197, 202, 218, 193, 219,  # S4
                180, 172, 183, 210, 163,  # S5
                214, 201, 206, 197, 190]  # S6

# ============================================================
# FIGURE 1: Transit Time Box Plot - S2 Congestion
# ============================================================
fig, ax = plt.subplots(figsize=(6, 5))
bp = ax.boxplot([baseline_s2, comm_s2, proposed_s2],
                labels=['Baseline', 'Comm-only', 'Proposed'],
                patch_artist=True)
colors = ['#9CA3AF', '#93C5FD', '#1E40AF']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax.set_ylabel('Transit Time (seconds)')
ax.set_title('90 Trials: Transit Time - Congestion (S2)')
ax.set_ylim(20, 70)
ax.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('90trials_figure1_s2_boxplot.png', dpi=300)
plt.show()

# ============================================================
# FIGURE 2: Transit Time Box Plot - S4 Priority Burst
# ============================================================
fig, ax = plt.subplots(figsize=(6, 5))
bp = ax.boxplot([baseline_s4, comm_s4, proposed_s4],
                labels=['Baseline', 'Comm-only', 'Proposed'],
                patch_artist=True)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax.set_ylabel('Transit Time (seconds)')
ax.set_title('90 Trials: Transit Time - Priority Burst (S4)')
ax.set_ylim(20, 55)
ax.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('90trials_figure2_s4_boxplot.png', dpi=300)
plt.show()

# ============================================================
# FIGURE 3: Transit Time Box Plot - S5 Peak Load
# ============================================================
fig, ax = plt.subplots(figsize=(6, 5))
bp = ax.boxplot([baseline_s5, comm_s5, proposed_s5],
                labels=['Baseline', 'Comm-only', 'Proposed'],
                patch_artist=True)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax.set_ylabel('Transit Time (seconds)')
ax.set_title('90 Trials: Transit Time - Peak Load (S5)')
ax.set_ylim(35, 85)
ax.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('90trials_figure3_s5_boxplot.png', dpi=300)
plt.show()

# ============================================================
# FIGURE 4: Latency Histogram (All 90 trials - Proposed)
# ============================================================
fig, ax = plt.subplots(figsize=(6, 4))
n, bins, patches = ax.hist(latency_data, bins=8, color='#1E40AF', edgecolor='black', alpha=0.7)
mean_latency = np.mean(latency_data)
ax.axvline(mean_latency, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_latency:.0f}ms')
ax.set_xlabel('Negotiation Latency (ms)')
ax.set_ylabel('Frequency')
ax.set_title('90 Trials: Latency Distribution (Proposed System)')
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('90trials_figure4_latency_histogram.png', dpi=300)
plt.show()

# ============================================================
# FIGURE 5: Fault Tolerance Bar Chart
# ============================================================
configs = ['Baseline', 'Comm-only', 'Proposed']
completion = [0, 0, 100]
fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(configs, completion, color=['#9CA3AF', '#93C5FD', '#1E40AF'], edgecolor='black')
for bar, val in zip(bars, completion):
    ax.text(bar.get_x() + bar.get_width()/2, val + 2, f'{val}%', ha='center', fontsize=12, fontweight='bold')
ax.set_ylabel('Completion Rate (%)')
ax.set_title('90 Trials: Fault Tolerance - Node Failure (S3)')
ax.set_ylim(0, 110)
ax.axhline(100, color='green', linestyle='--', alpha=0.5)
ax.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('90trials_figure5_fault_tolerance.png', dpi=300)
plt.show()

# ============================================================
# FIGURE 6: Message Overhead Bar Chart
# ============================================================
configs = ['Baseline', 'Comm-only', 'Proposed']
bytes_data = [98, 156, 342]
fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(configs, bytes_data, color=['#9CA3AF', '#93C5FD', '#1E40AF'], edgecolor='black')
for bar, val in zip(bars, bytes_data):
    ax.text(bar.get_x() + bar.get_width()/2, val + 10, f'{val} B', ha='center', fontsize=12, fontweight='bold')
ax.set_ylabel('Message Bytes per Trial')
ax.set_title('90 Trials: Message Overhead Comparison')
ax.set_ylim(0, 400)
ax.axhline(520, color='green', linestyle='--', alpha=0.5, label='ESP32 RAM Limit (520KB)')
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('90trials_figure6_message_overhead.png', dpi=300)
plt.show()

# ============================================================
# FIGURE 7: Improvement Comparison Bar Chart
# ============================================================
scenarios = ['S2 (Congestion)', 'S4 (Priority)', 'S5 (Peak Load)']
improvements = [52.1, 39.2, 41.7]
fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(scenarios, improvements, color='#1E40AF', edgecolor='black')
for bar, val in zip(bars, improvements):
    ax.text(bar.get_x() + bar.get_width()/2, val + 1, f'{val}%', ha='center', fontsize=12, fontweight='bold')
ax.set_ylabel('Improvement (%)')
ax.set_title('90 Trials: Proposed vs Baseline Improvement')
ax.set_ylim(0, 60)
ax.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('90trials_figure7_improvement.png', dpi=300)
plt.show()

print("All 7 figures saved for 90 trials!")
