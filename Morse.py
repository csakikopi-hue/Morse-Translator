from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
    # Hungarian special characters
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


def fordito(szoveg):
    """Text to Morse code"""
    result = []
    for ch in szoveg.upper():
        if ch in MORSE_CODE:
            result.append(MORSE_CODE[ch])
        else:
            return {"error": f"Hiba! A '{ch}' karakter nem támogatott Morse kódban."}
    return {"result": ' '.join(result)}

# Note: .upper() already handles á→Á, é→É, ő→Ő etc. in Python


def visszafejto(morse_sor):
    """Morse code to text - words separated by ' / ', letters by ' '"""
    words = morse_sor.strip().split('/')
    result_words = []
    for word in words:
        word = word.strip()
        if not word:
            continue
        letters = word.split()
        word_str = ''
        for code in letters:
            if not code:
                continue
            if not all(c in '.-' for c in code):
                return {"error": f"Hiba! Érvénytelen morse kód: '{code}'. Csak . és - karakterek engedélyezettek."}
            if code not in REVERSE_MORSE:
                return {"error": f"Hiba! Ismeretlen morse kód: '{code}'."}
            word_str += REVERSE_MORSE[code]
        result_words.append(word_str)
    return {"result": ' '.join(result_words)}


@app.route('/')
def index():
    return render_template('input.html')


@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    text_input = data.get('text', '')
    mode = data.get('mode', '1')  # 1 = text to morse, 2 = morse to text

    if mode == '1':
        result = fordito(text_input)
        return jsonify(result)
    elif mode == '2':
        result = visszafejto(text_input)
        return jsonify(result)

    return jsonify({"error": "Ismeretlen mód"}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
