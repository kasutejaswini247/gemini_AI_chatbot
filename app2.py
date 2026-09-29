import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e1b4b, #312e81);
    color: white;
}

/* Main container */
.block-container {
    max-width: 800px;
    padding-top: 50px;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;
    background: linear-gradient(90deg, #60a5fa, #a78bfa, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 35px;
}

/* Text area label */
label {
    color: #e2e8f0 !important;
    font-weight: 600 !important;
}

/* Text area */
.stTextArea textarea {
    background-color: rgba(15, 23, 42, 0.8) !important;
    color: white !important;
    border: 1px solid #6366f1 !important;
    border-radius: 15px !important;
    padding: 15px !important;
    font-size: 16px !important;
}

/* Text area focus */
.stTextArea textarea:focus {
    border: 2px solid #a78bfa !important;
    box-shadow: 0 0 15px rgba(167, 139, 250, 0.4) !important;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #ec4899);
    color: white;
    font-size: 17px;
    font-weight: 700;
    transition: 0.3s;
    margin-top: 15px;
}

/* Button hover */
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(139, 92, 246, 0.5);
}

/* Response box */
.response-box {
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid #6366f1;
    border-radius: 18px;
    padding: 25px;
    margin-top: 25px;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
}

/* Response heading */
.response-title {
    color: #a78bfa;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 15px;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 45px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- UI ----------------

st.markdown(
    '<div class="main-title">🤖 Gemini AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">✨ Ask Gemini anything and get intelligent answers instantly</div>',
    unsafe_allow_html=True
)


prompt = st.text_area(
    "💬 Enter your prompt",
    placeholder="Explain Artificial Intelligence...",
    height=150
)


if st.button("🚀 Generate Response"):

    if prompt:

        with st.spinner("🧠 Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.success("✅ Response generated!")

        st.markdown(
            '<div class="response-box">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="response-title">💡 Gemini Response</div>',
            unsafe_allow_html=True
        )

        st.write(response.text)

        st.markdown("</div>", unsafe_allow_html=True)

    else:

        st.warning("⚠️ Please enter a prompt.")


# Footer
st.markdown(
    '<div class="footer">Powered by Google Gemini ✨</div>',
    unsafe_allow_html=True
)