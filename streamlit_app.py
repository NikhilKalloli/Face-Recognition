import streamlit as st
from PIL import Image
from identify import *
from io import BytesIO


st.set_page_config(page_title="Face Recognition App", page_icon=":smiley:")

def main():
    st.title("Face Recognition App")
    sample_image_path = "./sample_image.jpg"
    sample_image = Image.open(sample_image_path)

    buf = BytesIO()
    sample_image.save(buf, format="JPEG")
    byte_im = buf.getvalue()

    sample_image_name = "sample_image.jpg"
    st.download_button(label="Download Sample Image", data=byte_im, file_name=sample_image_name, key="download_button")


    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image_placeholder = st.empty()
        recognizing_message = st.empty()

        image_placeholder.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        recognizing_message.write("Recognizing...")
       
        total_faces = faceDetection(uploaded_file)
        names = faceRecognition(uploaded_file)

        # Face Detection Results Section
        recognizing_message.empty()  
        st.header("Face Detection Results:")
        st.write(f"Total Faces Detected: {total_faces}")
        st.write(f"Total Recognized Faces: {getKnownFaces()}")
        st.write(f"Total Unrecognized Faces: {getUnknownFaces()}")

        # Names Section
        if names:
            st.header("Names:")
            for name in names:
                st.write(f"- {name}")

        # Known Faces Section
        known_names = getKnownName()
        if known_names:
            st.header("Known Faces:")
            for name in known_names:
                known_image_path = f"./known/{name}.jpg"
                known_image = Image.open(known_image_path)
                st.image(known_image, caption=name, width=200)

        # Unknown Faces Section
        st.header("Unknown Faces:")
        if getUnknownFaces() == 0:
            st.write("None")
        else:
            for i in range(getUnknownFaces()):
                unknown_image_path = f"./unknown/{i}.jpg"
                unknown_image = Image.open(unknown_image_path)
                st.image(unknown_image, caption=f"Unknown Face #{i + 1}", width=200)

        # Reset the known names and face counts
        setKnownName()
        setFacesToZero()

if __name__ == "__main__":
    main()
