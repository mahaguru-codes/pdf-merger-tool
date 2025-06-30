# 📄 PDF Merger Tool (Web Version)

A simple, fast, and user-friendly **PDF Merger** built with Python and Flask. Upload multiple PDF files and download a single, merged file — all from your browser. Deployed and hosted on Replit.

![image](https://github.com/user-attachments/assets/4466b040-2078-473c-9444-2798eb5779a8)

---

## ✨ Features

- 🔗 Merge multiple PDFs into one
- 📁 Upload via web interface (no CLI required)
- 💾 Download merged file instantly
- 🧩 Modular architecture (`Flask` + `pypdf`)
- 🌐 Hosted online (Replit-friendly)

---

## 🚀 Live Demo

👉 **[Try it here](https://your-replit-url.repl.co)**  
*(Replace with your actual Replit link)*

---

## 🧰 Technologies Used

| Tech     | Purpose                     |
|----------|-----------------------------|
| Python   | Core programming language   |
| Flask    | Web framework (backend)     |
| pypdf    | PDF handling (merging)      |
| HTML/CSS | Frontend UI                 |
| Replit   | Hosting platform            |

---

## 📦 Project Structure

pdf-merger-tool/
├── app.py # Flask application entry point
├── requirements.txt # Dependencies (Flask, pypdf)
├── .replit # Replit config (run = python app.py)
├── templates/
│ └── index.html # Frontend HTML
├── static/
│ └── styles.css # UI styling
└── pdf_operations/
└── merge.py # PDF merging logic (pypdf)

---

## 🛠️ Local Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/pdf-merger-tool.git
cd pdf-merger-tool

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then visit http://localhost:8080 in your browser.
