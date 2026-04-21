# Decentralized Coordination of Embedded Nodes in Airport Baggage Handling Systems

## Overview

This repository presents the simulation framework, experimental datasets, and analysis for the IEEE conference paper:

**“Decentralized Coordination of Embedded Nodes in Airport Baggage Handling Systems: A Distributed Negotiation Approach.”**

The work proposes a **fully distributed coordination protocol** in which ESP32-based embedded nodes—representing conveyor belts, diverters, RFID scanners, and carousels—negotiate decisions autonomously, eliminating reliance on a centralized PLC.
This work addresses the critical lack of standardized interaction mechanisms among multi-vendor embedded systems in airport environments, enabling heterogeneous nodes from different manufacturers to seamlessly coordinate without proprietary protocols or centralized controllers.
---

## Key Contributions

- **Decentralized decision-making** using distributed voting and negotiation
- **Real-time coordination** under congestion, failure, and peak load
- **Fault-tolerant routing** with dynamic recovery
- **Low-overhead communication** using ESP-NOW protocol
- **Statistically validated performance gains**

---

## Key Results

| Metric                    | 45 Trials | 90 Trials | Change   |
| ------------------------- | --------- | --------- | -------- |
| S2 Congestion Improvement | 35.4%     | **52.1%** | ↑ +16.7% |
| S4 Priority Burst         | —         | **39.2%** | New      |
| S5 Peak Load              | —         | **41.7%** | New      |
| Fault Tolerance           | 0% → 100% | 0% → 100% | —        |
| Mean Latency              | 177 ms    | 187 ms    | +10 ms   |
| Message Overhead          | 342 B     | 342 B     | —        |

---

## 📁 Project Structure

### Root Files
- 'sketch.ino' — Main ESP32 simulation code
- 'diagram.json' — System architecture / simulation diagram
- 'README.md' — Project documentation
  
### 📊 Data (Raw Experimental Datasets)
- 'data/45_trials/'
- 'data/90_trials/'
- 'data/315_trials/'
  
### 📈 Figures (Generated Visualizations)
- 'figures/45_trials/'
- 'figures/90_trials/'
- 'figures/315_trials/'
  
### 📉 Results (Processed Outputs & Analysis)
- 'results/45_trials/'
- 'results/90_trials/'
- 'results/315_trials/'

---

## System Configurations

| Code | Configuration      | Description                          |
| ---- | ------------------ | ------------------------------------ |
| 0    | Baseline           | Centralized PLC control              |
| 1    | Communication-only | Message exchange without negotiation |
| 2    | Proposed           | Distributed negotiation protocol     |

---

## Experimental Scenarios (90 Trials)

| Code | Scenario       | Description                |
| ---- | -------------- | -------------------------- |
| S1   | Normal Flow    | Standard operation         |
| S2   | Congestion     | High load on Conveyor B    |
| S3   | Node Failure   | Conveyor B failure         |
| S4   | Priority Burst | Consecutive priority bags  |
| S5   | Peak Load      | Maximum throughput         |
| S6   | Recovery       | Post-failure stabilization |

---

## Trial Design

- **45 Trials:**
  3 Configurations × 3 Scenarios × 5 Trials

- **90 Trials:**
  3 Configurations × 6 Scenarios × 5 Trials

> Representative subsets are visualized in figures, while aggregate metrics are computed over all trials.

---

## Key Findings

### Performance Gains

- Up to **52.1% reduction in transit time** under congestion
- Significant improvements under peak and priority conditions
- Large effect sizes indicating strong practical impact

### Real-Time Feasibility

- Mean latency: **187 ms**
- Worst-case latency: **< 220 ms**
- Suitable for real-time embedded control systems

### Fault Tolerance

- **100% completion rate** under node failure
- Autonomous rerouting without central intervention

### Communication Efficiency

- **342 bytes per trial**
- <0.1% of ESP32 RAM usage

---

## Installation

```bash
git clone https://github.com/yourusername/baggage-handling-distributed.git
cd baggage-handling-distributed
```

### Arduino Setup

* Install ESP32 board package
* Required libraries:

  * `esp_now.h`
  * `WiFi.h`

---

## Simulation (Wokwi)

### Steps:

1. Create 5 ESP32 instances
2. Assign node IDs:

   - '1' : Conveyor A
   - '2' : Diverter
   - '3' : Conveyor B
   - '4' : RFID
   - '5' : Carousel
