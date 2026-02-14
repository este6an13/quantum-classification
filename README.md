### 🧬 Quantum-Based Binary Classification of Histological Images of Salivary Glands with Sjögren Syndrome

Designed and evaluated **quantum-enhanced neural network architectures** for the **binary classification of salivary gland histological images** associated with **Sjögren’s Syndrome**.
Implemented and compared **quanvolutional neural networks (QNNs)** against classical **CNNs**, using **random quantum circuits** as local feature extractors within a hybrid quantum–classical pipeline.

Built a complete experimental framework including **image preprocessing**, **quantum feature extraction**, and **model evaluation** under **10 randomized train–test splits with 5-fold cross-validation**.
Explored multiple experimental variants: **downsampled vs. original-resolution images**, **data augmentation**, **stacked quanvolutional layers**, **hyperparameter grid search**, and **transfer learning** using **MedViT** and **ResNet18** features.

Implemented **quanvolutional layers** using **Pennylane**, encoding local image patches into **4-qubit quantum circuits** with randomized rotations and entangling gates, and integrated them into PyTorch training loops.
Extended the study with **variational quantum classifiers (VQC)** in a **Dressed Quantum Neural Network** setting, analyzing optimization behavior, overfitting, and performance degradation related to barren plateaus and feature incompatibility.

The project revealed regimes where QNNs outperform classical CNNs on limited data, as well as failure modes where quantum layers struggle to exploit transformer-based features, highlighting both the promise and current limitations of quantum machine learning in medical imaging.