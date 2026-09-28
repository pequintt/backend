from datetime import datetime
from pathlib import Path
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
DATA_FILE = Path(__file__).with_name("data.txt")

@app.post("/api/data")
def save_data():
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()

    if not text:
        return jsonify({
            "error": "Поле не должно быть пустым"
        }), 400

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write(f"[{current_time}] {text}\n")

    return jsonify({
        "message": "Данные успешно сохранены"
    })

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )