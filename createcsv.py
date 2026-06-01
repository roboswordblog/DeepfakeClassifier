import pandas as pd
from pathlib import Path
# https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images?resource=download for the data
base = Path("Dataset")

rows = []

for split in ["Train", "Validation", "Test"]:
    for label, y in [("Real", 0), ("Fake", 1)]:
        folder = base / split / label

        for img in folder.iterdir():
            if img.is_file():
                rows.append({
                    "x": str(img),
                    "y": y,
                    "split": split
                })

df = pd.DataFrame(rows)

df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("dataset.csv", index=False)