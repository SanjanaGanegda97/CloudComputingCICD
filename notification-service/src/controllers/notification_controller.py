from flask import Flask, request, jsonify
from services.notification_service import NotificationService

app = Flask(__name__)
notification_service = NotificationService()

@app.route('/notifications', methods=['POST'])
def send_notification():
    data = request.json
    result = notification_service.send_notification(data)
    return jsonify(result), 200

@app.route('/notifications/schedule', methods=['POST'])
def schedule_notification():
    data = request.json
    result = notification_service.schedule_notification(data)
    return jsonify(result), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
