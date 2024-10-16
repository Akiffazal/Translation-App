# Translation App

A simple web application for translating text between various languages using the Deep Translator API. This app is built using Streamlit and can be easily deployed on Streamlit Community Cloud.

## Features

- **Language Selection**: Choose the input and output languages from a comprehensive list of supported languages, with English set as the default input language.
- **Text Translation**: Enter text to translate, and receive the translated text instantly.
- **User-Friendly Interface**: A clean and intuitive interface designed for ease of use.

## Supported Languages

The app supports translation between a variety of languages, including (but not limited to):

- Afrikaans
- Albanian
- Arabic
- Armenian
- Bengali
- Bosnian
- Catalan
- Croatian
- Czech
- Danish
- Dutch
- English (default input language)
- French
- German
- Hindi
- Italian
- Japanese
- Korean
- Portuguese
- Russian
- Spanish
- Turkish
- And many more!

## Requirements

To run this application, you will need:

- Python 3.7 or higher
- Streamlit
- Deep Translator

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Akiffazal/translation-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd translation-app
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open the provided URL in your web browser.

3. Select the input and output languages, enter the text you want to translate, and click the "Translate" button.

## Deployment

You can easily deploy this app on Streamlit Community Cloud by following these steps:

1. Push your code to a GitHub repository.
2. Go to [Streamlit Community Cloud](https://streamlit.io/sharing) and sign in.
3. Click on "New app", select your repository, and deploy.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Deep Translator](https://github.com/nicknochnack/Deep-Translator)
