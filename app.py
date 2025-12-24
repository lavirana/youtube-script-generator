import streamlit as st
from groq import Groq

# 1. Connect to the Secret Key you added in Streamlit Cloud
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Page Configuration
st.set_page_config(page_title="AI YouTube Script Generator", page_icon="🎥", layout="centered")

# --- CUSTOM CSS FOR THE CLEAN CARD LAYOUT ---
# --- THE ULTIMATE FOOTER REMOVER ---
st.markdown("""
    <style>
        /* CSS Fallback */
        header, footer, [data-testid="stHeader"], [data-testid="stFooter"], [data-testid="stToolbar"] {
            display: none !important;
            visibility: hidden !important;
        }
        .main .block-container {
            background-color: #ffffff;
            padding: 3rem 2rem !important;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            max-width: 720px;
            margin: auto;
            border: 1px solid #eee;
        }
        .stApp { background-color: #f8f9fa; }
    </style>

    <script>
        function removeElements() {
            // Target the footer and the specific "Built with Streamlit" link
            const footer = document.querySelector('footer');
            const toolbar = document.querySelector('[data-testid="stToolbar"]');
            const decoration = document.querySelector('[data-testid="stDecoration"]');
            
            if (footer) footer.remove();
            if (toolbar) toolbar.remove();
            if (decoration) decoration.remove();
            
            // Look for any div containing "Built with" and hide it
            const divs = document.getElementsByTagName('div');
            for (let i = 0; i < divs.length; i++) {
                if (divs[i].innerText && divs[i].innerText.includes('Built with')) {
                    divs[i].style.display = 'none';
                }
            }
        }

        // Run immediately and then every 500ms to catch late-loading elements
        setInterval(removeElements, 500);
    </script>
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