# UreterStoneYOLO

Python implementation for automated detection of ureteral stones on kidney–ureter–bladder (KUB) radiographs, using transfer learning with **YOLOv11**.

This repository accompanies the research project on deep learning–based ureteral stone detection.  
All experiments were conducted using YOLOv11 with fine-tuning on institutionally collected medical radiographs.

---

## 🧠 Overview

UreterStoneYOLO provides a reproducible implementation of a detection pipeline for ureteral stones using kidney–ureter–bladder (KUB) X-rays.  
The goal is to assist radiologists in identifying small ureteral stones with optimized detection sensitivity and minimal false positives.

---

## 👩‍💻 Author

All source code in this repository was written by **Jiho Park, M.D.**

**Jiho Park, M.D.**  
Resident / Research Assistant  
Department of Radiology, Seoul St. Mary's Hospital  
College of Medicine, The Catholic University of Korea  
222 Banpo-daero, Seocho-gu, Seoul, 06591, Republic of Korea  

---

## 📦 Installation

This project is based on **Python 3.10+** and **Ultralytics YOLOv11**.  
You can set up the environment as follows:

```bash
# 1. Clone this repository
git clone https://github.com/<your-username>/UreterStoneYOLO.git
cd UreterStoneYOLO

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate     # or: venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -U pip
pip install ultralytics opencv-python numpy matplotlib jupyter
```
---

## 👩‍💻 Author

Run the demonstration notebook to visualize and test detection results.

jupyter notebook demo.ipynb


The notebook includes:

Model loading and configuration

Example inference on sample radiographs

Visualization of detection outputs

⚠️ Note: Trained model weights (best.pt) are not included in this repository due to institutional and privacy policies.
Please contact the corresponding author for access to the trained model under research collaboration terms.

---

## ⚙️ Model and Training Details

Base model: YOLOv11 medium sized model (Ultralytics, 2024)

Training type: Transfer learning (fine-tuning)

Input size: 2560 x 2560 pixels

Optimizer: Automatically selected by Ultralytics (SGD, lr=0.01)

Dataset: KUB radiographs (institutional anonymized dataset) - not included

Evaluation metrics: Precision, Recall, mAP@50, mAP@50-95

---

## 🔒 Data Availability

The raw dataset (training/validation/test) is not publicly available due to patient privacy protection and institutional policy.
Data may be shared upon reasonable request to the corresponding author.

Corresponding Author
Hokun Kim, M.D., Ph.D.
Assistant Professor
Department of Radiology, Seoul St. Mary's Hospital
College of Medicine, The Catholic University of Korea
222 Banpo-daero, Seocho-gu, Seoul, 06591, Republic of Korea
Phone: +82-2-2258-1934

---

## 📖 Citation

If you find this repository useful, please cite our work:

📌 Paper under review.
Citation details will be updated once the manuscript is accepted for publication.

@article{park2025ureterstoneyolo,
  title={UreterStoneYOLO: Automated Detection of Ureteral Stones on KUB Radiographs Using YOLOv11},
  author={Park, Jiho and Kim, Hokun},
  journal={In preparation},
  year={2025}
}

---

## ⚠️ License and Usage Notice

This project uses the Ultralytics YOLOv11 framework, which is released under the AGPL-3.0 license.
Accordingly:

Use of this repository is permitted for academic and research purposes only.

Redistribution, integration into commercial software, or deployment as a cloud/web service requires a commercial license from Ultralytics.
See: https://ultralytics.com/license

---

## 🧾 Acknowledgments

We gratefully acknowledge the contribution of the Department of Radiology at Seoul St. Mary's Hospital for support and feedback throughout this study.

---

## 🩻 Contact

For questions, collaborations, or dataset/model access requests, please contact:

Jiho Park, M.D.
📧 hoyinside@gmail.com

Department of Radiology, Seoul St. Mary's Hospital
The Catholic University of Korea
