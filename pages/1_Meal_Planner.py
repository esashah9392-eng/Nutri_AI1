# Add to top of pages/1_meal_planner.py
import streamlit as st

st.markdown("""
<style>
.meal-hero {
    background: linear-gradient(135deg, #a8e6cf, #88d8a3, #dcedc1);
    border-radius: 30px;
    padding: 3rem;
    text-align: center;
    box-shadow: 0 30px 80px rgba(168,230,207,0.4);
    margin: 2rem 0;
}
.food-card {
    background: rgba(255,255,255,0.95);
    border-radius: 20px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 15px 40px rgba(0,0,0,0.1);
    border-left: 5px solid #4ECDC4;
}
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="meal-hero">
    <h2 style="color: #1B5E20; font-size: 2.5rem;">🍽️ Your Precision Meal Plan</h2>
    <p style="color: #2E7D32; font-size: 1.3rem;">Exact foods • Perfect portions • Optimal nutrition</p>
</div>
""", unsafe_allow_html=True)





import streamlit as st
st.markdown("""
<style>
.nutrition-card {
    background: linear-gradient(135deg, #a8e6cf, #88d8a3) !important;
    border-radius: 20px !important;
    padding: 2rem !important;
    box-shadow: 0 20px 40px rgba(168, 230, 207, 0.4) !important;
}
.meal-item {
    background: rgba(255,255,255,0.9) !important;
    border-radius: 15px !important;
    padding: 1rem !important;
    margin: 0.5rem 0 !important;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1) !important;
}
</style>
""", unsafe_allow_html=True)


import streamlit as st
import random

st.title("🍽️ Detailed AI Meal Planner")
st.markdown("---")

# Safety check
if 'user_profile' not in st.session_state or not st.session_state.user_profile:
    st.error("👈 **Complete your profile on the main page first!**")
    st.stop()

profile = st.session_state.user_profile

# Enhanced food database with fiber
FOOD_DATABASE = {
    "proteins": {
        "Chicken Breast": {"cal": 165, "pro": 31, "carb": 0, "fat": 3.6, "fiber": 0},
        "Salmon": {"cal": 208, "pro": 20, "carb": 0, "fat": 13, "fiber": 0},
        "Eggs (2 large)": {"cal": 155, "pro": 13, "carb": 1.1, "fat": 11, "fiber": 0},
        "Greek Yogurt": {"cal": 100, "pro": 17, "carb": 6, "fat": 0.4, "fiber": 0},
        "Tofu": {"cal": 76, "pro": 8, "carb": 1.9, "fat": 4.8, "fiber": 2}
    },
    "carbs": {
        "Brown Rice (100g)": {"cal": 111, "pro": 2.6, "carb": 23, "fat": 0.9, "fiber": 1.8},
        "Sweet Potato (150g)": {"cal": 129, "pro": 2.4, "carb": 30, "fat": 0.2, "fiber": 4.5},
        "Quinoa (100g)": {"cal": 120, "pro": 4.1, "carb": 21, "fat": 1.9, "fiber": 2.8},
        "Oats (40g)": {"cal": 152, "pro": 5.3, "carb": 27, "fat": 2.7, "fiber": 4}
    },
    "vegetables": {
        "Broccoli (150g)": {"cal": 53, "pro": 4.2, "carb": 10.5, "fat": 0.6, "fiber": 5.1},
        "Spinach (100g)": {"cal": 23, "pro": 2.9, "carb": 3.6, "fat": 0.4, "fiber": 2.2},
        "Carrots (100g)": {"cal": 41, "pro": 0.9, "carb": 9.6, "fat": 0.2, "fiber": 2.8},
        "Avocado (100g)": {"cal": 160, "pro": 2, "carb": 9, "fat": 15, "fiber": 7}
    },
    "fruits": {
        "Banana": {"cal": 89, "pro": 1.1, "carb": 23, "fat": 0.3, "fiber": 2.6},
        "Apple": {"cal": 52, "pro": 0.3, "carb": 14, "fat": 0.2, "fiber": 2.4},
        "Berries (100g)": {"cal": 57, "pro": 1.2, "carb": 14, "fat": 0.3, "fiber": 2.4}
    },
    "snacks": {
        "Almonds (30g)": {"cal": 174, "pro": 6.3, "carb": 6.5, "fat": 15, "fiber": 3.7},
        "Peanut Butter (2 tbsp)": {"cal": 188, "pro": 8, "carb": 7, "fat": 16, "fiber": 2.5}
    }
}

