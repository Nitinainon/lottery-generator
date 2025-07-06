import streamlit as st
import random
from datetime import datetime
import pytz # เพิ่ม library สำหรับจัดการโซนเวลา

# --- การตั้งค่าพื้นฐาน ---
st.set_page_config(page_title="🎯 สุ่มเลขเด็ด", layout="centered")

# กำหนดโซนเวลาของประเทศไทย
BKK_TIMEZONE = pytz.timezone("Asia/Bangkok")

# --- DATA ---
lottery_list = [
    "นิเคอิเช้า", "จีนเช้า", "หุ้นฮั่งเส็งเช้า", "หุ้นไต้หวัน",
    "หุ้นเกาหลี", "หุ้นนิคเคอิบ่าย", "หุ้นจีนบ่าย", "หุ้นฮั่งเส็งบ่าย",
    "หุ้นสิงคโปร์", "หุ้นไทยเย็น", "หุ้นอินเดีย", "หุ้นอียิปต์"
]

# --- FUNCTIONS ---
def generate_numbers():
    position = random.choice(["บน", "ล่าง"])
    numbers = [f"{random.randint(0, 99):02d}" for _ in range(6)]
    return position, numbers

# --- UI LAYOUT ---

# 1. ส่วนหัว (Header)
st.markdown("<h2 style='text-align: center;'>🎯 ระบบสุ่มเลขเด็ด</h2>", unsafe_allow_html=True)
# แปลงเวลาให้เป็นเวลาไทยก่อนแสดงผล
current_time_bkk = datetime.now(BKK_TIMEZONE)
st.markdown(f"<p style='text-align: center;'>📅 {current_time_bkk.strftime('%d/%m/%Y')}</p>", unsafe_allow_html=True)
st.divider()

# 2. ส่วนสุ่มเลข (Lottery Selection)
st.markdown("#### เลือกหวยที่ต้องการสุ่ม")

selected_lottery = st.selectbox(
    "เลือกหวย:",
    lottery_list,
    label_visibility="collapsed"
)

if st.button("🎰 สุ่มเลขเลย!", use_container_width=True, type="primary"):
    pos, nums = generate_numbers()
    
    # ใช้ st.session_state ในการเก็บผลลัพธ์ชั่วคราว
    st.session_state.temp_result = (pos, nums)
    
    # สร้างข้อความสำหรับเก็บในประวัติ
    result_text = f"**{selected_lottery}** | {pos}: **{', '.join(nums)}**"
    timestamp = datetime.now(BKK_TIMEZONE).strftime('%H:%M:%S')
    
    # **[แก้ไข]** เก็บประวัติลงใน st.cache_data แทน session_state
    if 'history_log' not in st.session_state:
        st.session_state.history_log = []
    st.session_state.history_log.insert(0, f"🕒 {timestamp} - {result_text}")


# 3. แสดงผลลัพธ์ล่าสุด (Latest Result Display)
if 'temp_result' in st.session_state:
    pos, nums = st.session_state.temp_result
    
    st.markdown("---")
    st.markdown(f"#### ผลล่าสุดของ **{selected_lottery}**")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric(label="ตำแหน่ง", value=pos)
    with col2:
        st.markdown(f"**เลขเด็ด:**")
        st.markdown(f"<h3 style='color: #FF4B4B;'>{', '.join(nums)}</h3>", unsafe_allow_html=True)

st.divider()

# 4. ส่วนประวัติ (History Section)
with st.expander("📜 ดูประวัติการสุ่มทั้งหมด", expanded=True):
    # **[แก้ไข]** ดึงข้อมูลประวัติจาก st.session_state.history_log
    if 'history_log' in st.session_state and st.session_state.history_log:
        if st.button("🗑️ ล้างประวัติ", use_container_width=True):
            st.session_state.history_log = []
            st.rerun()

        st.markdown("---")
        for entry in st.session_state.history_log:
            st.info(entry)
    else:
        st.write("ยังไม่มีการสุ่มเลข")