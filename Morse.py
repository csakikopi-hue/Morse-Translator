from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..',  '9': '----.',
    'Á': '.--.-', 'É': '..-..', 'Í': '..-.-', 'Ó': '---.',
    'Ö': '---.', 'Ő': '----', 'Ú': '..--', 'Ü': '..--',
    'Ű': '..---.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


def encode(text: str) -> dict:
    """Convert plain text to Morse code."""
    result = []
    for ch in text.upper():
        if ch not in MORSE_CODE:
            return {"error": f"Character '{ch}' is not supported in Morse code."}
        result.append(MORSE_CODE[ch])
    return {"result": ' '.join(result), "length": len(result)}


def decode(morse_str: str) -> dict:
    """Convert Morse code to plain text. Words separated by '/', letters by space."""
    result_words = []
    for word in morse_str.strip().split('/'):
        word = word.strip()
        if not word:
            continue
        word_str = ''
        for code in word.split():
            if not code:
                continue
            if not all(c in '.-' for c in code):
                return {"error": f"Invalid morse code: '{code}'. Only . and - are allowed."}
            if code not in REVERSE_MORSE:
                return {"error": f"Unknown morse sequence: '{code}'."}
            word_str += REVERSE_MORSE[code]
        result_words.append(word_str)
    return {"result": ' '.join(result_words), "length": len(result_words)}


def validate_request(data: dict) -> tuple[str, str] | tuple[None, None]:
    """Validate incoming request data. Returns (text, mode) or (None, None) on error."""
    if not data:
        return None, None
    text = data.get('text', '').strip()
    mode = data.get('mode', '1')
    if mode not in ('1', '2'):
        return None, None
    return text, mode


@app.route('/')
def index():
    return render_template('Morse.html')


@app.route('/convert', methods=['POST'])
def convert():
    text, mode = validate_request(request.json)

    if text is None:
        return jsonify({"error": "Invalid request."}), 400
    if not text:
        return jsonify({"error": "Input is empty."}), 400

    result = encode(text) if mode == '1' else decode(text)
    status = 200 if 'result' in result else 422
    return jsonify(result), status


@app.route('/health')
def health():
    """Simple health check endpoint."""
    return jsonify({"status": "ok", "supported_chars": len(MORSE_CODE)})


@app.errorhandler(404)
def not_found(_):
    return jsonify({"error": "Not found."}), 404


@app.errorhandler(500)
def server_error(_):
    return jsonify({"error": "Internal server error."}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)