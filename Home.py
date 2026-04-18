import streamlit as st

# ✅ Page config (ONLY ONCE, TOP)
st.set_page_config(
    page_title="Nutri AI",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✅ Initialize objects
from utils.meal_generator import MealGenerator
from utils.nutrition_calculator import NutritionCalculator

if "meal_generator" not in st.session_state:
    st.session_state.meal_generator = MealGenerator()

if "calculator" not in st.session_state:
    st.session_state.calculator = NutritionCalculator()

# ✅ ALL CSS IN ONE PLACE
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #E8F5E8, #C8E6C9, #A5D6A7);
}

/* MAIN HEADER */
.main-header {
    font-family: 'Poppins', sans-serif;
    font-size: 4rem;
    font-weight: 700;
    color: #1B5E20;
    text-align: center;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.15);
}

/* SUBTEXT */
.subtext {
    text-align: center;
    font-size: 1.3rem;
    color: #2E7D32;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.1);
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(135deg, #4CAF50, #45a049);
    color: white;
    border-radius: 12px;
    padding: 0.7rem 2rem;
    font-weight: 600;
}

import streamlit as st

st.set_page_config(page_title="Nutri AI", layout="wide")

# ✅ SIDEBAR FIX
st.markdown("""
<style>

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.98) !important;
    border-radius: 20px !important;
    box-shadow: 0 20px 50px rgba(0,0,0,0.15) !important;
}

/* TEXT FIX */
[data-testid="stSidebar"] * {
    color: black !important;
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)

st.title("💪 Nutri AI")

# ✅ HEADER
st.markdown('<h1 class="main-header">💪 Nutri AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtext">Welcome to your AI Nutrition App 🚀</p>', unsafe_allow_html=True)

# ✅ SAMPLE CONTENT
st.markdown('<div class="card">', unsafe_allow_html=True)

st.write("### Enter your details")

age = st.number_input("Age")
weight = st.number_input("Weight")
goal = st.selectbox("Goal", ["Lose Weight", "Gain Muscle"])

if st.button("Generate Plan"):
    if goal == "Lose Weight":
        calories = weight * 20
    else:
        calories = weight * 30

    st.success(f"Recommended Calories: {calories}")

st.markdown('</div>', unsafe_allow_html=True)
# Your existing app code continues here...
# ... rest of your app.py code

import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict

# Initialize session state FIRST
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'calculator' not in st.session_state:
    st.session_state.calculator = None
if 'meal_generator' not in st.session_state:
    st.session_state.meal_generator = None



st.markdown("""
<style>
    .main-header {font-size: 3rem; color: #2E7D32; text-align: center; margin-bottom: 2rem;}
    .metric-card {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; border-radius: 10px; color: white;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🥗 Nutri AI</h1>', unsafe_allow_html=True)
st.markdown("### Your Personal Nutrition Coach")

# Import utils safely
try:
    from utils.nutrition_calculator import NutritionCalculator
    from utils.meal_generator import MealGenerator
    st.session_state.calculator = NutritionCalculator()
    st.session_state.meal_generator = MealGenerator()
except Exception as e:
    st.error(f"❌ Module loading error: {str(e)}")
    st.stop()

# Sidebar Profile
with st.sidebar:
    st.header("👤 Your Profile")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 18, 80, 25)
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        height = st.number_input("Height (cm)", 150, 200, 170)
        weight = st.number_input("Weight (kg)", 40, 150, 70)
    
    goal = st.selectbox("Goal", ["Weight Loss", "Weight Gain", "Muscle Gain"])
    activity = st.selectbox("Activity Level", 
                          ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
    
    if st.button("💾 Save Profile", use_container_width=True):
        st.session_state.user_profile = {
            'age': age, 'gender': gender, 'height': height, 
            'weight': weight, 'goal': goal, 'activity': activity
        }
        st.rerun()

# Show profile if exists
if st.session_state.user_profile:
    profile = st.session_state.user_profile
    
    # Calculate nutrition
    bmr = st.session_state.calculator.calculate_bmr(
        profile['age'], profile['weight'], profile['height'], profile['gender'].lower()
    )
    tdee = st.session_state.calculator.calculate_tdee(bmr, profile['activity'].lower())
    calories = st.session_state.calculator.get_calorie_target(tdee, profile['goal'].lower().replace(' ', '_'))
    macros = st.session_state.calculator.get_macros(calories, profile['goal'].lower().replace(' ', '_'))
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("BMR", f"{bmr:.0f} kcal")
    with col2: st.metric("TDEE", f"{tdee:.0f} kcal") 
    with col3: st.metric("Calories", f"{calories:.0f} kcal")
    with col4: st.metric("Protein", f"{macros['protein']:.0f}g")
    
    st.markdown("---")
    st.subheader("🚀 Quick Actions")
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🍽️ Generate Meal Plan", use_container_width=True):
            st.session_state.show_meal_plan = True
            st.rerun()
    with col_b:
        if st.button("💬 Chat with AI", use_container_width=True):
            st.session_state.show_chat = True
            st.rerun()
else:
    st.info("👈 **Complete your profile in the sidebar to get started!**")

# Show preview meal if calculated
if 'show_meal_plan' in st.session_state and st.session_state.show_meal_plan:
    st.session_state.current_page = "meal_planner"
    st.rerun()
