from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

# Cho phép tất cả các nguồn (hoặc thay bằng domain cụ thể)
CORS(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()  # Nhận dữ liệu JSON
    print(f"Received data: {data}")  # In dữ liệu ra console
    return 'Data received', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
