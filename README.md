# TrashNet: Automated Waste Classification with Deep Learning

## Overview

TrashNet is an AI-powered system designed to classify waste into recyclable categories using deep learning. This project utilizes the TrashNet dataset to build a convolutional neural network (CNN) that accurately labels images of trash as either non-recyclable or one of five recyclable materials: paper, cardboard, glass, metal, and plastic. The model incorporates data augmentation techniques to enhance generalization and performance on unseen data.


## Getting Started

### Prerequisites

- Python 3.6+
- TensorFlow 2.x
- Additional libraries specified in `requirements.txt`

## Data Preparation
The data preparation script data_preparation.py splits the dataset into training, validation, and test sets. It organizes the data into separate directories for each class and applies the necessary transformations.

## Model Training
The model_training.py script builds and trains a convolutional neural network (CNN) using the training and validation datasets. Data augmentation techniques such as rotation, shifting, and zooming are applied to improve the model's robustness.

## Key Model Architecture
Convolutional layers with ReLU activation
MaxPooling layers
Dense layers with Dropout for regularization
Output layer with softmax activation for multi-class classification
## Data Preparation

The data preparation script `data_preparation.py` splits the dataset into training, validation, and test sets. It organizes the data into separate directories for each class and applies the necessary transformations.

## Model Training

The `model_training.py` script builds and trains a convolutional neural network (CNN) using the training and validation datasets. Data augmentation techniques such as rotation, shifting, and zooming are applied to improve the model's robustness.

### Key Model Architecture

- Convolutional layers with ReLU activation
- MaxPooling layers
- Dense layers with Dropout for regularization
- Output layer with softmax activation for multi-class classification

## Model Evaluation

The `model_evaluation.py` script evaluates the trained model on the test dataset. It reports the model's accuracy and identifies misclassified images for further analysis.

## Results

### Without Data Augmentation

- **Test Accuracy**: 58.27%
- **Training Time**: Shorter per epoch

### With Data Augmentation

- **Test Accuracy**: 66.54%
- **Training Time**: Longer per epoch

### Unseen Data

- **Test Accuracy on Unseen Data**: 84.21%

The model with data augmentation achieved higher accuracy, demonstrating the effectiveness of augmentation in improving model generalization.

## Visualization and Analysis

Misclassified images were analyzed to identify patterns and common characteristics. Most misclassifications occurred in zoomed-in images with complex backgrounds. Adjustments to the zoom range in data augmentation helped improve performance on such images.


## Acknowledgments
- [TrashNet Dataset](https://www.kaggle.com/datasets/feyzazkefe/trashnet)
- TensorFlow and Keras for providing powerful deep learning tools