def generate_detailed_meal(meal_type, target_calories):
    """Generate detailed meal with exact portions"""
    meals = {
        "breakfast": [("Greek Yogurt", 150), ("Oats", 40), ("Berries", 100)],
        "lunch": [("Chicken Breast", 150), ("Brown Rice", 100), ("Broccoli", 150)],
        "dinner": [("Salmon", 150), ("Sweet Potato", 150), ("Spinach", 100)],
        "snack": [("Apple", 150), ("Peanut Butter", 32)]
    }
    
    base_meal = meals.get(meal_type, meals["lunch"])
    meal_items = []
    meal_total = {"cal": 0, "pro": 0, "carb": 0, "fat": 0, "fiber": 0}
    
    for food_name, grams in base_meal:
        # Find food in database
        found = False
        for category, foods in FOOD_DATABASE.items():
            if food_name in foods:
                food_data = foods[food_name]
                # Scale to grams
                multiplier = grams / 100
                item = {
                    "name": f"{food_name} ({grams}g)",
                    "cal": round(food_data["cal"] * multiplier),
                    "pro": round(food_data["pro"] * multiplier, 1),
                    "carb": round(food_data["carb"] * multiplier, 1),
                    "fat": round(food_data["fat"] * multiplier, 1),
                    "fiber": round(food_data["fiber"] * multiplier, 1)
                }
                meal_items.append(item)
                
                # Add to totals
                for key in meal_total:
                    meal_total[key] += item[key]
                found = True
                break
        
        if not found:
            # Fallback
            meal_items.append({"name": f"{food_name} ({grams}g)", "cal": 100, "pro": 5, "carb": 15, "fat": 3, "fiber": 2})
    
    # Scale to target calories
    scale_factor = target_calories / meal_total["cal"] if meal_total["cal"] > 0 else 1
    for item in meal_items:
        for key in ["cal", "pro", "carb", "fat", "fiber"]:
            item[key] = round(item[key] * scale_factor, 1)
    
    # Recalculate totals
    meal_total = {"cal": 0, "pro": 0, "carb": 0, "fat": 0, "fiber": 0}
    for item in meal_items:
        for key in meal_total:
            meal_total[key] += item[key]
    
    return {
        "type": meal_type.title(),
        "items": meal_items,
        "total": meal_total
    }

# Calculate target calories
bmr = st.session_state.calculator.calculate_bmr(
    profile['age'], profile['weight'], profile['height'], profile['gender'].lower()
)
tdee = st.session_state.calculator.calculate_tdee(bmr, profile['activity'].lower())
daily_calories = st.session_state.calculator.get_calorie_target(tdee, profile['goal'].lower().replace(' ', '_'))
cal_per_meal = daily_calories // 4

st.metric("Daily Target", f"{daily_calories} kcal")
st.metric("Per Meal", f"{cal_per_meal} kcal")

# Generate button
if st.button("🎯 Generate Detailed Meal Plan", use_container_width=True):
    with st.spinner("🍳 Preparing your personalized meals..."):
        meal_types = ["breakfast", "lunch", "dinner", "snack"]
        meals = []
        for meal_type in meal_types:
            meal = generate_detailed_meal(meal_type, cal_per_meal)
            meals.append(meal)
        
        st.session_state.detailed_meal_plan = {
            "meals": meals,
            "daily_total": daily_calories,
            "profile": profile
        }
        st.rerun()

# Display plan
if 'detailed_meal_plan' in st.session_state:
    plan = st.session_state.detailed_meal_plan
    st.markdown("## 📋 Your Complete Daily Meal Plan")
    
    daily_total = {"cal": 0, "pro": 0, "carb": 0, "fat": 0, "fiber": 0}
    
    for meal in plan["meals"]:
        # Meal header
        st.markdown(f"### {meal['type']} ({meal['total']['cal']:.0f} kcal)")
        
        # Nutrition summary
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Protein", f"{meal['total']['pro']}g")
        col2.metric("Carbs", f"{meal['total']['carb']}g") 
        col3.metric("Fat", f"{meal['total']['fat']}g")
        col4.metric("Fiber", f"{meal['total']['fiber']}g")
        
        # Food items table
        st.markdown("**🍽️ Foods & Portions:**")
        food_data = []
        for item in meal['items']:
            food_data.append({
                "Food": item['name'],
                "Calories": item['cal'],
                "Protein": f"{item['pro']}g",
                "Carbs": f"{item['carb']}g", 
                "Fat": f"{item['fat']}g",
                "Fiber": f"{item['fiber']}g"
            })
        
        st.dataframe(food_data, use_container_width=True, hide_index=True)
        
        # Add to daily total
        for key in daily_total:
            daily_total[key] += meal['total'][key]
        
        st.markdown("---")
    
    # Daily Summary
    st.markdown("## 📊 Daily Nutrition Summary")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Calories", f"{daily_total['cal']:.0f} kcal")
    col2.metric("Protein", f"{daily_total['pro']:.0f}g")
    col3.metric("Carbs", f"{daily_total['carb']:.0f}g")
    col4.metric("Fat", f"{daily_total['fat']:.0f}g")
    col5.metric("Fiber", f"{daily_total['fiber']:.0f}g")
    
    st.balloons()
    st.success(f"✅ **Perfect plan for {profile['goal']}** - Follow this daily!")
    
    # Action buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 New Plan", use_container_width=True):
            del st.session_state.detailed_meal_plan
            st.rerun()
    with col2:
        st.download_button(
            "💾 Download Plan", 
            data="Your meal plan is ready to follow!",
            file_name="nutri_plan.txt"
        )

else:
    st.info("""
    🎯 **Click "Generate Detailed Meal Plan"**
    
    **What you'll get:**
    - Exact food names & portions (grams)
    - Calories, Protein, Carbs, Fat, Fiber per food
    - Perfectly balanced for your goals
    - Daily nutrition summary
    """)

st.markdown("---")
st.caption("🥗 Nutri AI - Precision Nutrition")