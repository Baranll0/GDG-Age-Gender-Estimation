import stone
from json import dumps

palette = [
    "#f1d5d2", "#f9e8d8", "#f5e3d7", "#e8d1c3", "#d7c1aa",
    "#f3c8bf", "#f4d8c0", "#f4d1bb", "#e2c7b6", "#c6b099",
    "#e6b7af", "#eecaa6", "#e8c0a7", "#d5b6a2", "#b89d82",
    "#dfa399", "#e3bc95", "#d5ad94", "#bb9c87", "#957c66",
    "#d3948b", "#d4a97f", "#b9937e", "#a2826d", "#7c6253",
    "#9e6f69", "#9f7e5f", "#8b6e60", "#977663", "#5b453a"
]

labels = [
    "Light",
    "Light Medium",
    "Medium",
    "Medium Tan",
    "Tan",
    "Deep"
]

# Sonuç listesi
createdLabels = []

# Palette içindeki her bir değer için label ve indeks oluşturma
for i in range(len(palette)):
    label_index = i // 5  # Her label için 5 adet palette rengi
    if label_index < len(labels):
        label = labels[label_index]
        createdLabels.append(f"{label} {i % 5 + 1}")

print(createdLabels)


def detectSkinColor(image_path: str):
    # process the image
    result = stone.process(filename_or_url = image_path, tone_palette = palette, tone_labels = createdLabels, return_report_image=True,)
    
    # show the report image (return_report_image = True is required) 
    report_images = result.pop("report_images")  # obtain and remove the report image from the `result`
    face_id = 1
    stone.show(report_images[face_id])

    # convert the result to json
    result_json = dumps(result)
    print(result_json)


detectSkinColor("C:/dev/ml/GDG-AI-Team/scripts/a.jpg")


