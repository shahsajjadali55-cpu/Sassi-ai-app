import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sassi AI Video Maker", page_icon="🔥", layout="centered")

st.markdown("<h1 style='color:#ff6a00; text-align:center;'>🔥 Sassi Panhun AI App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>سائیں اپنا AI ویڈیو میکر - Nawabshah</p>", unsafe_allow_html=True)

story = st.text_area("📜 کہانی لکھو:", "Sassi ne Thar mein Panhun ko talash kiya, rait ke teelay par uski yaad mein royi...")

files = st.file_uploader("📸 اپنی 3-4 تصویریں ڈالو:", accept_multiple_files=True, type=['jpg','jpeg','png'])

if st.button("🚀 AI ویڈیو بناؤ"):
    if not files or len(files) < 2:
        st.warning("سائیں کم از کم 2 تصویریں ڈالو!")
    else:
        st.success("ماشاءاللہ! آپ کی AI ویڈیو تیار ہے 👇")
        st.balloons()
        for i, f in enumerate(files):
            img = Image.open(f)
            st.image(img, use_container_width=True)
            st.markdown(f"**Scene {i+1}:** {story}")
            st.markdown("---")
        st.info("📥 اسکرین ریکارڈ کر لو - یہی آپ کی AI ویڈیو ہے!")

st.markdown("---")
st.caption("Made with ❤️ by Sassi AI - Nawabshah Sindh")
