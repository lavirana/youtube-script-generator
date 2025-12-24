import streamlit as st
from groq import Groq

# Page Configuration
st.set_page_config(page_title="AI YouTube Script Generator", page_icon="🎥")

# Sidebar for API Key
st.sidebar.title("Settings ⚙️")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password", help="Get your free key at console.groq.com")

st.title("🎥 YouTube Script Generator")
st.write("Enter your video topic below to generate a professional, high-engagement script instantly!")

# User Inputs
topic = st.text_input("Video Topic:", placeholder="e.g. How to learn Artificial Intelligence in 2025")
tone = st.selectbox("Choose Tone:", ["Informative", "Funny", "Professional", "Storytelling", "Energetic"])
video_length = st.slider("Target Length (Minutes):", 1, 15, 5)

if st.button("Generate Script 🚀"):
    if not api_key:
        st.error("Please enter your Groq API Key in the sidebar to continue.")
    elif not topic:
        st.warning("Please enter a topic to generate a script.")
    else:
        try:
            client = Groq(api_key=api_key)
            
            # AI Prompt - Optimized for full English and better structure
            prompt = f"""
            Act as an expert YouTube Content Creator. Write a comprehensive video script in English.
            Topic: {topic}
            Tone: {tone}
            Estimated Video Duration: {video_length} minutes.
            
            The script must include:
            1. An attention-grabbing HOOK (first 15 seconds).
            2. A clear INTRODUCTION.
            3. KEY CHAPTERS/BODY points with detailed explanations.
            4. A strong CALL TO ACTION (CTA) to like and subscribe.
            5. A memorable OUTRO.
            
            Make the language engaging, natural, and easy to read.
            """

            with st.spinner("AI is crafting your professional script..."):
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                )
                
                script = completion.choices[0].message.content
                st.success("Your Script is Ready!")
                st.markdown("---")
                
                # Using markdown for better formatting of the result
                st.markdown(script)
                
                # Optional Download button
                st.download_button(
                    label="📥 Download Script as Text",
                    data=script,
                    file_name="youtube_script.txt",
                    mime="text/plain"
                )
                
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer for your Blog
st.markdown("---")
st.caption("Developed with ❤️ for **TheTechInfo.net**")