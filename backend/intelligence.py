import json
import ollama
from pathlib import Path

from backend.scene_understanding import analyze_scene


# ---------------------------------------------------
# REPORT GENERATION FUNCTION
# ---------------------------------------------------

def generate_report(detections, image_path):

    # ---------------------------------------------------
    # RUN SCENE UNDERSTANDING
    # ---------------------------------------------------

    scene_assessment = analyze_scene(image_path)

    # ---------------------------------------------------
    # FORMAT DETECTIONS
    # ---------------------------------------------------

    formatted_detections = json.dumps(detections, indent=4)

    # ---------------------------------------------------
    # FUSED MULTIMODAL PROMPT
    # ---------------------------------------------------

    prompt = f"""
You are a professional geospatial intelligence analyst.

You are provided:

1. Structured aerial detections
2. Scene-level aerial image understanding

---------------------------------------------------
SCENE ASSESSMENT
---------------------------------------------------

{scene_assessment}

---------------------------------------------------
DETECTION DATA
---------------------------------------------------

{formatted_detections}

---------------------------------------------------
ANALYTICAL RULES
---------------------------------------------------

You MUST follow these rules strictly:

- Report ONLY evidence visible in the image or detections
- Do NOT infer military activity without explicit visual indicators
- Do NOT infer surveillance, law enforcement, hostile activity, or tactical intent unless directly observable
- Default to civilian/commercial interpretation when evidence is ambiguous
- Clearly separate observations from assessments
- Avoid dramatic or speculative language
- Be concise, factual, and operationally focused
- Mention uncertainty briefly when necessary

---------------------------------------------------
REQUIRED OUTPUT FORMAT
---------------------------------------------------

SCENE TYPE:
(1-2 lines)

OBSERVED INFRASTRUCTURE:
(1-3 lines)

OBSERVED VEHICLE / MARITIME ACTIVITY:
(1-3 lines)

SPATIAL PATTERNS:
(1-3 lines)

ANALYST ASSESSMENT:
(2-4 lines)

CONFIDENCE:
(Low / Moderate / High with short explanation)
"""

    # ---------------------------------------------------
    # GENERATE REPORT
    # ---------------------------------------------------

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # ---------------------------------------------------
    # EXTRACT REPORT
    # ---------------------------------------------------

    report = response["message"]["content"]

    # ---------------------------------------------------
    # SAVE REPORT
    # ---------------------------------------------------

    Path("reports").mkdir(exist_ok=True)

    report_path = "reports/intelligence_report.txt"

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)

    # ---------------------------------------------------
    # RETURN RESULTS
    # ---------------------------------------------------

    return {
        "report": report,
        "scene_assessment": scene_assessment,
        "report_path": report_path
    }