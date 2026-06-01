import pandas as pd
from pathlib import Path

dataset_dir = Path("dataset")

rows = []

for img_path in (dataset_dir / "real").glob("*"):
    if img_path.is_file():
        rows.append({
            "x": str(img_path),
            "y": 0
        })

for img_path in (dataset_dir / "fake").glob("*"):
    if img_path.is_file():
        rows.append({
            "x": str(img_path),
            "y": 1
        })

df = pd.DataFrame(rows)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv("deepfake_dataset.csv", index=False)