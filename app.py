import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


model = load_model('brain_tumor.h5')


st.markdown(
    """
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #8EE4AF;
            padding: 20px;
            margin-bottom: 20px;
        }
        .navbar-title {
            font-size: 36px; 
            font-weight: bold;
            margin-right: 10px;
        }
        .navbar-logo {
            height: 40px;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: #666;
        }
    </style>
    
    <div class="navbar">
        <div class="navbar-title">Tumor Track AI</div>
    </div>
    """, unsafe_allow_html=True
)


uploaded_file = st.file_uploader("Upload MRI image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
   
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

   
    img = image.load_img("temp_image.jpg", target_size=(224, 224))
    x = image.img_to_array(img)
    x = x / 255.0  
    x = np.expand_dims(x, axis=0)

    
    preds = model.predict(x)
    pred_class = np.argmax(preds, axis=1)[0]

    
    classes = ["Glioma Tumor", "Meningioma Tumor", "No Tumor", "Pituitary Tumor"]
    result = classes[pred_class]

   
    st.info("Result: " + result)
    st.image(img, caption="Uploaded MRI Image", use_column_width=True)


st.markdown(
    """
    <div class="footer">
        Created and Designed by BRATAJIT DAS | &copy 2024 All Rights Reserved
    </div>
    """, unsafe_allow_html=True
)
