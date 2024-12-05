# Deep Learning

## Keras Datasets

This repository contains various datasets commonly used in computer vision and machine learning tasks. Below are brief descriptions of each dataset included:

### Table of Contents
1. [Introduction](#introduction)
2. [Datasets](#datasets)
   - [CIFAR-10](#cifar-10)
   - [MNIST](#mnist)
   - [Fashion MNIST](#fashion-mnist)
   - [IMDB](#imdb)
   - [Reuters](#reuters)
   - [Boston Housing ](#boston-housing-dataset)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)

## CIFAR-10
- **Description**: CIFAR-10 is a benchmark dataset consisting of 60,000 32x32 color images in 10 classes, with 6,000 images per class. It is commonly used for image classification tasks.
- **Applications**: Image classification, Convolutional Neural Networks (CNNs).
- **Source**: CIFAR-10 Dataset

## MNIST
- **Description**: MNIST is a dataset of handwritten digits containing 60,000 training images and 10,000 testing images, each in a 28x28 grayscale image format.
- **Applications**: Handwritten digit recognition, Image classification.
- **Source**: MNIST Dataset

## Fashion MNIST
- **Description**: Fashion MNIST is a dataset of Zalando's article images, consisting of 60,000 training images and 10,000 testing images. Each image is a 28x28 grayscale image labeled with 10 classes.
- **Applications**: Image classification.
- **Source**: Fashion MNIST Dataset

## IMDB
- **Description**: IMDB is a dataset of movie reviews for sentiment analysis. It consists of 50,000 movie reviews categorized into positive and negative reviews.
- **Applications**: Sentiment analysis, Natural Language Processing (NLP).
- **Source**: IMDB Dataset

## Reuters
- **Description**: Reuters is a dataset of Reuters news articles categorized into 46 topics. It is used for text categorization and includes 11,228 training documents and 2,578 test documents.
- **Applications**: Text categorization, Natural Language Processing (NLP).
- **Source**: Reuters Dataset

## Boston Housing 
- **Description**: The Boston Housing dataset contains information collected by the U.S Census Service concerning housing in the area of Boston, Massachusetts. The dataset includes 506 instances and 14 attributes, including the median value of owner-occupied homes in $1000s.
- **Applications**: Regression analysis, prediction of housing prices.
- **Source**: UCI Machine Learning Repository

## Installation
To get started with this repository, clone it to your local machine and install the necessary dependencies.
```
bash
git clone https://github.com/oscartma/DeepLearning.git
cd DeepLearning
pip install -r requirements.txt
```

## Usage
Each dataset has its own sub-directory with specific instructions on how to run the code. Generally, you can navigate to the respective dataset directory and execute the Python scripts.

For example, to run a model on the CIFAR-10 dataset:
cd CIFAR-10
python train_model.py

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/usuario/cifar10-deeplearning-docker-k8s/notebooks/cifar10_training.ipynb)



## Contributing
We welcome contributions to this repository. If you have any suggestions or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
