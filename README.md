# Intelligent Congestion Prediction and Control in Data Center Networks Using SDN and Deep Learning

[![Conference](https://img.shields.io/badge/Conference-ICon_INDIA_2026-blue.svg)](https://iconindia2026.aconf.org/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-green.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange.svg)](https://pytorch.org/)
[![SDN](https://img.shields.io/badge/Network-OpenFlow_SDN-green.svg)](https://openflow.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Accepted for presentation at the **International Conference on Intelligent Networks and Data-driven Intelligent Applications (ICon INDIA 2026)**.

---

## 👥 Authors
- **Vibhas Reddy A** ([@VIBHAS777](https://github.com/VIBHAS777))
- **Pavan Kumar S**
- **Hima Sagar B**

---

## 🌐 Overview
Modern cloud data centers running distributed computing workloads (e.g., MapReduce, ML distributed training) frequently encounter catastrophic **TCP Incast** congestion. Standard congestion mitigation strategies (RED, ECN, standard ECMP) react only after packet queue thresholds have already been exceeded, triggering packet loss, retransmission storms, and tail latency inflation.

This project couples an **LSTM recurrent neural network** with a centralized **Software-Defined Networking (SDN)** controller. By forecasting switch port buffer saturation 50–100 ms in advance, the controller proactively modifies OpenFlow forwarding rules and deflects elephant flows onto underutilized spine paths before packet drops occur.

---

## 📁 Repository Structure
```
sdn-congestion-control-deeplearning/
├── paper/
│   ├── Intelligent_Congestion_Prediction_and_Control_in_Data_Center_Networks.pdf
│   └── Acceptance_Email_ICon_INDIA_2026.pdf
├── src/
│   ├── dl_predictor.py    # Time-series LSTM buffer occupancy predictor
│   └── sdn_controller.py  # Proactive OpenFlow flow installation & rerouting engine
├── main.py                # Incast burst simulation & proactive reroute demo
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Quick Start
```bash
git clone https://github.com/VIBHAS777/sdn-congestion-control-deeplearning.git
cd sdn-congestion-control-deeplearning
pip install -r requirements.txt
python main.py
```

---

## 📜 Citation
```bibtex
@inproceedings{reddy2026sdncongestion,
  title={Intelligent Congestion Prediction and Control in Data Center Networks Using SDN and Deep Learning},
  author={Reddy A, Vibhas and Kumar S, Pavan and Sagar B, Hima},
  booktitle={International Conference on Intelligent Networks and Data-driven Intelligent Applications (ICon INDIA)},
  year={2026}
}
```
