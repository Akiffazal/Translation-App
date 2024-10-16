import streamlit as st
from deep_translator import GoogleTranslator

# Supported languages
LANGUAGES = {
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'ar': 'Arabic',
    'hy': 'Armenian',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'ca': 'Catalan',
    'hr': 'Croatian',
    'cs': 'Czech',
    'da': 'Danish',
    'nl': 'Dutch',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'tl': 'Filipino',
    'fi': 'Finnish',
    'fr': 'French',
    'de': 'German',
    'el': 'Greek',
    'gu': 'Gujarati',
    'ht': 'Haitian Creole',
    'ha': 'Hausa',
    'haw': 'Hawaiian',
    'he': 'Hebrew',
    'hi': 'Hindi',
    'hu': 'Hungarian',
    'is': 'Icelandic',
    'ig': 'Igbo',
    'id': 'Indonesian',
    'ga': 'Irish',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'kn': 'Kannada',
    'kk': 'Kazakh',
    'km': 'Khmer',
    'ko': 'Korean',
    'ku': 'Kurdish (Kurmanji)',
    'ky': 'Kyrgyz',
    'la': 'Latin',
    'lv': 'Latvian',
    'lt': 'Lithuanian',
    'lb': 'Luxembourgish',
    'mk': 'Macedonian',
    'ml': 'Malayalam',
    'mt': 'Maltese',
    'mi': 'Māori',
    'mr': 'Marathi',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'no': 'Norwegian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'pa': 'Punjabi',
    'ro': 'Romanian',
    'ru': 'Russian',
    'sr': 'Serbian',
    'si': 'Sinhalese',
    'sk': 'Slovak',
    'sl': 'Slovenian',
    'es': 'Spanish',
    'su': 'Sundanese',
    'sw': 'Swahili',
    'sv': 'Swedish',
    'tl': 'Tagalog',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'cy': 'Welsh',
    'xh': 'Xhosa',
    'yi': 'Yiddish',
    'zu': 'Zulu',
}

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
