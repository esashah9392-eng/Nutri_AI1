import streamlit as st
import os
from dotenv import load_dotenv



st.header("App Preferences")
theme = st.selectbox("Theme", ["Light", "Dark"])
unit_system = st.selectbox("Unit System", ["Metric", "Imperial"])

if st.button("💾 Save Preferences"):
    st.success("✅ Preferences saved!")

st.header("📊 Data Export")
if st.button("📥 Export Meal History"):
    st.info("Coming soon...")

st.header("ℹ️ About")
st.markdown("""
**Nutri AI** is your personal nutrition coach powered by: SYED ESSA SHAH
- **OpenAI GPT** for smart chaT
- **Nutrition Database** for accurate meal planning

**Version 1.0** | **Made with ❤️ for health**
""")