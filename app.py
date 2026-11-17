import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import time
from urllib.parse import quote

st.set_page_config(page_title="Sassi AI Real Video", layout="centered")
st.markdown("<h1 style='text-align:center;color:#ff6a00;'>🎬 Sassi - Real AI Video</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>سائیں اپنا YouTube جیسا ویڈیو میکر!</p>", unsafe_allow_html=True)

story = st.text_area("📝 کہانی لکھو:", "Sassi ne Thar mein Panhun ko talash kiya, ret ke teelay par royi, ishq amar ho gaya")

if st.button("🚀 اصلی ویڈیو بناؤ - YouTube Style"):
    if not story:
        st.warning("کہانی تو لکھو سائیں!")
    else:
        with st.spinner("AI YouTube جیسی ویڈیو بنا رہا ہے..."):
            prompts = [
                f"Sindhi beautiful girl Sassi running in Thar desert sandstorm cinematic 8k {story[:40]}",
                f"Sindhi girl Sassi crying searching love desert dunes sunset cinematic",
                f"Sassi and Panhun romantic meeting Sindhi palace happy ending cinematic"
            ]
            
            for i, p in enumerate(prompts):
                try:
                    url = f"https://image.pollinations.ai/prompt/{quote(p)}?width=720&height=1280&nologo=true&seed={i+10}"
                    r = requests.get(url, timeout=30)
                    img = Image.open(BytesIO(r.content))
                    st.image(img, caption=f"Scene {i+1} - {story[:30]}", use_container_width=True)
                    st.markdown(f"**Scene {i+1}:** {story}")
                except Exception as e:
                    st.error(f"Scene {i+1} error: {e}")
                time.sleep(1)
            
            st.success("ماشاءاللہ! اصلی ویڈیو تیار ہے سائیں! 👇")
            st.balloons()
            st.info("سائیں اب Screen Record کر لو - یہی آپ کی YouTube ویڈیو ہے! CapCut میں گانا لگا دو - تیار!")
