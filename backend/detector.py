from ultralytics import YOLO
from pathlib import Path
import json


# ---------------------------------------------------
# LOAD OBB MODEL
# ---------------------------------------------------

model = YOLO("yolov8n-obb.pt")


# ---------------------------------------------------
# DETECTION FUNCTION
# ---------------------------------------------------

def run_detection(image_path):

    # Create output directory
    output_dir = "data/output"

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------
    # RUN OBB DETECTION
    # ---------------------------------------------------

    results = model(
        image_path,
        imgsz=1280,
        conf=0.20
    )

    result = results[0]

    # ---------------------------------------------------
    # SAVE CLEAN VISUALIZATION
    # ---------------------------------------------------

    output_image_path = f"{output_dir}/detected_image.jpg"

    plotted_image = result.plot(
        labels=False,
        boxes=True,
        conf=False
    )

    from PIL import Image
    import numpy as np

    Image.fromarray(plotted_image[..., ::-1]).save(output_image_path)

    # ---------------------------------------------------
    # EXTRACT OBB DETECTIONS
    # ---------------------------------------------------

    detections = []

    if result.obb is not None:

        for i in range(len(result.obb.cls)):

            class_id = int(result.obb.cls[i])

            object_name = result.names[class_id]

            confidence = float(result.obb.conf[i])

            xywhr = result.obb.xywhr[i].tolist()

            corners = result.obb.xyxyxyxy[i].tolist()

            detection_data = {
                "object": object_name,
                "confidence": round(confidence, 2),

                "center_coordinates": {
                    "x_center": round(xywhr[0], 2),
                    "y_center": round(xywhr[1], 2)
                },

                "dimensions": {
                    "width": round(xywhr[2], 2),
                    "height": round(xywhr[3], 2)
                },

                "rotation_radians": round(xywhr[4], 4),

                "rotated_corners": [
                    {
                        "x": round(point[0], 2),
                        "y": round(point[1], 2)
                    }
                    for point in corners
                ]
            }

            detections.append(detection_data)

    # ---------------------------------------------------
    # SAVE JSON
    # ---------------------------------------------------

    json_output_path = f"{output_dir}/detection_results.json"

    with open(json_output_path, "w") as file:
        json.dump(detections, file, indent=4)

    # ---------------------------------------------------
    # RETURN RESULTS
    # ---------------------------------------------------

    return {
        "detections": detections,
        "output_image_path": output_image_path,
        "json_output_path": json_output_path
    }