# phishing-email-detection-nlp
# Phishing Email Detection 

## Overview
This project implements a TF-IDF + Logistic Regression pipeline for detecting phishing emails.


## Quickstart
1. Create Python venv and install:
   `pip install -r requirements.txt`
2. Run demo:
   `python phishing_nlp_detection.py`

## Files
- `phishing_nlp_detection.py` — main script (training + evaluation + interactive mode)
- `phishing_emails.csv` — sample dataset
- `phishing_detector.joblib` — saved model (output)
- `tests/` — unit tests (created by Teammate B)
- `slides/` — presentation slides (created by Teammate D)

## Usage Examples
- Train and evaluate:
  `python phishing_nlp_detection.py`
- Predict a single email:
  `python predict.py --text "Urgent!"

## FAQ
Q: What does label 1 mean?
A: `1` = phishing, `0` = legitimate.

Q: How to re-train with my own dataset?
A: Replace `phishing_emails.csv` with your CSV (columns: text,label) and run the script.
