import streamlit as st
import random
import time

#page setup 
st.set_page_config(page_title="Faith Ball of Emotion 🎱", page_icon="🎱", layout="centered")

st.markdown("<h1 style='text-alignment:center'>🎱 Faith Ball of Emotion 🎱</h1>", unsafe_allow_html=True)
st.caption("Pick your emotion and shake for a verse")

#emotionbank
verses = {
	"Joyful": [
		("Philippians 4:4", "Rejoice in the Lord always; again I will say, rejoice."),
		("Psalm 16:11", "You make known to me the path of life; in your presence there is fullness of joy; at your right hand are pleasures forevermore.")
	],
	"Scared": [
		("Isaiah 41:10", "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand."),
		("Psalm 23:4", "Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.")
	],
	"Sad": [
		("Deuteronomy 31:8", "The Lord Himself goes before you and will be with you; He will never leave you nor forsake you. Do not be afraid; do not be discouraged."),
		("Matthew 5:48", "Blessed are those who mourn, for they will be comforted.")
	],
	"Anxious": [
		("Matthew 6:34", "Therefore do not worry about tomorrow, for tomorrow will worry about itself. Each day has enough trouble of its own."),
		("Psalm 34:4", "I sought the LORD, and He answered me and delivered me from all my fears.")
	],
	"Thankful": [
		("Colossians 3:15", "Let the peace of Christ rule in your hearts, since as members of one body you were called to peace. And be thankful."),
		("Psalm 7:17", "I will give thanks to the LORD because of his righteousness; I will sing the praises of the name of the LORD Most High.")
	]
}

#app ui
emotion = st.selectbox("I am feeling...", list(verses.keys()))

if st.button("Shake the Faith Ball 🎱"):
	placeholder = st.empty()
	shake_text = ["Shaking...", "Still shaking...", "Almost there...", "✨"]
	for t in shake_text:
		placeholder.markdown(f"<h3 style='text-align:center;'>{t}</h3>", unsafe_allow_html=True)
		time.sleep(0.6)
	placeholder.empty()
	
	verse_ref, verse_text = random.choice(verses[emotion])
	st.balloons()
	st.markdown(f'<h2 style="text-align:center;">“{verse_text}”</h2>', unsafe_allow_html=True)
	st.markdown(f"<p style='text-align:center; font-style:italic;'>— {verse_ref}</p>", unsafe_allow_html=True)

colors = {
    "Joy": "#fff8e7",
    "Fear": "#cce0ff",
    "Sadness": "#e6e6fa",
    "Anxiety": "#e0fff5",
    "Gratitude": "#fff5e0"
}

color = colors[emotion]
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {color};
        transition: background-color 1s ease;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    .fadein {
        animation: fadeIn 2s ease-in;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(f"<h2 class='fadein' style='text-align:center;'>“{verse_text}”</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    @keyframes sparkle {
      0% {text-shadow: 0 0 5px gold;}
      50% {text-shadow: 0 0 20px gold;}
      100% {text-shadow: 0 0 5px gold;}
    }
    .sparkle {
      animation: sparkle 2s infinite;
      color: #fdd835;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(f"<h2 class='sparkle' style='text-align:center;'>“{verse_text}”</h2>", unsafe_allow_html=True)
