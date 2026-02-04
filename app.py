import streamlit as st
from PIL import Image
import numpy as np
import cv2
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Image → GIF Tool",
    layout="centered"
)

st.title(" AI Image → GIF Tool")

# ---------------- FACE DETECTOR ----------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- FUNCTIONS ----------------

def resize_image(img, size):
    return img.resize((size, size), Image.LANCZOS)

def face_aware_blur(img, blur_strength):
    img_np = np.array(img)
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0:
        return img

    mask = np.zeros_like(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

    k = blur_strength * 2 + 1
    blurred = cv2.GaussianBlur(img_np, (k, k), 0)
    final = np.where(mask[..., None] == 255, img_np, blurred)

    return Image.fromarray(final)

def ai_background_removal(img):
    from rembg import remove  # lazy load
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    result = remove(buf.getvalue())
    return Image.open(io.BytesIO(result)).convert("RGBA")

def optimize_for_gif(img):
    return img.convert("P", palette=Image.ADAPTIVE, colors=256)

def create_gif(images, duration):
    buf = io.BytesIO()
    images[0].save(
        buf,
        format="GIF",
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0,
        optimize=True
    )
    buf.seek(0)
    return buf

# ---------------- UI ----------------

uploaded_files = st.file_uploader(
    "Upload PNG / JPG images",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

st.subheader("Options")

make_gif = st.toggle(" Convert to GIF", value=True)
face_blur = st.toggle(" Face-Aware Background Blur")
ai_remove = st.toggle(" AI Background Removal")

image_size = st.slider(
    "Output Image Size (px)",
    min_value=256,
    max_value=512,
    value=320,
    step=32
)

blur_strength = st.slider(
    "Blur Strength",
    min_value=5,
    max_value=45,
    value=25,
    step=2
)

gif_duration = st.slider(
    "GIF Frame Duration (ms)",
    min_value=100,
    max_value=800,
    value=300,
    step=100
)

process = st.button("Process")

# ---------------- PROCESS ----------------

if process and uploaded_files:
    processed = []

    for file in uploaded_files:
        img = Image.open(file).convert("RGB")
        img = resize_image(img, image_size)

        if ai_remove:
            st.write("Removing background (AI)…")
            img = ai_background_removal(img)

        if face_blur:
            img = face_aware_blur(img, blur_strength)

        img = optimize_for_gif(img)
        processed.append(img)

    if make_gif and len(processed) > 1:
        gif = create_gif(processed, gif_duration)
        st.image(gif)
        st.download_button("⬇ Download GIF", gif, "output.gif", "image/gif")
    else:
        buf = io.BytesIO()
        processed[0].save(buf, format="GIF")
        buf.seek
