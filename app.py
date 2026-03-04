from flask import Flask, request,jsonify
import os 
import psycopg2
import time

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST','db')
DB_NAME =os.getenv('DB_NAME', 'tasksdb')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
APP_ENV = os.getenv('APP_ENV', 'development')

@app.route('/')
def home():
    return f"DevOps API is Running in {APP_ENV} environment"

def get_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            return conn
        except:
            time.sleep(4)
    raise Exception("Could not connect to the database")

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, name TEXT);")
    conn.commit()
    cur.close()
    conn.close()

@app.route ('/tasks', methods=['POST'])
def add_task():
    data = request.json
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (name) VALUES (%s);", (data['name'],))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Task added successfully"})  

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute ("SELECT * FROM tasks;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "environment": APP_ENV
    })

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)