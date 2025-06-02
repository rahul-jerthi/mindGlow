import streamlit as st
from config import gemini_config  # This runs the API config
from utils.analyzer import analyze_depression
from utils.questions import questions, placeholders

# Set Streamlit page config
st.set_page_config(page_title="Mind Glow", layout="centered", page_icon="✨")

# Header
st.markdown("""
    <h1 style='text-align: center;'>
        <span style='color: white;'>🌟 Mind Glow:</span>
        <span style='color: violet;'>Your Vibe Check 🌟</span>
    </h1>
""", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #6b7280;'>Big feels? I'm your soft place to land 💫</h3>", unsafe_allow_html=True)

st.write("**How it works:** Type how you’re feeling below. Example vibes are there to spark you—keep it real, babe! 💖")

# Input responses
user_responses = []
for i, (q, p) in enumerate(zip(questions, placeholders)):
    response = st.text_input(f"{i+1}. {q}", placeholder=p, key=f"q{i}")
    user_responses.append(response)

# Button
# if st.button("✨ Glow Me Up—Analyze Now! ✨", use_container_width=True):
#     if all(response.strip() for response in user_responses):
#         with st.spinner("Reading your glow, cutie..."):
#             result = analyze_depression(user_responses)

#         st.markdown("<h2 style='color: #ff4b4b;'>🎉 Your Glow Report 🎉</h2>", unsafe_allow_html=True)
#         lines = result.split('\n')
#         formatted_result = ""
#         for line in lines:
#             if ':' in line:
#                 key, value = line.split(':', 1)
#                 formatted_result += f"<p style='font-size: 18px; margin: 10px 0; color: #000000;'><strong>{key.strip()}:</strong> {value.strip()}</p>"
#         st.markdown(
#             f"<div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px;'>{formatted_result}</div>",
#             unsafe_allow_html=True
#         )
#     else:
#         st.error("Oops, fill in all the vibes so I can glow you up!")


# Analyze Button—bold and clickable
if st.button("✨ Glow Me Up—Analyze Now! ✨", use_container_width=True):
    if all(response.strip() for response in user_responses):  # No empty fields, babe!
        with st.spinner("Reading your glow, cutie..."):
            result = analyze_depression(user_responses)
        st.markdown("<h2 style='color: #ff4b4b;'>🎉 Your Glow Report 🎉</h2>", unsafe_allow_html=True)
        
        # Split the result into lines and clean up Markdown junk
        lines = result.split('\n')
        formatted_result = ""
        for line in lines:
            if ':' in line:  # Only process lines with a colon
                key, value = line.split(':', 1)
                # Strip * and ** from key and value
                clean_key = key.strip().replace('*', '').replace('**', '')
                clean_value = value.strip().replace('*', '').replace('**', '')
                formatted_result += f"<p style='font-size: 18px; margin: 10px 0; color: #000000;'><strong>{clean_key}:</strong> {clean_value}</p>"
        
        st.markdown(
            f"<div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px;'>{formatted_result}</div>",
            unsafe_allow_html=True
        )
        
    else:
        st.error("Oops, Cutie fill in all the vibes so I can glow you up!")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff69b4;'>Crafted with care from your words — keep shining ✨</p>", unsafe_allow_html=True)
