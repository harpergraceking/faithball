import streamlit as st
import random

#page setup 
st.set_page_config(page_title="Faith Ball of Emotion 🎱", page_icon="🎱", layout="centered")

st.title("Faith Ball of Emotion 🎱")
st.caption("Pick your emotion and shake for a verse")

#emotionbank
verses = {
	"Joyful": [
		(),
		()
	],
	"Scared": [
		(),
		()
	],
	"Sad": [
		(),
		()
	],
	"Anxious": [
		(),
		()
	],
	"Thankful": [
		(),
		()
	]
}

#app ui
emotion = st.selectbox("I am feeling...", list(verses.keys()))

if st.button("Shake the Faith Ball 🎱"):
	verse_ref, verse_text = random.choice(verses[emotion])
	st.success(f""{verse_text}" - {verse_ref}")
	st.balloons()
