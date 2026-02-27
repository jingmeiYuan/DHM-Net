# [HA-Net]
The code of "Bridging Local and Global Contexts: A Hierarchical Attention Network for Robust Visual Inspection in Industrial Environments" from The Visual Computer.
![Framework Overview](https://github.com/jingmeiYuan/HA-Net/blob/53dab4fd908d7a0e12be7e9001c7773dd6dc7ddc/Framework%20Overview.png)  
![Framework Overview]([(https://github.com/jingmeiYuan/HA-Net/blob/53dab4fd908d7a0e12be7e9001c7773dd6dc7ddc/Framework%20Overview.png)])  
*Figure: Overview of the [HA-Net] framework [A Hierarchical Attention Network for Robust Visual Inspection in Industrial Environments].*

**[HA-Net]** is a[HA-Net is a hierarchical attention network for robust visual inspection in industrial environments]
[![GitHub Stars]((https://github.com/jingmeiYuan/HA-Net.git))]

---

## ✨ Key Features

- **[A dual-backbone feature extraction network]**  
  [Through the dual-backbone network design, the feature representation capability is effectively improved by preserving fine-grained textures and enhancing semantic capture capabilities]。

- **[A Hierarchical Dual Attention Fusion (HDAF) module]**  
  [This module incorporates a dual-path attention mechanism that fuses local and global information. Combined with RepConv, it effectively eliminates the semantic gap and spatial alignment bias among multi-source heterogeneous features while reducing the number of parameters, thereby achieving deep fusion and refined reorganization of features from different backbone networks.]。

- **[A Multi-scale Feature Information Selection (MFIS) module]**  
  [By introducing a Spatial-Frequency Selection Mechanism (SFSM), this module adaptively selects signals highly relevant to defects. It effectively suppresses noise interference arising from large variations in defect scale and complex industrial backgrounds, by enriching the extracted feature representation, the modeling of detailed information is optimized.]。


---



## 📥 Installation

### Prerequisites
- Python ≥ [3.8]
- PyTorch ≥ [2.0.0]
- CUDA ≥ [12.1]


### Steps
1. Clone the repository:
   ```bash
   git clone [https://github.com/jingmeiYuan/HA-Net].git
   cd [HA-Net]
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Download pre-trained models
   ```bash
   wget https://github.com/jingmeiYuan/HA-Net.git/releases/download/



---
   ##  Citation
If you find this work useful in your research, please consider citing our paper:

@article{wu2026dual,  
  title={Bridging Local and Global Contexts: A Hierarchical Attention Network for Robust Visual Inspection in Industrial Environments},  
  author={Jingmei Yuan,Ang Li and Xiushuang Yang,  
  journal={The Visual Computer},  
  year={2026},  
  publisher={Springer},  
}  

---
 ##  Contact
 If you have any questions about our work or code, please email 35555147@qq.com .
