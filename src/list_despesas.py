import os

base_path = "data/raw/extracted"

keywords = [
    "evento",
    "sinistro",
    "assist",
    "contab",
    "desp"
]

for root, dirs, files in os.walk(base_path):
    for file in files:
        name = file.lower()
        if any(k in name for k in keywords):
            print(os.path.join(root, file))
