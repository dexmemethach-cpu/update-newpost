from flask import Flask, request
import requests

app = Flask(__name__)

# Telegram Bot Token và Chat ID
bot_token = "8106631505:AAFq8iqagLhsCh8Vr_P0lpdMljGoyJmZOu8"  # Thay bằng token của bạn
chat_id = "-1003174496663"  # Thay bằng chat ID của bạn

# Hàm gửi tin nhắn tới Telegram
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    return response

# Nhận dữ liệu từ Webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()  # Nhận dữ liệu JSON từ Webhook
    message = f"Received data: {data}"  # Định dạng tin nhắn
    send_to_telegram(message)  # Gửi tin nhắn đến Telegram
    return 'Data received and sent to Telegram', 200

if __name__ == '__main__':
    app.run(debug=True)
