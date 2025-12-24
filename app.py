import streamlit as st
from groq import Groq
import time

# 1. HARDCODE YOUR API KEY HERE
GROQ_API_KEY = "YOUR_ACTUAL_GROQ_API_KEY"

# Page Configuration
st.set_page_config(page_title="AI YouTube Script Generator", page_icon="🎥", layout="centered")

# Custom CSS to hide Sidebar, Footer, and Fullscreen button
st.markdown("""
    <style>
        /* Hide the sidebar */
        [data-testid="stSidebar"] {display: none;}
        [data-testid="stSidebarNav"] {display: none;}
        
        /* Hide the "Built with Streamlit" footer */
        footer {visibility: hidden;}
        
        /* Hide the Top Right Hamburger menu and Fullscreen button */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Optional: Style the button to match your blog's red theme */
        .stButton>button {
            width: 100%; 
            border-radius: 10px; 
            height: 3em; 
            background-color: #FF0000; 
            color: white; 
            border: none;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #CC0000; 
            color: white;
        }
    ._hostedName_1upux_12 {
    display: none !important;
}
 ._linkOutText_1upux_17 {
    display: none !important;
}
            ._container_1upux_1 {
    background-color: white !important;
            }
    </style>
""", unsafe_allow_html=True)

st.title("🎥 YouTube Script Generator")
st.write("Enter your video topic below to generate a professional script instantly!")

# User Inputs
topic = st.text_input("Video Topic:", placeholder="e.g. How to learn Artificial Intelligence in 2025")
col1, col2 = st.columns(2)
with col1:
    tone = st.selectbox("Choose Tone:", ["Informative", "Funny", "Professional", "Storytelling", "Energetic"])
with col2:
    video_length = st.slider("Target Length (Min):", 1, 15, 5)

if st.button("Generate Script 🚀"):
    if not topic:
        st.warning("Please enter a topic to generate a script.")
    else:
        try:
            client = Groq(api_key=GROQ_API_KEY)
            
            prompt = f"""
            Act as an expert YouTube Content Creator. Write a comprehensive video script in English.
            Topic: {topic}
            Tone: {tone}
            Estimated Video Duration: {video_length} minutes.
            Include: Hook, Introduction, Key Chapters, Call to Action, and Outro.
            """

            with st.spinner("AI is crafting your script..."):
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                )
                
                script = completion.choices[0].message.content
                st.success("Your Script is Ready!")
                st.markdown("---")
                st.markdown(script)
                
        except Exception as e:
            # RATE LIMIT VALIDATION
            if "429" in str(e) or "rate_limit_exceeded" in str(e).lower():
                st.error("⚠️ **Server Busy:** Many people are using the tool. Please wait **60 seconds** and try again.")
            else:
                st.error(f"An unexpected error occurred: {e}")

# Footer for your blog
st.markdown("---")
# st.caption("Developed with ❤️ for **TheTechInfo.net**")