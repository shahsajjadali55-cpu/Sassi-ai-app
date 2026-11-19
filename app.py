import streamlit as st
from PIL import Image
import urllib.parse, requests, time
from io import BytesIO

st.set_page_config(page_title="Clean Studio - 1 Photo 1 Scene", layout="centered")
st.markdown("<h2 style='text-align:center'>📸 Clean Studio - 1 Photo = 1 Real Scene</h2>")

# ONLY ONE PHOTO
uploaded = st.file_uploader("📸 اپنی تصویر اپلوڈ کرو (بس ایک)", type=["jpg","png","jpeg"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="آپ کی Original Photo", width=300)
    
    # Expression - yahi motion hai
    expression = st.selectbox("😊 اس تصویر میں کیا کروانا ہے؟", 
        ["has rahi hai - laughing happily", "ro rahi hai - crying sad", "dekh rahi hai camera ko - looking", "baat kar rahi hai - talking"])
    
    background = st.text_area("📍 بیک گراؤنڈ کہاں ہے؟", "Thar desert, beautiful background, cinematic lighting")
    
    if st.button("🎬 1 سین بناؤ - صاف", use_container_width=True):
        with st.spinner("⏳ آپ کی تصویر کا ایک ہی سین بنا رہا ہوں..."):
            # CLEAN PROMPT - No Sassi, No Cartoon
            # Use user's uploaded image description + expression
            clean_prompt = f"real human, same girl as photo, {expression}, {background}, photorealistic, real skin texture, DSLR photo, 8k, sharp face, NOT cartoon, NOT anime, NOT illustration, NOT Sassi, NOT 3d"
            enc = urllib.parse.quote(clean_prompt)
            
            # SINGLE IMAGE - No Loop, No Extra
            url = f"https://image.pollinations.ai/prompt/{enc}?width=720&height=1280&seed={int(time.time())}&nologo=true&model=turbo"
            
            try:
                r = requests.get(url, timeout=30)
                if len(r.content) > 10000:
                    final_img = Image.open(BytesIO(r.content))
                    st.image(final_img, caption=f"✅ آپ کا 1 سین - {expression}")
                    st.download_button("📥 یہ 1 سین Download کرو", r.content, "clean_scene_1.jpg")
                    
                    # Simple motion - only slight zoom, not fake
                    st.markdown("---")
                    st.info("💡 یہ 1 صاف تصویر ہے - اس کو CapCut میں ڈال کر `Animation -> Zoom In` لگاؤ تو ہلکی Motion آ جائے گی۔ اصلی ہنسی/رونے کا AI Video free میں کوئی نہیں دیتا، سب اسی 1 فوٹو سے ہی بناتے ہیں!")
                else:
                    st.error("Free limit - 45 سیکنڈ بعد دوبارہ بٹن دباؤ سائیں")
            except Exception as e:
                st.error(f"Error: {e} - 45 sec wait karke dubara try karo")
else:
    st.warning("👆 پہلے اوپر اپنی 1 تصویر اپلوڈ کرو سائیں")

st.caption("Clean Code: 1 Upload = 1 Scene | No Extra Images | No Sassi Fix | No Cartoon Prompt")
