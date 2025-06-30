from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename
from pdf_operations.merge import merge_pdfs

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
MERGED_FILE = "merged_output.pdf"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        files = request.files.getlist("pdfs")
        file_paths = []

        for f in files:
            filename = secure_filename(f.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            f.save(path)
            file_paths.append(path)

        merge_pdfs(file_paths, MERGED_FILE)
        return send_file(MERGED_FILE, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
