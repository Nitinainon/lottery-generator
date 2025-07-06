import streamlit as st
import random
from datetime import datetime

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

# -----------------------------
st.set_page_config(page_title="ระบบสุ่มเลขหวย", layout="centered")
st.title("🎯 ระบบสุ่มเลขหวย (00–99)")
st.markdown(f"📅 วันที่: **{datetime.now().strftime('%d/%m/%Y')}**")

st.markdown("---")

# ปุ่มสุ่มแยกกัน 12 ปุ่ม
for lottery in lottery_list:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader(f"📌 {lottery}")
    with col2:
        if st.button(f"สุ่มเลข - {lottery}"):
            pos, nums = generate_numbers()
            st.success(f"ตำแหน่ง: **{pos}** | เลขที่สุ่ม: **{', '.join(nums)}**")
