# Rice Leaf Disease Detection Using Deep Learning (CNN)

This repository contains a deep learning model for rice leaf disease classification, built using Convolutional Neural Networks (CNN) and deployed with **Streamlit**. The system allows users to upload images of rice leaves, predicts the disease, and provides information on causes, symptoms, treatments, and prevention methods.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Model Overview](#model-overview)
- [Disease Information](#disease-information)
- [Future Improvements](#future-improvements)
- [License](#license)

## Features
- **Image Classification**: Upload an image of a rice leaf and receive a prediction of the disease.
- **Disease Consultation**: Detailed information on causes, symptoms, treatments, and prevention for the detected disease.
- **Web Interface**: Easy-to-use web application powered by **Streamlit**.

## Technologies
- **TensorFlow**: Used for building the CNN model.
- **Keras**: Provides an easy interface for deep learning.
- **Streamlit**: For creating a user-friendly web interface.
- **PIL**: Used for image processing.
- **NumPy**: For numerical computations.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/VishahFatima/Rice-Leaf-Disease-Detection-using-Image-Classification.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Rice-Leaf-Disease-Detection-using-Image-Classification
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Ensure that your trained model is saved as `rice_disease_model.keras` in the project root directory.

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Upload an image of a rice leaf in **JPG**, **JPEG**, or **PNG** format.

3. The app will classify the image and provide details about the disease.

## Model Overview
The CNN model was trained using the **Rice Leaf Disease Dataset** from Kaggle. The model classifies images into three categories:
- **Bacterial Leaf Blight**
- **Brown Spot**
- **Leaf Smut**

### Model Summary:
- Input Size: 224x224x3 (RGB images)
- Layers: 4 Convolutional layers with MaxPooling, Flatten, Dense layers, and Dropout.
- Optimizer: Adam
- Loss Function: Categorical Crossentropy
- Accuracy: 70.83% on validation data.

## Disease Information

The app provides information about the following diseases:

- **Bacterial Leaf Blight**:
  - Causes: Caused by the bacterium *Xanthomonas oryzae*.
  - Symptoms: Yellowing of leaves, water-soaked lesions, wilting.
  - Treatments: Use resistant varieties, apply antibiotics, and ensure field sanitation.
  - Prevention: Use certified seeds, practice crop rotation, avoid overhead irrigation.

- **Brown Spot**:
  - Causes: Fungal disease caused by *Bipolaris oryzae*.
  - Symptoms: Brown spots with yellow halos, leaf necrosis, reduced yield.
  - Treatments: Use fungicides, remove infected debris, ensure proper drainage.
  - Prevention: Crop rotation, maintain soil nitrogen levels, avoid overly wet conditions.

- **Leaf Smut**:
  - Causes: Fungal infection caused by *Entyloma oryzae*.
  - Symptoms: Black smutty spores, stunted growth, reduced yield.
  - Treatments: Remove infected plants, apply fungicides, practice good sanitation.
  - Prevention: Use resistant varieties, avoid infested fields, ensure proper spacing.

## Future Improvements
- Expand the model to recognize more rice diseases.
- Improve accuracy by using more advanced architectures (e.g., ResNet, Inception).
- Add multilingual support for a wider user base.
