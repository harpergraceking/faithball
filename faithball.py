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
		("Psalm 16:11", "You make known to me the path of life; in your presence there is fullness of joy; at your right hand are pleasures forevermore."),
		("Psalm 37:4", "Delight yourself in the Lord, and he will give you the desires of your heart."),
		("1 Thessalonians 5:16-18", "Rejoice always, pray without ceasing, give thanks in all circumstances; for this is the will of God in Christ Jesus for you.")
	],
	"Sad": [
		("Deuteronomy 31:8", "The Lord Himself goes before you and will be with you; He will never leave you nor forsake you. Do not be afraid; do not be discouraged."),
		("Matthew 5:48", "Blessed are those who mourn, for they will be comforted."),
		("Psalm 9:9", "The Lord is a shelter for the oppressed, a refuge in times of trouble."),
		("Isaiah 40:31", "But those who trust in the Lord will find new strength. They will soar high on wings like eagles. They will run and not grow weary. They will walk and not faint.")
	],
	"Anxious": [
		("Matthew 6:34", "Therefore do not worry about tomorrow, for tomorrow will worry about itself. Each day has enough trouble of its own."),
		("Psalm 34:4", "I sought the LORD, and He answered me and delivered me from all my fears."),
		("Isaiah 41:10", "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand."),
		("Psalm 23:4", "Even though I walk through the darkest valley, I will fear no evil, for you are with me; your rod and your staff, they comfort me.")
	],
	"Thankful": [
		("Colossians 3:15", "Let the peace of Christ rule in your hearts, since as members of one body you were called to peace. And be thankful."),
		("Psalm 7:17", "I will give thanks to the Lord because of his righteousness; I will sing the praises of the name of the LORD Most High."),
		("1 Chronicles 16:34", "Give thanks to the Lord, for he is good; his love endures forever."),
		("James 1:17", "Every good and perfect gift is from above, coming down from the Father of the heavenly lights, who does not change like shifting shadows.")
	],
	"Angry": [
		("Proverbs 14:17", "A quick-tempered person acts foolishly, and one who schemes is hated... A patient person shows great understanding, but a tempered one promotes foolishness."),
		("James 1:19-20", "My dear brothers and sisters, understand this: Everyone should be quick to listen, slow to speak, and slow to anger, for human anger does not accomplish God's righteousness."),
		("Ephesians 4:26-27", "Be angry and do not sin. Don't let the sun go down on your anger, and don't give the devil an opportunity."),
		("Ephesians 4:31-32", "Let all bitterness, anger and wrath, shouting and slander be removed from you, along with all malice. And be kind and compassionate to one another, forgiving one another, just as God also forgave you in Christ.")
	],
	"Guilty": [
		("John 8:10-11", "Straightening up, Jesus said to her, 'Woman, where are they? Did no one condemn you?' She said, 'No one, Lord.' And Jesus said, 'I do not condemn you, either. Go. From now on sin no more.'"),
		("Romans 8:1-2", "Therefore, there is now no condemnation for those who are in Christ Jesus. For the law of the Spirit of life in Christ Jesus has set you free from the law of sin and death."),
		("1 John 1:9", "If we confess our sins, He is faithful and righteous to forgive us our sins and to cleanse us from all unrighteousness."),
		("Hebrews 8:12", "And I will forgive their wickedness, and I will never again remember their sins.")
		
	],
	"Lucky": [
		("Jeremiah 29:11", "For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope."),
		("Deuteronomy 31:6", "Be strong and courageous. Do not fear or be in dread of them, for it is the Lord your God who goes with you. He will not leave you or forsake you."),
		("Proverbs 3:5-6", "Trust in the Lord with all your heart, and do not lean on your own understanding. In all your ways acknowledge him, and he will make straight your paths."),
		("Isaiah 41:10", "Fear not, for I am with you; do not be dismayed, for I am your God; I will strengthen you, I will help you, I will uphold you with my righteous right hand.")
	]


}
colors = {
    "Joyful": "#FFD23F",     #yellow
    "Anxious": "#EE4B2B",     #red
    "Sad": "#39546d",        #blue
    "Guilty": "#84597e",    #purple
    "Thankful": "#FA86C4",    #pink
	"Angry": "#FF0000",     #red
	"Lucky": "#4CBB17",   #green
}
emotion = st.selectbox("I am feeling...", list(verses.keys()))

# --- Apply color background immediately ---
color = colors.get(emotion, "#ffffff")
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

# shake button
if st.button("Shake the Faith Ball 🎱"):
    placeholder = st.empty()
    shake_text = ["Shaking...", "Still shaking...", "Almost there...", "Let the ball tell you what you need to hear"]
    for t in shake_text:
        placeholder.markdown(f"<h3 style='text-align:center;'>{t}</h3>", unsafe_allow_html=True)
        time.sleep(0.6)
    placeholder.empty()

    verse_ref, verse_text = random.choice(verses[emotion])

    # --- Fade-in effect ---
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

    # --- Sparkle effect ---
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

    # --- Verse display ---
    st.markdown(f"<h2 class='fadein' style='text-align:center;'>{verse_text}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; font-style:italic;'>— {verse_ref}</p>", unsafe_allow_html=True)
