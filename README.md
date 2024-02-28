# TumorTrack AI

TumorTrack AI is a Transfer Learning based brain tumor classification system capable of predicting type of brain tumor using MRI images.It is trained using Inception V3 architecture and has acquired an accuracy of 93.69% on the training dataset and 80.20% on the validation dataset.

# How to Run

1. **Install Dependencies**: Make sure you have the necessary dependencies installed. You can install them using the following command:
    ```
    pip install -r requirements.txt
    ```

2. **Run the Application**: Run the Streamlit application using the following command:
    ```
    streamlit run app.py
    ```

3. **Upload MRI Images**: Once the application is running, upload an MRI image of the brain using the file uploader.

4. **View Results**: The application will process the uploaded image and display the predicted result indicating the type of tumor detected.

# Screenshots

| ![screenshot 1](https://github.com/Bratajit-03/TumorTrack-AI/assets/106532791/3b063bdd-a300-4157-8a6f-36a8614e120d) | ![Screenshot 2](https://github.com/Bratajit-03/TumorTrack-AI/assets/106532791/9b4eee27-ad3f-43ee-b85b-4e0fc5b35215) |
|:--:|:--:|
| *Caption: Upload an MRI image* | *Caption: Displaying the predicted result* |

# Dataset

The model was trained on the [Brain MRI Images for Brain Tumor Classification](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri) dataset available on Kaggle.

# License

This project is licensed under MIT License - see the [LICENSE](LICENSE) file for details.
