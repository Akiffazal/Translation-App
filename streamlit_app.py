import streamlit as st
from deep_translator import GoogleTranslator

# Get all supported languages dynamically
supported_languages = GoogleTranslator.get_supported_languages()
LANGUAGES = {lang['code']: lang['name'] for lang in supported_languages}

# App title
st.title("Translation App")

# Language selection
st.write("Select the languages for translation:")
input_lang = st.selectbox("Input Language", list(LANGUAGES.values()), index=0)  # Default to the first option
output_lang = st.selectbox("Output Language", list(LANGUAGES.values()), index=1)  # Default to the second option

# Input text
st.write("Enter the text you want to translate:")
input_text = st.text_area("Input Text", "")

# Button to translate
if st.button("Translate"):
    if input_text:
        # Get language codes for selected languages
        input_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(input_lang)]
        output_lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(output_lang)]

        # Translate the text
        translation = GoogleTranslator(source=input_lang_code, target=output_lang_code).translate(input_text)
        st.success(f"**Translated Text:** {translation}")
    else:
        st.error("Please enter some text to translate.")

# Footer
st.write("Powered by Google Translate API")
