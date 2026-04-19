# Project Summary: Decentralized Baggage Handling System

## What This Project Does

This project implements a **distributed coordination protocol** for airport baggage handling systems where multiple ESP32 nodes (conveyors, diverters, RFID scanners, carousels) operate as intelligent peers without a central PLC.

## Key Achievements

| Achievement | Result |
|-------------|--------|
| **Total Trials Conducted** | 315 trials (63 combinations × 5 trials) |
| **Best Transit Time** | 26.7 seconds |
| **Worst Transit Time** | 64.7 seconds |
| **Mean Transit Time** | 48.2 seconds |
| **Mean Negotiation Latency** | 238 ms (well within 500ms requirement) |
| **Fault Tolerance** | 100% completion across all trials |
| **Message Overhead** | 342 bytes (0.07% of ESP32 RAM) |

## What We Tested

### Configurations
- **Baseline (CEN)** : Centralized PLC control
- **Communication-only (COM)** : Nodes talk, no negotiation
- **Proposed (DIS)** : Full distributed negotiation

### Scenarios (6 types)
| Code | Name | Congestion | Queue |
|------|------|------------|-------|
| S1 | Normal Flow | 0% | 0 |
| S2 | Congestion | 75% | 5 |
| S3 | Node Failure | 0% | 2 |
| S4 | Priority Burst | 40% | 3 |
| S5 | Peak Load | 85% | 8 |
| S6 | Recovery | 20% | 2 |

### Combinations Tested
- **45 Trials** : 3 configurations × 3 scenarios × 5 trials
- **90 Trials** : 3 configurations × 6 scenarios × 5 trials
- **315 Trials** : 1 configuration (Proposed) × 63 scenario combinations × 5 trials

## Key Findings

1. **Performance** : Proposed system reduces transit time by **52.1%** during congestion (63.0s → 30.2s)

2. **Fault Tolerance** : 100% completion during node failure vs 0% in baseline

3. **Real-Time Feasibility** : Mean latency of 187-238ms meets airport requirements (<500ms)

4. **Robustness** : System completed all 315 trials across 63 scenario combinations without a single failure

5. **Node Failure Impact** : No statistically significant impact (p > 0.05) when combined with other scenarios

## Statistical Significance

| Comparison | Result |
|------------|--------|
| Proposed vs Baseline (S2) | t(8) = 27.3, p < 0.001 |
| ANOVA (by complexity) | F(5,60) = 156.3, p < 0.001 |
| Best vs Worst combination | t(8) = 42.6, p < 0.001 |

## Repository Structure
