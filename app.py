import streamlit as st
from groq import Groq

# 1. Connect to the Secret Key you added in Streamlit Cloud
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Page Configuration
st.set_page_config(page_title="AI YouTube Script Generator", page_icon="🎥", layout="centered")

# --- CUSTOM CSS FOR THE CLEAN CARD LAYOUT ---
st.markdown("""
    <style>
        /* 1. Hide the Sidebar and the Toggle Button at the top left */
        [data-testid="stSidebar"], [data-testid="stSidebarNav"], .st-emotion-cache-16idsys p {display: none;}
        
        /* 2. Hide the entire Streamlit Header (Hamburger & Fullscreen) */
        header, [data-testid="stHeader"] {visibility: hidden; display: none;}

        /* 3. Hide the entire Footer container completely */
        footer {visibility: hidden; height: 0%; position: absolute;}
        [data-testid="stFooter"] {display: none;}

        /* 4. Hide the 'Status Widget' (The small lightning bolt/spinner) */
        [data-testid="stStatusWidget"] {visibility: hidden; display: none;}

        /* 5. Custom Page Styling */
        .stApp { background-color: #f8f9fa; }

        .main .block-container {
            background-color: #ffffff;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            max-width: 700px;
            margin-top: 20px;
            border: 1px solid #eee;
        }

        /* 6. Professional Button */
        .stButton>button {
            width: 100%; border-radius: 12px; height: 3.5em; 
            background-color: #e63946; color: white; font-weight: bold; border: none;
        }
        .stButton>button:hover { background-color: #d62828; color: white; }
    </style>
""", unsafe_allow_html=True)

import streamlit as st

# JavaScript to check the parent URL
st.markdown("""
<script>
    // Check if the app is inside an iframe
    if (window.self !== window.top) {
        var parentUrl = document.referrer;
        // Replace 'thetechinfo.net' with your actual domain
        if (!parentUrl.includes("thetechinfo.net")) {
            document.body.innerHTML = "<h1>Access Denied</h1><p>This tool is only authorized for use on TheTechInfo.net</p>";
        }
    }
</script>
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