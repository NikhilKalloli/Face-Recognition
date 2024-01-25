# Face Recognition App

This is a Streamlit web application for face recognition using a pre-trained YOLO (You Only Look Once) model and the DeepFace library. The app allows users to upload an image, detects faces, and performs face recognition to identify known faces.

## Features

- **Face Detection**: The app uses the YOLO model to detect faces in uploaded images.

- **Face Recognition**: The DeepFace library is employed for face recognition. Known faces are saved in the 'known' folder, and unknown faces are saved in the 'unknown' folder.

- **User-friendly Interface**: The Streamlit app provides a user-friendly interface for easy interaction.


## Usage

1. Clone the repository:

   ```
   git clone https://github.com/NikhilKalloli/Face-Recognition.git
   ```
2. Navigate to the directory:
    ```
    cd face-recognition-app
    ```

3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ``` 
    streamlit run streamlit_app.py
    ```