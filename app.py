import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image

# Load your trained model
model = load_model('rice_disease_model.keras')

# Expanded static disease information
disease_info = {
    'Bacterial leaf blight': {
        'causes': 'Caused by the bacterium Xanthomonas oryzae.',
        'symptoms': [
            'Yellowing of leaves starting from the leaf tips.',
            'Water-soaked lesions that turn dark brown or black.',
            'Wilting and stunted growth.'
        ],
        'treatments': [
            'Use resistant varieties of rice.',
            'Apply appropriate antibiotics such as streptomycin or oxytetracycline.',
            'Ensure proper field sanitation and crop rotation.'
        ],
        'prevention': [
            'Plant certified disease-free seeds.',
            'Practice crop rotation with non-host crops.',
            'Avoid overhead irrigation to reduce leaf wetness.'
        ]
    },
    'Brown spot': {
        'causes': 'Fungal disease caused by Bipolaris oryzae.',
        'symptoms': [
            'Brown spots on leaves, often with a yellow halo.',
            'Leaf drying and necrosis.',
            'Reduced yield due to affected plants.'
        ],
        'treatments': [
            'Use fungicides such as propiconazole or chlorothalonil.',
            'Remove and destroy infected plant debris.',
            'Ensure proper drainage in fields.'
        ],
        'prevention': [
            'Practice crop rotation with resistant varieties.',
            'Maintain proper nitrogen levels in soil.',
            'Avoid planting in overly wet conditions.'
        ]
    },
    'Leaf smut': {
        'causes': 'Fungal infection caused by Entyloma oryzae.',
        'symptoms': [
            'Black smutty spores on leaves and panicles.',
            'Stunted growth and reduced yield.',
            'May cause complete crop failure in severe cases.'
        ],
        'treatments': [
            'Remove and destroy infected plants.',
            'Apply fungicides if necessary, though less effective once symptoms appear.',
            'Practice good field sanitation.'
        ],
        'prevention': [
            'Use resistant varieties of rice.',
            'Avoid planting rice in heavily infested fields.',
            'Ensure proper spacing to reduce humidity among plants.'
        ]
    }
}

# Function to preprocess the uploaded image
def load_and_prep_image(uploaded_file):
    img = Image.open(uploaded_file)
    img = img.resize((224, 224))  # Resize to the input size of the model
    img = np.array(img) / 255.0   # Normalize the image
    img = img.reshape(1, 224, 224, 3)  # Add batch dimension
    return img

# Streamlit UI
st.title("Rice Disease Detection and Consultation")

uploaded_file = st.file_uploader("Upload an image of a rice leaf", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("Classifying...")

    img = load_and_prep_image(uploaded_file)
    predictions = model.predict(img)
    predicted_class = np.argmax(predictions, axis=-1)

    # Mapping model output to class labels
    class_labels = {0: 'Bacterial leaf blight', 1: 'Brown spot', 2: 'Leaf smut'}
    predicted_label = class_labels[predicted_class[0]]

    st.write(f"Predicted Disease: **{predicted_label}**")

    # Fetching disease information from static dictionary
    if predicted_label in disease_info:
        info = disease_info[predicted_label]
        
        st.write(f"**Causes:** {info['causes']}")
        st.write(f"**Symptoms:**")
        for symptom in info['symptoms']:
            st.write(f"- {symptom}")
        st.write(f"**Treatments:**")
        for treatment in info['treatments']:
            st.write(f"- {treatment}")
        st.write(f"**Prevention:**")
        for prevention in info['prevention']:
            st.write(f"- {prevention}")
    else:
        st.write("No information available for this disease.")