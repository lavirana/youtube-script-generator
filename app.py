import streamlit as st
from groq import Groq

# 1. HARDCODE YOUR API KEY
GROQ_API_KEY = "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"

st.set_page_config(page_title="AI YouTube Script Generator", page_icon="🎥", layout="centered")

# --- CUSTOM CSS FOR CLEAN CARD LAYOUT ---
st.markdown("""
    <style>
        /* 1. Hide default Streamlit elements */
        [data-testid="stSidebar"] {display: none;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}

        /* 2. Change background to a light grey for contrast */
        .stApp {
            background-color: #f8f9fa;
        }

        /* 3. Create the White Card Effect */
        .main .block-container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            max-width: 700px;
            margin-top: 50px;
            border: 1px solid #eee;
        }

        /* 4. Style the Input Fields */
        .stTextInput input, .stSelectbox div[data-baseweb="select"] {
            border-radius: 10px !important;
        }

        /* 5. Custom Red Button */
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
            box-shadow: 0 5px 15px rgba(230, 57, 70, 0.3);
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

# --- APP CONTENT ---
st.markdown("<h1 style='text-align: center; color: #1d3557;'>🎥 YouTube Script Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #457b9d;'>Enter your topic below to generate a high-engagement script.</p>", unsafe_allow_html=True)

# Layout using columns for a tighter feel
topic = st.text_input("What is your video about?", placeholder="e.g. 5 Best AI Tools for Students")

col1, col2 = st.columns(2)
with col1:
    tone = st.selectbox("Video Tone", ["Informative", "Funny", "Professional", "Storytelling"])
with col2:
    video_length = st.slider("Length (Min)", 1, 15, 5)

if st.button("Generate Professional Script"):
    # (Existing Groq logic here...)
    pass

st.markdown("---")
#st.markdown("<p style='text-align: center; font-size: 0.8em; color: gray;'>Powered by <b>TheTechInfo.net</b></p>", unsafe_allow_html=True)