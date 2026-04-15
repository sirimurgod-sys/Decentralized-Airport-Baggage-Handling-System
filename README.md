# Decentralized-Airport-Baggage-Handling-System
This repository presents a distributed coordination framework for airport baggage handling systems using low-cost ESP32 nodes. Unlike centralized PLC-based systems that create single points of failure, it enables intelligent peer-to-peer negotiation among conveyors, diverters, RFID scanners, and carousel nodes.
📌 Overview
This repository presents the complete implementation and simulation framework for the IEEE conference paper:
“Decentralized Coordination of Embedded Nodes in Airport Baggage Handling Systems: A Distributed Negotiation Approach”
The project reimagines traditional airport baggage systems by eliminating centralized PLC control and enabling autonomous, peer-to-peer coordination among ESP32-based embedded nodes.
Instead of rigid control hierarchies, the system adopts a distributed negotiation protocol, allowing nodes (conveyors, diverters, RFID scanners, and carousels) to dynamically collaborate in real time.
🚀 Key Contributions
•	⚡ 35.4% reduction in baggage transit time under congestion 
•	🛡️ 100% fault tolerance during node failure scenarios 
•	⏱️ Sub-second negotiation latency (mean: 177 ms) 
•	🔁 Fully decentralized decision-making architecture (no single point of failure) 
________________________________________
🧠 System Architecture
The system consists of five cooperative embedded nodes:
Node ID	Component	Role
1	Conveyor A	Initial bag transport
2	Diverter	Decision-making and routing
3	Conveyor B	Secondary path (congestion-prone)
4	RFID Scanner	Priority detection
5	Carousel	Final destination & logging
Each node communicates using ESP-NOW protocol, enabling low-latency, connectionless communication.
________________________________________
📂 Repository Structure
├── sketch.ino              # Core ESP32 distributed protocol implementation
├── diagram.json            # Wokwi simulation configuration
├── data/
│   ├── trial_data.csv      # Raw results (45 trials)
│   └── analysis_results.xlsx
├── results/
│   └── figures/            # Graphs used in the paper
└── README.md               # Documentation
________________________________________
⚙️ Requirements
Tool	Version	Purpose
Arduino IDE	2.0+	Code development
ESP32 Board Package	3.0.0+	Board support
Wokwi Simulator	Latest	Online simulation
Python (optional)	3.11+	Statistical analysis
________________________________________
🛠️ Installation & Setup
1. Clone Repository
git clone https://github.com/yourusername/baggage-handling-distributed.git
cd baggage-handling-distributed
2. Configure Arduino IDE
•	Open Preferences 
•	Add: 
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
•	Install ESP32 via Boards Manager 
________________________________________
3. Libraries
No external libraries required:
•	esp_now.h 
•	WiFi.h 
________________________________________
🧪 Simulation Setup
🔹 Option A: Online Simulation (Recommended)
Use Wokwi ESP32 Simulator
Steps:
1.	Create 5 separate simulation instances 
2.	Upload sketch.ino to each 
3.	Assign node IDs: 
#define MY_NODE_ID X
Node	ID
Conveyor A	1
Diverter	2
Conveyor B	3
RFID	4
Carousel	5
4.	Run all simulations simultaneously 
5.	Open Node 5 Serial Monitor for results 
________________________________________
🔹 Option B: Physical Deployment
•	Flash code to 5 ESP32 boards 
•	Ensure same Wi-Fi channel 
•	Monitor outputs via serial 
________________________________________
🔄 Experimental Configurations
Configurations
Code	Mode	Description
0	Baseline	Centralized PLC
1	Communication-only	No negotiation
2	Proposed	Full distributed negotiation
________________________________________
Scenarios
Code	Scenario	Description
1	Normal Flow	No congestion
2	Congestion	Priority + bottleneck
3	Node Failure	Conveyor B failure
________________________________________
⚡ Core Protocol Parameters
#define VOTE_TIMEOUT           500
#define HEARTBEAT_INTERVAL     2000
#define NODE_FAILURE_TIMEOUT   5000
________________________________________
📡 Communication Model
Message Type	Purpose
PRIORITY_ALERT	RFID detects priority
STATUS	Congestion reporting
VOTE_REQUEST	Diverter initiates negotiation
VOTE_RESPONSE	Cost evaluation
ACTION	Final routing decision
COMPLETE	Delivery confirmation
HEARTBEAT	Node health monitoring
________________________________________
📊 Output Data Format
The system logs structured CSV data:
Field	Description
trial_id	Trial number
node_id	Node identifier
config	System configuration
scenario	Scenario type
transit_time_s	Time taken
latency_ms	Negotiation delay
message_bytes	Communication overhead
congestion	System load
queue	Queue length
________________________________________
📈 Results Summary
Scenario: Congestion (S2)
Configuration	Transit Time	Latency	Improvement
Baseline	44.02s	0 ms	—
Comm-only	37.86s	0 ms	13.9%
Proposed	28.46s	177 ms	35.4%
________________________________________
🔬 Statistical Significance
•	p-value < 0.001 → Highly significant 
•	Large effect sizes (Cohen’s d > 10) 
•	Strong validation of distributed approach 
________________________________________
🛡️ Fault Tolerance (S3)
Configuration	Completion Rate
Baseline	0%
Comm-only	0%
Proposed	100%
________________________________________
🔁 Automated Trial Execution
The system runs:
3 Configurations × 3 Scenarios × 5 Trials = 45 Trials
Execution is fully automated within the firmware.
________________________________________
🧮 Data Analysis (Python)
import pandas as pd
from scipy import stats

df = pd.read_csv('trial_data.csv')
s2 = df[df['scenario'] == 2]

baseline = s2[s2['config'] == 0]['transit_time_s']
proposed = s2[s2['config'] == 2]['transit_time_s']

t_stat, p_val = stats.ttest_ind(baseline, proposed)
print(p_val)
________________________________________
⚠️ Troubleshooting
ESP-NOW Issues
•	Ensure all nodes are active simultaneously 
Callback Error
•	Use updated ESP32 v3.0+ signature: 
void OnDataRecv(const esp_now_recv_info_t *info, const uint8_t *data, int len)
Missing Data
•	Only Node 5 logs final outputs 
________________________________________
📚 Citation
@inproceedings{yourname2026decentralized,
  title={Decentralized Coordination of Embedded Nodes in Airport Baggage Handling Systems},
  author={Your Name},
  booktitle={IEEE WIN-TECH Conference},
  year={2026}
}
________________________________________
📜 License
MIT License
________________________________________
👤 Author
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


