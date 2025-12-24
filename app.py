import streamlit as st
from groq import Groq

# 1. Connect to the Secret Key you added in Streamlit Cloud
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Page Configuration
st.set_page_config(page_title="AI YouTube Script Generator", page_icon="🎥", layout="centered")

# --- CUSTOM CSS FOR THE CLEAN CARD LAYOUT ---
st.markdown("""
    <style>
        /* Hide default Streamlit elements */
        [data-testid="stSidebar"] {display: none;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}

        /* Background color for the page */
        .stApp {
            background-color: #f8f9fa;
        }

        /* Create the White Card Effect */
        .main .block-container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            max-width: 700px;
            margin-top: 50px;
            border: 1px solid #eee;
        }

        /* Custom Red Button Style */
        .stButton>button {
            width: 100%; 
            border-radius: 12px; 
            height: 3.5em; 
            background-color: #e63946; 
            color: white; 
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #d62828;
            color: white;
            box-shadow: 0 5px 15px rgba(230, 57, 70, 0.3);
        }
            ._hostedName_1upux_12 {
    display: none !important;
    margin-left: .75rem;
}
            ._linkOutText_1upux_17 {
    display: none !important;
    margin-right: 1rem;
    font-weight: 600;
}
    </style>
""", unsafe_allow_html=True)

# --- APP CONTENT ---
st.markdown("<h1 style='text-align: center; color: #1d3557;'>🎥 YouTube Script Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #457b9d;'>Generate a professional, high-engagement script instantly!</p>", unsafe_allow_html=True)

# Input Section
topic = st.text_input("Video Topic:", placeholder="e.g. How to learn Artificial Intelligence in 2025")

col1, col2 = st.columns(2)
with col1:
    tone = st.selectbox("Choose Tone:", ["Informative", "Funny", "Professional", "Storytelling", "Energetic"])
with col2:
    video_length = st.slider("Target Length (Min):", 1, 15, 5)

# --- GENERATION LOGIC ---
if st.button("Generate Script 🚀"):
    if not topic:
        st.warning("Please enter a topic first!")
    else:
        try:
            # Initialize Groq with the Secret Key
            client = Groq(api_key=GROQ_API_KEY)
            
            prompt = f"""
            Act as an expert YouTube Content Creator. Write a comprehensive video script in English.
            Topic: {topic}
            Tone: {tone}
            Estimated Video Duration: {video_length} minutes.
            Include: A catchy Hook, Introduction, Key Chapters/Points, a Call to Action, and an Outro.
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
            if "429" in str(e):
                st.error("⚠️ Server Busy: Please wait 60 seconds and try again.")
            else:
                st.error(f"Something went wrong: {e}")

# Footer
st.markdown("---")
# st.markdown("<p style='text-align: center; font-size: 0.8em; color: gray;'>Developed for <b>TheTechInfo.net</b></p>", unsafe_allow_html=True)