# QR Code Counterfeit Detection

This project implements various computer vision, machine learning, and deep learning techniques to differentiate between original (first print) and counterfeit (second print) QR codes. It includes:
1. data preprocessing
2. feature engineering
3. exploratory data analysis (EDA)
4. model training / fine-tuning
5. evaluation


## Setup and Installation:

1\. Clone the Repository: 
```
git clone https://github.com/coderkageQRCode-Counterfeit-Detection.git
cd QRCode-Counterfeit-Detection
```

2\. Install Dependencies: 
```
pip install -r requirements.txt
```

3\. Prepare the Dataset:  
- Ensure that \"fp/\" (first print) and \"sp/\" (second print) contain the original images.
- Run \"copy_rename.py\" to rename and organize images into the \"data/\" folder.


## Feature Engineering:

Extracted numerical features include:

1. Statistical Features: Entropy, kurtosis, variance
2. Image-based Metrics: Peak separation, Euclidean peak distance, edge density, blur level
3. Signal Quality: Signal-to-noise ratio (SNR)
4. Global Image Features: Height, width, area

Features are stored in \"feature_data.csv\" for traditional ML models and FFNN.

## Models Implemented:

Traditional Machine Learning Models: 
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- k-Nearest Neighbors (KNN)
- XGBoost

Deep Learning Models: 
- Feedforward Neural Network (FFNN) (trained on extracted features)
- Convolutional Neural Network (CNN) (trained on raw image data)
- Transfer Learning (ResNet-18) (pretrained on ImageNet, fine-tuned for classification)

## Evaluation:

Models were evaluated using: 
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrices

## Conclusion:

This project successfully applies both machine learning and deep learning to QR code print authentication. Future work may focus on:

- Deploying as a real-time API
- Improving model robustness
- Optimizing for edge devices
