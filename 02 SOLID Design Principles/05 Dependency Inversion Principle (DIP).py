class GmailClient:
    def send_email(self, recipient, subject, body):
        # Logic to send email using Gmail API
        pass


class EmailService:
    def __init__(self):
        self.gmail_client = GmailClient()

    def send_email(self, recipient, subject, body):
        self.gmail_client.send_email(recipient, subject, body)


class EmailClient:
    def send_email(self, recipient, subject, body):
        raise NotImplementedError


class Gmail_Client(EmailClient):
    def send_email(self, recipient, subject, body):
        # Logic to send email using Gmail API
        pass


class Outlook_Client(EmailClient):
    def send_email(self, recipient, subject, body):
        # Logic to send email using Outlook API
        pass


class Email_Service:
    def __init__(self, email_client):
        self.email_client = email_client

    def send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)


if __name__ == "__main__":
    gmail_client = Gmail_Client()
    email_service = Email_Service(gmail_client)
    email_service.send_email("xyz@gmail.com", "Subject", "abc@gamil.com")
