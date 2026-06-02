from pathlib import Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB
app.config["UPLOAD_FOLDER"] = "uploads"

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "bmp"}


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/classify")
def classify_image():
    file = request.files.get("image")

    if not file or file.filename == "":
        return render_template(
            "index.html",
            error="Please choose an image file before submitting.",
        )

    if not allowed_file(file.filename):
        return render_template(
            "index.html",
            error="Unsupported file type. Please upload PNG, JPG, JPEG, WEBP, or BMP.",
        )

    upload_dir = Path(app.config["UPLOAD_FOLDER"])
    upload_dir.mkdir(parents=True, exist_ok=True)

    safe_name = secure_filename(file.filename)
    save_path = upload_dir / safe_name
    file.save(save_path)

    result = "Real"
    confidence = "100.00%"

    return render_template(
        "index.html",
        result=result,
        confidence=confidence,
        filename=safe_name,
    )


if __name__ == "__main__":
    app.run(debug=True)