3. Run all simultaneously
4. Monitor **Node 5** for CSV output

---

## Output Format

| Field          | Description            |
| -------------- | ---------------------- |
| trial_id       | Trial number           |
| config         | System configuration   |
| scenario       | Scenario ID            |
| transit_time_s | Transit time           |
| latency_ms     | Negotiation latency    |
| message_bytes  | Communication overhead |

---

## Reproducibility

To reproduce results:

1. Run all simulations
2. Collect Node 5 output
3. Save as CSV
4. Execute statistical script

---

## 📊 Extended Evaluation: 315 Trials Across 63 Scenario Combinations

### 🔍 Overview
To validate system robustness, we conducted a comprehensive evaluation covering **all 63 possible combinations** of six scenarios (S1–S6).  
Each configuration was tested over **5 trials**, resulting in a total of **315 experimental runs**.

---

### 🧩 Scenario Coverage

| Combination Type | Count |
|------------------|-------|
| Single scenario  | 6     |
| Two scenarios    | 15    |
| Three scenarios  | 20    |
| Four scenarios   | 15    |
| Five scenarios   | 6     |
| All scenarios    | 1     |
| **Total**        | **63 combinations (315 trials)** |

---

### ⚡ Key Performance Metrics

- **Best Transit Time:** 26.7 s (S1 only)  
- **Worst Transit Time:** 64.7 s (S2 + S4 + S5 + S6)  
- **Average Transit Time:** 48.2 s  
- **Mean Negotiation Latency:** 238 ms  
- **95th Percentile Latency:** 285 ms  
- **Completion Rate:** **100% (315/315 trials)**  

---

### 📈 Performance vs Complexity

| Active Scenarios | Mean Transit Time |
|------------------|-------------------|
| 1 | 38.1 s |
| 2 | 44.7 s |
| 3 | 48.7 s |
| 4 | 53.2 s |
| 5 | 58.9 s |
| 6 | 63.1 s |

> Performance shows a gradual and predictable increase in transit time as system complexity rises.

---

### 🛡️ Fault Tolerance

- Node failure scenario (S3) had **no statistically significant impact on performance**  
- Indicates strong **system resilience under failure conditions**

---

### 📊 Statistical Validation

- **1 vs 6 Scenarios:** t = 47.0, p < 0.001  
- **Best vs Worst Case:** t = 42.6, p < 0.001  
- **ANOVA:** F(5,60) = 156.3, p < 0.001  

> Results confirm statistically significant performance variation with complexity.

---

### 🖼️ Generated Figures

- `figure1_transit_by_complexity.png` — Performance vs complexity   
- `figure2_latency_distribution.png` — Latency distribution  
- `figure3_fault_tolerance.png` — Node failure impact  
- `figure4_best_vs_worst.png` — Extreme case comparison  

---

### ✅ Conclusion

The system achieved **100% successful execution across all 315 trials**, demonstrating:

- Robust performance under all scenario combinations  
- Graceful degradation with increasing complexity  
- Strong fault tolerance with zero failure cases  

**Overall, the results validate the system as highly reliable and scalable under diverse operating conditions.**

## Citation

```bibtex
@inproceedings{saubalini2026decentralized,
  title={Decentralized Coordination of Embedded Nodes in Airport Baggage Handling Systems},
  author={Saubalini Gopalakrishnan Vaneeswari and Siri M},
  booktitle={IEEE WIN-TECH Conference},
  year={2026}
}
---

## License

MIT License
---

## Version History

| Version | Date       | Changes                  |
| ------- | ---------- | ------------------------ |
| 1.0     | April 2026 | Initial 45-trial release |
| 2.0     | April 2026 | Extended to 90 trials    |

__________________________________________________________
## Authors

###	Saubalini Gopalakrishnan Vaneeswari 
-	1st year, Department of Electronics & Communication Engineering 
-	Bangalore Institute of Technology, Visvesvaraya Technological University
-	Email: 1bi25ec133@bit-bangalore.edu.in

###	Siri M
-	1st year, Department of Electronics & Communication Engineering 
-	Bangalore Institute of Technology, Visvesvaraya Technological University
-	Email: 1bi25ec148@bit-bangalore.edu.in
___________________________________________________________
##🙏 Acknowledgments

-	IEEE for research platform 

-	Espressif Systems for ESP32 & ESP-NOW

-	Wokwi for simulation support


