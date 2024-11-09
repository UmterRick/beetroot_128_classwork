class EmailService:
    def send_mail(self, msg):
        print(f"Seng {msg}")


class Notification:
    def __init__(self):
        self.email_service = EmailService()

    def send_notification(self, msg):
        self.email_service.send_mail(msg)





###################################################

class MessageService:
    def send(self, msg):
        pass


class NewEmailService(MessageService):
    def send(self, msg):
        print(f"Send E-Mail: {msg}")


class SMSService(MessageService):
    def send(self, msg):
        print(f"Send SMS: {msg}")



class ViberMessage(MessageService):
    def send(self, msg):
        print(f"Send to Viber: {msg}")



class NewNotification:
    def __init__(self, service: MessageService):
        self.service = service

    def send_notification(self, msg):
        self.service.send(msg)
