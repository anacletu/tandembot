# Welcome to Tandembot!

A voice chatbot utilizing speech recognition, speech synthesis, and artificial intelligence through the Google Gemini API to interact with users.

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example Usage](#example-usage)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Features

- Recording of user input audio.
- Speech recognition to convert user input into text.
- Interaction with an artificial intelligence model to generate responses.
- Speech synthesis to transform chatbot responses into audio.

## Prerequisites

- Python 3.x
- Python libraries listed in `requirements.txt`
- Valid credentials for the Gemini API

## Installation

1. Clone the repository:
```bash
git clone https://github.com/anacletu/virtual_tandem
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file in the project root and add your API key, endpoint, and audio preferences:
```env
API_KEY=your_api_key
API_URL=https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent
FS=44100
DURATION=15
```

## Usage
Run the main script:

``` bash
python main.py
```

Follow the instructions in the terminal to interact with the chatbot.
The script will make a request to the API, convert the response into speech, and play the audio.

## Example Usage
See a quick video demonstrating simple conversations in Portuguese, English, and Spanish.

https://github.com/anacletu/tandembot/assets/56979763/33817e23-0f4b-4245-aa1b-306f7661abfa

## Future Improvements
- Addition of support for more languages.
- Implementation of a graphical interface to facilitate interaction.
- Improvement of speech recognition and speech synthesis robustness.
- More configuration possibilities, such as language level and response complexity.

## Contributing
Contributions are welcome! For suggestions, bug fixes, and other changes, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [license](LICENSE) file for more details.