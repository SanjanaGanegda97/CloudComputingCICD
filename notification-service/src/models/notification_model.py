class Notification:
    def __init__(self, id, recipient_email, subject, message, scheduled_time=None):
        self.id = id
        self.recipient_email = recipient_email
        self.subject = subject
        self.message = message
        self.scheduled_time = scheduled_time

    def to_dict(self):
        return {
            "id": self.id,
            "recipient_email": self.recipient_email,
            "subject": self.subject,
            "message": self.message,
            "scheduled_time": self.scheduled_time,
        }
