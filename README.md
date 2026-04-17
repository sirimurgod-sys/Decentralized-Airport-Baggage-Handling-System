# Decentralized Coordination of Embedded Nodes in Airport Baggage Handling Systems

## Overview

This repository presents the simulation framework, experimental datasets, and analysis for the IEEE conference paper:

**“Decentralized Coordination of Embedded Nodes in Airport Baggage Handling Systems: A Distributed Negotiation Approach.”**

The work proposes a **fully distributed coordination protocol** in which ESP32-based embedded nodes—representing conveyor belts, diverters, RFID scanners, and carousels—negotiate decisions autonomously, eliminating reliance on a centralized PLC.
This work addresses the critical lack of standardized interaction mechanisms among multi-vendor embedded systems in airport environments, enabling heterogeneous nodes from different manufacturers to seamlessly coordinate without proprietary protocols or centralized controllers.
---

## Key Contributions

* **Decentralized decision-making** using distributed voting and negotiation
* **Real-time coordination** under congestion, failure, and peak load
* **Fault-tolerant routing** with dynamic recovery
* **Low-overhead communication** using ESP-NOW protocol
* **Statistically validated performance gains**

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

## Repository Structure

```
├── sketch.ino
├── diagram.json
├── README.md
├── data/
│   ├── 45_trials/
│   └── 90_trials/
├── figures/
│   ├── 45_trials/
│   └── 90_trials/
└── results/
```

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

* **45 Trials:**
  3 Configurations × 3 Scenarios × 5 Trials

* **90 Trials:**
  3 Configurations × 6 Scenarios × 5 Trials

> Note: Representative subsets are visualized in figures, while aggregate metrics are computed over all trials.

---

## Key Findings

### Performance Gains

* Up to **52.1% reduction in transit time** under congestion
* Significant improvements under peak and priority conditions
* Large effect sizes indicating strong practical impact

### Real-Time Feasibility

* Mean latency: **187 ms**
* Worst-case latency: **< 220 ms**
* Suitable for real-time embedded control systems

### Fault Tolerance

* **100% completion rate** under node failure
* Autonomous rerouting without central intervention

### Communication Efficiency

* **342 bytes per trial**
* <0.1% of ESP32 RAM usage

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

   * 1: Conveyor A
   * 2: Diverter
   * 3: Conveyor B
   * 4: RFID
   * 5: Carousel
3. Run all simultaneously
4. Monitor Node 5 for CSV output

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

---
#Authors

•	Saubalini Gopalakrishnan Vaneeswari 
•	Department of Electronics & Communication Engineering 
•	Visvesvaraya Technological University
•	Email: 1bi25ec133@bit-bangalore.edu.in

•	Siri M
•	Department of Electronics & Communication Engineering 
•	Visvesvaraya Technological University
•	Email: 1bi25ec148@bit-bangalore.edu.in
________________________________________
🙏 Acknowledgments

•	IEEE for research platform 

•	Espressif Systems for ESP32 & ESP-NOW

•	Wokwi for simulation support


