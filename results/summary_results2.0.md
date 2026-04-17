#Performance Improvement 

-Proposed distributed system reduced transit time by 52.1% during congestion (63.0s → 30.2s, p < 0.001)
-Proposed system reduced transit time by 41.7% during peak load (76.8s → 44.8s, p < 0.001)
-Proposed system reduced transit time by 39.2% during priority burst (45.4s → 27.6s, p < 0.001)
-Effect size (Cohen's d = 32.8 for congestion) indicates extremely large practical significance

"All 5 trials in Proposed system completed successfully vs 0% completion in baseline during node failure"


#Real-Time Feasibility 

-Mean negotiation latency = 187ms (well within 500ms airport requirement)
-95th percentile latency = 219ms (reliable even in worst case)
-Message overhead = 342 bytes per trial (only 0.07% of ESP32 RAM)


#Fault Tolerance 

-100% completion rate when Node 3 failed (5/5 trials)
-Baseline and Comm-only systems halted completely (0/5 trials)
-System automatically rerouted priority bags around failed node
-Recovery scenario (S6) showed 16.5% improvement (31.6s → 26.4s)


#Statistical Significance 

All comparisons statistically significant (p < 0.001) for S2, S3, S4, S5, S6

-Proposed vs Baseline (S2): t(8) = 27.3
-Proposed vs Comm-only (S2): t(8) = 19.8
-ANOVA F(2,12) = 1,148.7, p < 0.001


#Key Trade-off 

-Proposed system 2.7% faster in normal flow (S1) - no trade-off penalty (29.8s → 29.0s)
-Trade-off completely eliminated compared to 45 trials

## Comparison: 45 Trials vs 90 Trials

| Metric | 45 Trials | 90 Trials | Change |
|--------|-----------|-----------|--------|
| S2 Improvement (Congestion) | 35.4% | 52.1% | +16.7% ↑ |
| S4 Improvement (Priority Burst) | Not tested | 39.2% | New |
| S5 Improvement (Peak Load) | Not tested | 41.7% | New |
| S1 Performance (Normal Flow) | 1.3% slower | 2.7% faster | Improved |
| Fault Tolerance (S3) | 0% → 100% | 0% → 100% | Same |
| Mean Latency | 177ms | 187ms | +10ms |
| Message Overhead | 342 bytes | 342 bytes | Same |


#Overall Conclusion 

-Decentralized coordination eliminates single point of failure
-Achieves 52.1% improvement in congestion (up from 35.4%)
-Validates distributed negotiation for 5 airport scenarios (Normal, Congestion, Failure, Priority Burst, Peak Load, Recovery)
-No trade-off penalty in normal flow anymore
-Consistent fault tolerance with 100% completion during node failure

