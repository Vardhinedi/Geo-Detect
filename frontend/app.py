import sys
from pathlib import Path

# ---------------------------------------------------
# FIX PYTHON IMPORT PATH
# ---------------------------------------------------

project_root = Path(__file__).resolve().parent.parent

sys.path.append(str(project_root))


# ---------------------------------------------------
# IMPORTS
# ---------------------------------------------------

import streamlit as st
from PIL import Image

from backend.detector import run_detection
from backend.intelligence import generate_report


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Satellite Intelligence System",
    layout="wide"
)

st.title("Satellite Vehicle Intelligence System")


# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Aerial / Satellite Image",
    type=["jpg", "jpeg", "png"]
)


# ---------------------------------------------------
# PROCESS IMAGE
# ---------------------------------------------------

if uploaded_file is not None:

    # Create directories
    Path("data").mkdir(exist_ok=True)
    Path("data/output").mkdir(parents=True, exist_ok=True)

    # Save uploaded image
    image_path = "data/test_image.jpg"

    with open(image_path, "wb") as file:
        file.write(uploaded_file.read())

    st.success("Image uploaded successfully.")

    # ---------------------------------------------------
    # DISPLAY ORIGINAL IMAGE
    # ---------------------------------------------------

    st.subheader("Original Image")

    original_image = Image.open(image_path)

    st.image(original_image, use_container_width=True)

    # ---------------------------------------------------
    # RUN DETECTION
    # ---------------------------------------------------

    st.subheader("Running Detection Engine...")

    detection_results = run_detection(image_path)

    detections = detection_results["detections"]

    detected_image_path = detection_results["output_image_path"]

    # ---------------------------------------------------
    # DISPLAY DETECTION IMAGE
    # ---------------------------------------------------

    st.subheader("Detection Output")

    detected_image = Image.open(detected_image_path)

    st.image(detected_image, use_container_width=True)

    # ---------------------------------------------------
    # DISPLAY STRUCTURED DATA
    # ---------------------------------------------------

    st.subheader("Structured Detection Data")

    st.json(detections)

    # ---------------------------------------------------
    # GENERATE REPORT
    # ---------------------------------------------------

    st.subheader("Generating Intelligence Report...")

    intelligence_results = generate_report(
        detections,
        image_path
   )

    report = intelligence_results["report"]

    # ---------------------------------------------------
    # DISPLAY REPORT
    # ---------------------------------------------------

    st.subheader("AI Intelligence Report")

    st.write(report)

    st.success("Analysis completed successfully.")