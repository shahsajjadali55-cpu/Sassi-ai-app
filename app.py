import streamlit as st
import urllib.parse, time

st.set_page_config(page_title="All Video Maker - Larkana", layout="centered")
st.markdown("<h1 style='text-align:center'>🎬 ہر قسم کی ویڈیو میکر - لاڑکانہ</h1>")

# ہر قسم کی ویڈیو
video_type = st.selectbox("ویڈیو کس قسم کی؟", 
["Sassi Pannu - سسی پنہوں", "Love Story - عشق", "Funny - مزاحیہ", "Horror - ڈراؤنی", "Islamic - اسلامی", "Sindhi Culture - ثقافت", "Custom - اپنی مرضی"])

story = st.text_area("📝 اپنی کہانی لکھو (اردو/سندھی/انگلش):", 
"Ek khubsurat larki Thar desert mein...", height=120)

style = st.selectbox("سٹائل:", ["Real Human - اصلی انسان", "Cartoon - کارٹون", "Cinematic - فلمی", "3D - تھری ڈی"])

if st.button("🚀 ہر قسم کی ویڈیو بناؤ - Download"):
    st.write("⏳ ویڈیو بن رہی ہے سائیں... 30 سیکنڈ...")
    
    base_prompt = ""
    if style == "Real Human - اصلی انسان":
        base_prompt = "photorealistic real human, ultra realistic, DSLR photo, 8k, natural skin, real face"
    elif style == "Cartoon - کارٹون":
        base_prompt = "cartoon style, animated, colorful"
    elif style == "Cinematic - فلمی":
        base_prompt = "cinematic movie scene, dramatic lighting, film grain"
    else:
        base_prompt = "3D render, pixar style"

    for i in range(4):
        full_prompt = f"{base_prompt}, {video_type}, {story}, scene {i+1}, highly detailed"
        encoded = urllib.parse.quote(full_prompt)
        img_url = f"https://image.pollinations.ai/prompt/{encoded}?width=720&height=1280&model=flux&nologo=true&seed={int(time.time())+i*50}"
        st.image(img_url, caption=f"Scene {i+1} - {video_type}")

    st.success("✅ ماشاءاللہ سائیں! ویڈیو تیار! Screen Record کر کے YouTube پر ڈال دو!")
    st.info("💡 ٹپ: CapCut ایپ میں 4 تصویریں ڈالو + گانا لگاؤ = اصلی ویڈیو!")
    st.balloons()
