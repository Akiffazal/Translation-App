import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# App title
st.title("Translation App")

# Input text
st.write("Enter the text you want to translate:")
input_text = st.text_area("Input Text", "")

# Language selection
st.write("Select the languages for translation:")
input_lang = st.selectbox("Input Language", list(LANGUAGES.values()), index=21)  # Default is English
output_lang = st.selectbox("Output Language", list(LANGUAGES.values()), index=38)  # Default is French

# Button to translate
if st.button("Translate"):
    # Get language codes for selected languages
    input_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(input_lang)]
    output_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(output_lang)]
    
    # Translate the text
    if input_text:
        translation = translator.translate(input_text, src=input_lang_code, dest=output_lang_code)
        st.success(f"**Translated Text:** {translation.text}")
    else:
        st.error("Please enter some text to translate.")

# Footer
st.write("Powered by Google Translate API")

