from scene_understanding import analyze_scene


# ---------------------------------------------------
# IMAGE PATH
# ---------------------------------------------------

image_path = "data/test_image.jpg"


# ---------------------------------------------------
# RUN SCENE ANALYSIS
# ---------------------------------------------------

scene_report = analyze_scene(image_path)


# ---------------------------------------------------
# PRINT RESULTS
# ---------------------------------------------------

print("\nSCENE UNDERSTANDING REPORT\n")

print(scene_report)