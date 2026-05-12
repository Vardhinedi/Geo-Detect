import ollama
from pathlib import Path
from PIL import Image


# ---------------------------------------------------
# SCENE UNDERSTANDING FUNCTION
# ---------------------------------------------------

def analyze_scene(image_path):

    # ---------------------------------------------------
    # CREATE SMALLER IMAGE FOR VLM
    # ---------------------------------------------------

    resized_image_path = "data/resized_scene_image.jpg"

    image = Image.open(image_path)

    image.thumbnail((640, 640))

    image.save(resized_image_path)

    # ---------------------------------------------------
    # ABSOLUTE PATH
    # ---------------------------------------------------

    absolute_image_path = str(Path(resized_image_path).resolve())

    # ---------------------------------------------------
    # STRICT GROUNDED PROMPT
    # ---------------------------------------------------

    prompt = """
You are a geospatial image analyst.

Your task is to describe ONLY directly visible features in the aerial image.

STRICT RULES:

- Describe only observable infrastructure and activity
- Do NOT guess the environment type unless visually obvious
- Do NOT mention ships, boats, ports, military activity, surveillance, or tactical activity unless clearly visible
- Do NOT speculate beyond visible evidence
- Focus on roads, buildings, vehicles, vegetation, intersections, traffic density, and spatial layout
- Use concise factual observations
- If uncertain, say uncertain instead of guessing

Provide a short scene description.
"""

    # ---------------------------------------------------
    # SEND IMAGE TO MODEL
    # ---------------------------------------------------

    response = ollama.chat(
        model="minicpm-v",
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [absolute_image_path]
            }
        ]
    )

    # ---------------------------------------------------
    # EXTRACT RESPONSE
    # ---------------------------------------------------

    scene_report = response["message"]["content"]

    return scene_report