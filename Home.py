import streamlit as st
import streamlit as st

# Initialize objects (FIX for deployment)
from utils.meal_generator import MealGenerator
from utils.nutrition_calculator import NutritionCalculator

if "meal_generator" not in st.session_state:
    st.session_state.meal_generator = MealGenerator()

if "calculator" not in st.session_state:
    st.session_state.calculator = NutritionCalculator()

st.title("💪 Nutri AI")
st.write("Welcome to your AI Nutrition App 🚀")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

/* NEW CLEAN GREEN BACKGROUND - PERFECT FOR FONTS */
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #E8F5E8 0%, #C8E6C9 50%, #A5D6A7 100%) !important;
    background-attachment: fixed !important;
}

/* KEEP ALL OTHER STYLES - JUST BACKGROUND CHANGED */
.stApp {
    background: rgba(255, 255, 255, 0.98) !important;
    backdrop-filter: blur(12px) !important;
    border-radius: 25px !important;
    box-shadow: 0 25px 60px rgba(0,0,0,0.15) !important;
    margin: 1.2rem !important;
}

.main-header {
    font-family: 'Poppins', sans-serif !important;
    font-size: 4rem !important;
    font-weight: 700 !important;
    color: #1B5E20 !important;
    text-align: center !important;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.15) !important;
}

/* ALL OTHER STYLES REMAIN SAME */
.metric-card, .stMetric {
    background: rgba(255, 255, 255, 1) !important;
    border-radius: 20px !important;
    border: 2px solid #E8F5E8 !important;
    box-shadow: 0 15px 40px rgba(0,0,0,0.1) !important;
    padding: 1.8rem !important;
}

.stMetric > label {
    color: #2E7D32 !important;
    font-weight: 600 !important;
    font-size: 1.2rem !important;
}

.stMetric > div > div {
    color: #1B5E20 !important;
    font-size: 2.8rem !important;
    font-weight: 700 !important;
}

/* BUTTONS */
.stButton > button {
    background: linear-gradient(135deg, #4CAF50, #45a049) !important;
    color: white !important;
    border-radius: 15px !important;
    padding: 1rem 2.5rem !important;
    font-weight: 600 !important;
    box-shadow: 0 10px 30px rgba(76,175,80,0.4) !important;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.98) !important;
    border-radius: 20px !important;
    box-shadow: 0 20px 50px rgba(0,0,0,0.15) !important;
}
</style>
""", unsafe_allow_html=True)
# Your existing app code continues here...

# Rest of your app code...

# STUNNING CSS + BACKGROUNDS
st.set_page_config(
    page_title="Nutri AI", 
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# COMPLETE PROFESSIONAL CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .main-header {
        font-family: 'Poppins', sans-serif;
        font-size: 4rem !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.95), rgba(255,255,255,0.85));
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.5rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 30px 60px rgba(0,0,0,0.15);
    }
    
    .stMetric > label {
        font-weight: 600 !important;
        color: #2E7D32 !important;
        font-size: 1.1rem !important;
    }
    
    .stMetric > div > div {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: #1B5E20 !important;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%) !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border-radius: 15px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.6) !important;
    }
    
    /* Chat bubbles */
    .stChatMessage {
        background: rgba(255,255,255,0.9) !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
    }
    
    /* Tables */
    .dataframe {
        border-radius: 15px !important;
        overflow: hidden !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
    }
    
    /* Expanders */
    .stExpander {
        background: linear-gradient(145deg, #ffffff, #f8f9fa) !important;
        border-radius: 15px !important;
        border: 2px solid #e9ecef !important;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08) !important;
    }
</style>
""", unsafe_allow_html=True)

# Animated Background
st.markdown("""
<div style="
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
">
</div>
<style>
@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
</style>
""", unsafe_allow_html=True)

# Glassmorphism Main Container
st.markdown("""
<div style="
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    border-radius: 30px;
    padding: 2rem;
    margin: 1rem;
    box-shadow: 0 25px 50px rgba(0,0,0,0.15);
    border: 1px solid rgba(255,255,255,0.3);
">
""", unsafe_allow_html=True)

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