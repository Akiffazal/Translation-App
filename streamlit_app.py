import streamlit as st
from deep_translator import GoogleTranslator

# App title
st.title("Translation App")

# Input text
st.write("Enter the text you want to translate:")
input_text = st.text_area("Input Text", "")

# Language selection
st.write("Select the languages for translation:")
input_lang = st.selectbox("Input Language", ["auto", "en", "fr", "es", "de"], index=0)  # Simplified for demo
output_lang = st.selectbox("Output Language", ["en", "fr", "es", "de"], index=1)  # Default is French

# Button to translate
if st.button("Translate"):
    if input_text:
        translation = GoogleTranslator(source=input_lang, target=output_lang).translate(input_text)
        st.success(f"**Translated Text:** {translation}")
    else:
        st.error("Please enter some text to translate.")

# Footer
st.write("Powered by Google Translate API")
