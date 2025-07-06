import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="🎯 ระบบสุ่มเลขหวย", layout="centered")

# รายการหวย
lottery_list = [
    "นิเคอิเช้า", "จีนเช้า", "หุ้นฮั่งเส็งเช้า", "หุ้นไต้หวัน",
    "หุ้นเกาหลี", "หุ้นนิคเคอิบ่าย", "หุ้นจีนบ่าย", "หุ้นฮั่งเส็งบ่าย",
    "หุ้นสิงคโปร์", "หุ้นไทยเย็น", "หุ้นอินเดีย", "หุ้นอียิปต์"
]

# ฟังก์ชันสุ่มเลข
def generate_numbers():
    position = random.choice(["บน", "ล่าง"])
    numbers = random.sample(range(100), 6)
    numbers_str = [f"{n:02d}" for n in numbers]
    return position, numbers_str

# เริ่มต้น session_state
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
st.markdown("## 🎯 ระบบสุ่มเลขหวย (00–99)")
st.markdown(f"📅 วันที่: **{datetime.now().strftime('%d/%m/%Y')}**")

st.divider()

# ปุ่มล้างประวัติ
col_clear, _ = st.columns([1, 4])
with col_clear:
    if st.button("🗑️ ล้างประวัติทั้งหมด", use_container_width=True):
        st.session_state.history = []
        st.success("ล้างประวัติเรียบร้อยแล้ว!")

st.divider()

# UI แบบทันสมัย แยกหวย
for lottery in lottery_list:
    with st.container():
        with st.expander(f"📌 {lottery}", expanded=False):
            col1, col2 = st.columns([3, 1])
            with col2:
                if st.button(f"สุ่มเลข", key=lottery):
                    pos, nums = generate_numbers()
                    result_text = f"🎲 {lottery} | ตำแหน่ง: **{pos}** | เลข: **{', '.join(nums)}**"
                    st.session_state.history.insert(0, result_text)
                    st.success(result_text)

st.divider()

# แสดงประวัติ
st.markdown("### 📜 ประวัติการสุ่มทั้งหมด")
if st.session_state.history:
    for i, entry in enumerate(st.session_state.history):
        with st.container():
            st.markdown(f"{i+1}. {entry}")
else:
    st.info("ยังไม่มีการสุ่มเลขในรอบนี้")
