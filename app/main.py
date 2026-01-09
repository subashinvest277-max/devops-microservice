from flask import Flask, jsonify
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from DevOps Microservice v1",
        "environment": app.config["ENVIRONMENT"]
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
