class EmailClient:
    def send_email(self, notification_data):
        print(f"Sending email to {notification_data['recipient_email']}")
        print(f"Subject: {notification_data['subject']}")
        print(f"Message: {notification_data['message']}")
