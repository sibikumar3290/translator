from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"translated": ""})

    try:
        result = translator.translate(text, dest="en")
        return jsonify({"translated": result.text})
    except Exception:
        return jsonify({"translated": "Translation failed"})

if __name__ == "__main__":
    app.run(debug=True)
