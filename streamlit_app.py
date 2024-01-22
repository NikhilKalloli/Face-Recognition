import streamlit as st
from PIL import Image
from identify import *

# Set the page title
st.set_page_config(page_title="Face Recognition App", page_icon=":smiley:")

# Main Streamlit app
def main():
    st.title("Face Recognition App")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        st.write("")
        st.write("Classifying...")

        # Perform face detection and recognition
        total_faces = faceDetection(uploaded_file)
        names = faceRecognition(uploaded_file)

        # Display the results
        st.write(f"Total Faces Detected: {total_faces}")
        st.write(f"Total Known Faces: {getKnownFaces()}")
        st.write(f"Total Unknown Faces: {getUnknownFaces()}")
        
        if names:
            st.write("Names:")
            for name in names:
                st.write(f"- {name}")

      # Display known faces
        known_names = getKnownName()
        if known_names:
            st.write("Known Faces:")
            for name in known_names:
                known_image_path = f"./known/{name}.jpg"
                known_image = Image.open(known_image_path)
                # resized_known_image = known_image.resize((200, 200))  # Resize the image
                st.image(known_image, caption=name, width=200)


# Display unknown faces
        st.write("Unknown Faces:")
        for i in range(getUnknownFaces()):
            unknown_image_path = f"./unknown/{i}.jpg"
            unknown_image = Image.open(unknown_image_path)
            # resized_unknown_image = unknown_image.resize((200, 200))  # Resize the image
            st.image(unknown_image, caption=f"Unknown Face {i}", width=200)

        # Reset the known names and face counts
        setKnownName()
        setFacesToZero()


# Run the app
if __name__ == "__main__":
    main()
