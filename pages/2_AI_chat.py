import streamlit as st
# Subtle chat overlay
st.markdown("""
<style>
.chat-hero {
    background: linear-gradient(135deg, rgba(78,205,196,0.1), rgba(255,107,107,0.1));
    border-radius: 25px;
    padding: 2rem;
    text-align: center;
    margin: 2rem 0;
    border: 1px solid rgba(78,205,196,0.3);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="chat-hero">
    <h2 style="color: #2E7D32;">🤖 Smart Nutrition Coach</h2>
    <p style="color: #1B5E20;">AI analyzes your meals • Perfect suggestions</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<style>
.chat-bubble {
    background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.9)) !important;
    backdrop-filter: blur(15px) !important;
    border-radius: 25px !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1) !important;
    padding: 1.5rem !important;
    margin: 1rem 0 !important;
}
</style>
""", unsafe_allow_html=True)



import streamlit as st
import random

st.title("💬 Smart Nutrition Coach")
st.markdown("### Tell me what you ate - I'll analyze & suggest next!")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "profile" not in st.session_state:
    st.session_state.profile = st.session_state.user_profile if st.session_state.get('user_profile') else {}

# Nutrition analysis rules
NUTRITION_RULES = {
    "high_protein": ["chicken", "egg", "yogurt", "tofu", "salmon", "tuna"],
    "high_carb": ["rice", "bread", "pasta", "potato", "oats"],
    "high_fat": ["avocado", "nuts", "peanut butter", "cheese", "oil"],
    "veggies": ["broccoli", "spinach", "carrot", "salad", "lettuce"],
    "fruits": ["banana", "apple", "berries", "orange"]
}

def analyze_food(user_input):
    """Smart food analysis without ML"""
    user_lower = user_input.lower()
    
    feedback = "Great choice! "
    suggestions = []
    goal = st.session_state.profile.get('goal', 'balanced').lower()
    
    # Protein check
    has_protein = any(word in user_lower for word in NUTRITION_RULES["high_protein"])
    if has_protein:
        feedback += "✅ Excellent protein source! "
    else:
        suggestions.append("• Add **chicken/eggs/yogurt** for protein")
    
    # Carb check
    has_carb = any(word in user_lower for word in NUTRITION_RULES["high_carb"])
    if has_carb:
        feedback += "🍚 Good energy source! "
    else:
        suggestions.append("• Add **brown rice/quinoa/oats** for energy")
    
    # Veggie check
    has_veggie = any(word in user_lower for word in NUTRITION_RULES["veggies"])
    if has_veggie:
        feedback += "🥬 Perfect veggies! "
    else:
        suggestions.append("• Add **broccoli/spinach** for fiber & vitamins")
    
    # Goal-specific advice
    if "loss" in goal:
        feedback += "💪 Keep portions moderate for weight loss. "
        suggestions.append("• Next: **salad + lean protein**")
    elif "gain" in goal:
        feedback += "📈 Add healthy fats for weight gain! "
        suggestions.append("• Next: **avocado + nuts**")
    elif "muscle" in goal:
        feedback += "🏋️ More protein needed for muscle gain! "
        suggestions.append("• Next: **chicken breast + eggs**")
    
    # Random encouragement
    encouragements = [
        "You're doing awesome! 💯",
        "Perfect balance! Keep going! 🔥", 
        "Healthy choice! 👏",
        "Great awareness! 🌟"
    ]
    
    return f"{feedback}\n\n**Next meal suggestions:**\n" + "\n".join(suggestions) + f"\n\n{ random.choice(encouragements) }"

# Chat interface
st.chat_message("assistant").markdown("""
👋 **Hi!** I'm your nutrition coach!

**Tell me:**
- What you ate today
- "I had rice and chicken"
- "Ate pizza for lunch"

**I'll analyze:**
- Protein, carbs, fats, fiber
- Balance for your goals
- Perfect next meal suggestions
""")

# Chat input
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What did you eat today?"):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing your meal..."):
            response = analyze_food(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Quick buttons
st.markdown("---")
st.subheader("🚀 Quick Analysis")
col1, col2, col3 = st.columns(3)

if col1.button("🍗 High Protein Meal", use_container_width=True):
    st.chat_message("user").markdown("I ate chicken and eggs")
    response = analyze_food("chicken eggs")
    st.chat_message("assistant").markdown(response)

if col2.button("🍚 Carb Heavy Meal", use_container_width=True):
    st.chat_message("user").markdown("I ate rice and bread") 
    response = analyze_food("rice bread")
    st.chat_message("assistant").markdown(response)

if col3.button("🥗 Veggie Meal", use_container_width=True):
    st.chat_message("user").markdown("I ate broccoli salad")
    response = analyze_food("broccoli salad")
    st.chat_message("assistant").markdown(response)

# Clear chat
if st.button("🗑️ Clear Chat", use_container_width=True):
    st.session_state.messages = []
    st.rerun()

st.markdown("---")
st.caption("🤖 Smart AI Coach ")