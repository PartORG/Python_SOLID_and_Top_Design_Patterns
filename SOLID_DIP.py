from abc import ABC, abstractmethod

# BAD CLASSES - violates Dependency Inversion Principle
class EmailService:
    def send_email(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")

class SmsService:
    def send_sms(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver}")

# it has direct dependency on concrete classes
class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()

    def send_notification(self, message, receiver, method):
        if method == "email":
            self.email_service.send_email(message, receiver)
        elif method == "sms":
            self.sms_service.send_sms(message, receiver)


# GOOD CLASSES - now class depends on abstraction:
class IMessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass

class EmailService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")

class SmsService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver}")

class NotificationService:
    def __init__(self, message_service: IMessageService):
        self.message_service = message_service

    def send_notification(self, message, receiver):
        self.message_service.send(message, receiver)
