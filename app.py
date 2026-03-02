from flask import Flask, jsonify
import os 

app = Flask(__name__)

APP_ENV = os.getenv('APP_ENV', 'development')

@app.route('/')
def home():
    return f"DevOps API is Running in {APP_ENV} environment"

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "environment": APP_ENV
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)