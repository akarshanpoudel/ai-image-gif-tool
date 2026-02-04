# ai-image-gif-tool
AI-powered Image to GIF web app with face-aware blur and background removal. Built using Python &amp; Streamlit.
# 🧠 AI Image → GIF Tool

A web-based AI application that converts images into optimized GIFs with advanced features like **face-aware background blur** and **AI background removal**.

Built using **Python**, **Streamlit**, **OpenCV**, and **rembg**.

---

## 🚀 Features

- 🖼 Upload PNG / JPG images
- 🎞 Convert multiple images into animated GIFs
- 🙂 Face-aware background blur (keeps faces sharp)
- 🧠 AI background removal (U²-Net via rembg)
- 🎚 Adjustable sliders:
  - Output image size
  - Blur strength
  - GIF frame duration
- ⚡ Optimized GIF size & quality
- 🌐 Deployed online using Streamlit Cloud

---

## 🖥 Live Demo

👉 *(Add your Streamlit Cloud URL here after deployment)*

---

## 🛠 Tech Stack

- **Python 3.9+**
- **Streamlit** – Web UI
- **Pillow (PIL)** – Image processing
- **OpenCV** – Face detection
- **rembg** – AI background removal
- **ONNX Runtime** – AI inference
- **NumPy**

---

## 📂 Project Structure
project/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignored files


---

## ⚙️ Local Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ai-image-gif-tool.git
cd ai-image-gif-tool
python -m pip install -r requirements.txt
python -m streamlit run app.py
http://localhost:8501
⚠️ Notes

First AI background removal run may take 30–60 seconds (model load).

Instagram profile pictures do not animate GIFs (only first frame).

Best use cases: stories, reels, previews, highlight covers.

