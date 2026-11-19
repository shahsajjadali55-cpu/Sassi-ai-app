import streamlit as st
import urllib.parse, time, requests

st.set_page_config(page_title="AI VIDEO STUDIO PRO", layout="wide")
st.markdown("<h1 style='text-align:center;color:green'>🎬 AI VIDEO STUDIO PRO - Unlimited No Watermark</h1>")

c1,c2,c3,c4 = st.columns(4)
with c1: vtype = st.selectbox("قسم", ["Sassi Pannu","Love Story","Sindhi","Islamic","Horror","Funny","Custom"])
with c2: size = st.selectbox("سائز", ["9:16 TikTok","16:9 YouTube","1:1 Insta","4:5 FB"])
with c3: qual = st.selectbox("کوالٹی", ["HD","Full HD","4K"])
with c4: scenes = st.slider("سین", 1, 10, 4)

script = st.text_area("📝 اسکرپٹ لکھو - کردار خود بنے گا:", "Sassi 20 year old Sindhi girl in red ajrak, Thar desert, waiting for Panhun, sad, cinematic", height=130)

if "9:16" in size: W,H=720,1280
elif "16:9" in size: W,H=1280,720
elif "1:1" in size: W,H=1024,1024
else: W,H=864,1080

if st.button("🚀 PRO VIDEO BANAO - NO WATERMARK UNLIMITED", use_container_width=True):
    prog = st.progress(0)
    for i in range(scenes):
        prog.progress((i+1)/scenes)
        prompt = f"{script}, {vtype}, scene {i+1}, photorealistic real human Pakistani, 8k, no watermark, no logo, no text"
        enc = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{enc}?width={W}&height={H}&seed={int(time.time())+i*99}&nologo=true&nofeed=true&model=flux"
        st.image(url, caption=f"Scene {i+1} - {size} - No Watermark")
        try:
            r = requests.get(url, timeout=15)
            st.download_button(f"📥 Download Scene {i+1}", r.content, f"pro_scene_{i+1}.jpg", key=f"{i}{time.time()}")
        except: pass
        if i < scenes-1: time.sleep(6)
    st.success("✅ تیار سائیں! Download کر لو - No Watermark!")
    st.balloons()
