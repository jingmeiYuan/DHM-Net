# DHM-Net: A Lightweight Dual-Backbone Network with Hierarchical Attention for Real-Time Industrial Surface Defect Detection

This repository contains the official implementation of **DHM-Net**, a lightweight dual-backbone network with hierarchical attention for real-time industrial surface defect detection.

![Framework Overview](Framework%20Overview.png)
*Figure: Overview of the DHM-Net framework.*

---


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

## 📊 Datasets

In this study, we utilize the following publicly available datasets for [Defect detection] ；

- **NEU-DET**  
  [Official Website](https://drive.google.com/file/d/1qrdZlaDi272eA79b0uCwwqPrm2Q_WI3k/view?pli=1)

- **GC10-DET**  
  [Download Link](https://pan.baidu.com/s/1Zrd-gzfVhG6oKdVSa9zoPQ) Verify Code：cdyt

👉 **Dataset Usage**: NEU-DET and GC10-DET are used for defect detection.

### 📋 Dataset Preparation
After downloading, organize the datasets as follows:  
#### Dataset Structure
```bash
├── datasets/  
   ├── images/ 
       ├── train/ 
       ├── val/   
   ├── labels/ 
       ├── train/ 
       ├── val/
```
## 🚀 Training and val

We provide scripts for both  defect detection tasks.

### Industrial Defect Detection
- **Training**:
  ```bash
  python train.py

- **Val**:
  ```bash
  python val.py

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

@article{yuan2026bridging,
  title={Bridging Local and Global Contexts: A Hierarchical Attention Network for Robust Visual Inspection in Industrial Environments},
  author={Yuan, Jingmei and Li, Ang and Yang, Xiushuang},
  journal={The Visual Computer},
  year={2026},
  publisher={Springer}
}  

---
 ##  Contact
 If you have any questions about our work or code, please email 35555147@qq.com .
