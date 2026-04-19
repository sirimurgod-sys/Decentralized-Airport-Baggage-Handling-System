import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# COMPLETE LATENCY DATA FROM 315 TRIALS
# ============================================================

latency_all = [
    194,185,173,183,199,227,205,229,237,226,231,208,207,214,220,
    175,167,160,168,158,195,159,181,165,162,251,249,224,212,240,
    230,241,221,247,230,204,185,187,227,186,213,189,209,216,219,
    257,241,233,250,250,215,237,241,232,255,228,196,183,180,183,
    211,182,211,179,225,258,254,255,246,230,252,232,229,225,244,
    239,256,260,254,225,226,241,216,252,248,266,272,271,245,252,
    273,264,247,278,243,226,225,255,238,265,229,238,255,258,252,
    267,231,249,272,247,249,266,261,267,270,272,246,268,260,271,
    264,273,259,242,271,246,254,244,276,285,265,245,255,266,282,
    255,235,253,225,243,228,272,260,243,239,245,249,266,272,285,
    272,244,244,268,268,181,209,201,182,168,195,190,195,211,180,
    231,232,229,248,215,219,256,235,209,229,170,183,179,202,197,
    203,201,181,207,179,241,211,245,211,230,238,245,248,215,226,
    223,200,212,216,220,226,227,233,185,205,233,258,219,217,230,
    256,253,251,248,248,196,209,185,222,233,203,232,214,209,223,
    252,220,258,245,238,238,245,237,256,218,231,251,255,231,232,
    231,251,261,250,240,264,276,240,261,269,258,242,262,271,251,
    225,256,243,271,234,242,244,239,257,269,246,258,252,251,252,
    282,265,277,284,266,246,265,275,255,269,249,249,265,278,279,
    280,253,283,285,238,268,282,263,261,259,249,240,249,273,254,
    280,263,262,279,265,282,265,255,237,267,262,261,253,258,277
]

# Verify length
print(f"Total latency values: {len(latency_all)}")  # Should be 315

# ============================================================
# CREATE HISTOGRAM
# ============================================================

fig, ax = plt.subplots(figsize=(10, 6))
n, bins, patches = ax.hist(latency_all, bins=20, color='#1E40AF', edgecolor='black', alpha=0.7)

# Add mean and median lines
mean_latency = np.mean(latency_all)
median_latency = np.median(latency_all)
ax.axvline(mean_latency, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_latency:.0f}ms')
ax.axvline(median_latency, color='green', linestyle='--', linewidth=2, label=f'Median = {median_latency:.0f}ms')

# Add 95th percentile
p95 = np.percentile(latency_all, 95)
ax.axvline(p95, color='orange', linestyle=':', linewidth=2, label=f'95th Percentile = {p95:.0f}ms')

ax.set_xlabel('Negotiation Latency (milliseconds)', fontsize=12, fontweight='bold')
ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax.set_title('Figure 5: Latency Distribution (315 Trials)', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.3)

# Add value labels on bars (optional)
for i, (rect, count) in enumerate(zip(patches, n)):
    if count > 0:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height + 0.5, str(int(count)), 
                ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('figure5_latency_distribution.png', dpi=300, bbox_inches='tight')
plt.show()
print("✓ Figure 5 saved: figure5_latency_distribution.png")

# Print statistics
print("\n=== Latency Statistics ===")
print(f"Mean: {mean_latency:.0f}ms")
print(f"Median: {median_latency:.0f}ms")
print(f"Std Dev: {np.std(latency_all):.0f}ms")
print(f"Min: {min(latency_all)}ms")
print(f"Max: {max(latency_all)}ms")
print(f"95th Percentile: {p95:.0f}ms")
