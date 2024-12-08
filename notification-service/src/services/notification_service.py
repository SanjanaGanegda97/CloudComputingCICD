from models.notification_model import Notification
from utils.email_client import EmailClient

class NotificationService:
    def __init__(self):
        self.notifications = {}
        self.email_client = EmailClient()

    def send_notification(self, data):
        notification = Notification(**data)
        self.email_client.send_email(notification.to_dict())
        return {"message": "Notification sent"}

    def schedule_notification(self, data):
        notification = Notification(**data)
        self.notifications[notification.id] = notification
        return {"message": "Notification scheduled", "id": notification.id}
