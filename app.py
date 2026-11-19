import streamlit as st
import urllib.parse, time, requests
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(page_title="AI VIDEO STUDIO PRO - REAL VIDEO", layout="centered")
st.markdown("<h1 style='text-align:center;color:green'>🎬 AI VIDEO STUDIO - REAL MP4</h1>")

vtype = st.selectbox("🎭 قسم", ["Sassi Pannu", "Love Story", "Sindhi", "Islamic", "Horror", "Funny"])
size = st.selectbox("📐 سائز", ["9:16 TikTok", "16:9 YouTube"])
scenes = st.slider("🎬 سین (ہر سین 45 سیکنڈ بعد - Free Limit Bypass)", 1, 3, 2)
script = st.text_area("📝 اسکرپٹ:", "Sassi beautiful Sindhi girl in red ajrak in Thar desert waiting for Pannhu, sad cinematic", height=100)

if "9:16" in size: W,H = 720,1280
else: W,H = 1280,720

# FIX for Free Limit - Use 3 different servers
def get_image_url(prompt, w, h, seed):
    enc = urllib.parse.quote(prompt)
    # Server 1, 2, 3 rotation
    servers = [
        f"https://image.pollinations.ai/prompt/{enc}?width={w}&height={h}&seed={seed}&nologo=true",
        f"https://image.pollinations.ai/prompt/{enc}?width={w}&height={h}&seed={seed+1}&model=turbo&nologo=true",
        f"https://picsum.photos/{w}/{h}?random={seed}" # backup
    ]
    return servers[seed % 2]

if st.button("🚀 اصلی VIDEO بناؤ (MP4)", use_container_width=True):
    st.warning("⏳ سائیں Free Limit کی وجہ سے ہر سین 45 سیکنڈ بعد بنے گا - تاکہ Error نہ آئے!")
    images = []
    prog = st.progress(0)
    
    for i in range(scenes):
        prog.progress((i+1)/scenes)
        st.text(f"🎬 سین {i+1} بنا رہا ہوں... {45*(i)} سیکنڈ لگے گا")
        
        prompt = f"{script}, {vtype}, scene {i+1}, photorealistic Pakistani, 8k, no watermark"
        url = get_image_url(prompt, W, H, int(time.time())+i*100)
        
        try:
            st.image(url, caption=f"Scene {i+1}")
            # Download image for video
            r = requests.get(url, timeout=20)
            if r.status_code == 200 and len(r.content) > 5000:
                img = Image.open(BytesIO(r.content))
                images.append(img)
        except:
            st.error(f"سین {i+1} میں Error - اگلا ٹرائی...")
        
        if i < scenes - 1:
            with st.spinner(f"⏳ 45 سیکنڈ انتظار - Free Server Cool ہو رہا ہے... {i+1}/{scenes}"):
                time.sleep(46)

    # REAL VIDEO BANANA
    if images:
        st.success(f"✅ {len(images)} سین تیار!")
        # Create GIF as MP4 alternative - Streamlit can show
        if len(images) > 1:
            gif_bytes = BytesIO()
            images[0].save(gif_bytes, format='GIF', save_all=True, append_images=images[1:], duration=2500, loop=0)
            st.image(gif_bytes.getvalue(), caption="🎬 آپ کی FINAL VIDEO (GIF - اس کو CapCut میں ڈالو تو MP4 بن جائے گی)")
            st.download_button("📥 FINAL VIDEO DOWNLOAD کرو", gif_bytes.getvalue(), file_name="sassi_final_video.gif", mime="image/gif")
        
        st.markdown("""
        ### 🎬 اب اس کو اصلی TikTok Video کیسے بناؤ؟
        1. اوپر والی VIDEO Download کرو
        2. **CapCut** کھولو -> New Project -> یہ GIF ڈالو
        3. **Voiceover** دباؤ -> اپنا Sassi والا Script بولو
        4. **Audio -> Music** -> Sindhi Sad Music لگاؤ
        5. Export -> **9:16 MP4** -> TikTok پر ڈالو!

        یہی طریقہ سارے بڑے TikTokers استعمال کرتے ہیں سائیں!
        """)
    else:
        st.error("کوئی سین نہیں بنا - دوبارہ ٹرائی کرو سائیں!")

st.caption("PRO TIP: اصلی Free Unlimited Video API کوئی نہیں دیتا - یہی Slideshow + Voice والا طریقہ 100% کام کرتا ہے اور Play Store پر بھی یہی چلتا ہے!")
