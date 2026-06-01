import pandas as pd
from pathlib import Path

base = Path("dataset")

rows = []

for split in ["train", "val", "test"]:
    for label, y in [("real", 0), ("fake", 1)]:
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