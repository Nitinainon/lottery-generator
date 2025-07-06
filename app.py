import streamlit as st
import random
from datetime import datetime

# ตั้งค่าหน้าเว็บให้เหมาะกับมือถือ
st.set_page_config(page_title="🎯 สุ่มเลขหวย", layout="centered")

# --- DATA ---
# รายการหวย
lottery_list = [
    "นิเคอิเช้า", "จีนเช้า", "หุ้นฮั่งเส็งเช้า", "หุ้นไต้หวัน",
    "หุ้นเกาหลี", "หุ้นนิคเคอิบ่าย", "หุ้นจีนบ่าย", "หุ้นฮั่งเส็งบ่าย",
    "หุ้นสิงคโปร์", "หุ้นไทยเย็น", "หุ้นอินเดีย", "หุ้นอียิปต์"
]

# --- FUNCTIONS ---
# ฟังก์ชันสุ่มเลข
def generate_numbers():
    position = random.choice(["บน", "ล่าง"])
    # สุ่มเลข 2 ตัว 6 ชุด
    numbers = [f"{random.randint(0, 99):02d}" for _ in range(6)]
    return position, numbers

# เริ่มต้น session_state หากยังไม่มี
if "history" not in st.session_state:
    st.session_state.history = []
if "results" not in st.session_state:
    st.session_state.results = {}

# --- UI LAYOUT ---

# 1. ส่วนหัว (Header)
st.markdown("<h2 style='text-align: center;'>🎯 ระบบสุ่มเลขเด็ด</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>📅 {datetime.now().strftime('%d/%m/%Y')}</p>", unsafe_allow_html=True)
st.divider()

# 2. ส่วนสุ่มเลข (Lottery Selection)
st.markdown("#### เลือกหวยที่ต้องการสุ่ม")

# ใช้ st.selectbox สำหรับมือถือจะประหยัดพื้นที่และใช้ง่าย
selected_lottery = st.selectbox(
    "เลือกหวย:",
    lottery_list,
    label_visibility="collapsed" # ซ่อน label เพื่อความคลีน
)

# ปุ่มสุ่มเลขจะอยู่ตรงกลางและมีขนาดใหญ่
if st.button("🎰 สุ่มเลขเลย!", use_container_width=True, type="primary"):
    pos, nums = generate_numbers()
    
    # เก็บผลลัพธ์ล่าสุดของหวยที่เลือก
    st.session_state.results[selected_lottery] = (pos, nums)
    
    # สร้างข้อความสำหรับเก็บในประวัติ
    result_text = f"**{selected_lottery}** | {pos}: **{', '.join(nums)}**"
    timestamp = datetime.now().strftime('%H:%M:%S')
    st.session_state.history.insert(0, f"🕒 {timestamp} - {result_text}")

# 3. แสดงผลลัพธ์ล่าสุด (Latest Result Display)
if selected_lottery in st.session_state.results:
    pos, nums = st.session_state.results[selected_lottery]
    
    st.markdown("---")
    st.markdown(f"#### ผลล่าสุดของ **{selected_lottery}**")
    
    # จัดคอลัมน์แสดงผลให้สวยงาม
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric(label="ตำแหน่ง", value=pos)
    with col2:
        # แสดงตัวเลขในรูปแบบที่อ่านง่าย
        st.markdown(f"**เลขเด็ด:**")
        st.markdown(f"<h3 style='color: #FF4B4B;'>{', '.join(nums)}</h3>", unsafe_allow_html=True)


st.divider()

# 4. ส่วนประวัติ (History Section)
with st.expander("📜 ดูประวัติการสุ่มทั้งหมด", expanded=True):
    if st.session_state.history:
        # ปุ่มล้างประวัติ
        if st.button("🗑️ ล้างประวัติ", use_container_width=True):
            st.session_state.history = []
            st.rerun() # สั่งให้รีเฟรชหน้าจอทันที

        st.markdown("---")
        # แสดงประวัติ
        for entry in st.session_state.history:
            st.info(entry)
    else:
        st.write("ยังไม่มีการสุ่มเลข")