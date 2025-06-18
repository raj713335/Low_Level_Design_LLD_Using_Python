# Define common Interface

from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        ...


# Implement the concreate Component (Basic Email Notification)

class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Sending EMAIL with message: {message}")


# Create the Base Decorator

class NotifierDecorator(Notifier):
    def __init__(self, wrapper: Notifier):
        self._wrapper = wrapper

    def send(self, message: str):
        self._wrapper.send(message)


# Create Concreate Decorator (SMS, Slack, Facebook)

class SMSNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        self.send_sms(message)

    def send_sms(self, message: str):
        print(f"Sending SMS with message: {message}")


class FacebookNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        self.send_facebook(message)

    def send_facebook(self, message: str):
        print(f"Sending Facebook with message: {message}")


class SlackNotifier(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        self.send_slack(message)

    def send_slack(self, message: str):
        print(f"Sending Slack with message: {message}")


# Client Code (Runtime composition with Decorators)

if __name__ == "__main__":
    # Basic notifier (email only)
    notifier = EmailNotifier()

    # wrap with SMS and Slack decorators
    notifier = SMSNotifier(notifier)
    notifier = SlackNotifier(notifier)
    notifier = FacebookNotifier(notifier)

    # Client Sends one message - it flows through all decorators
    notifier.send("Alert: Server CPU usage exceeded 90% threshold")


# Addition of numbers using a decorators

def sumx(func):
    def wrapper(*args, **kwargs):
        result = sum(args)
        return func(result, **kwargs)
    return wrapper

@sumx
def sum_numbers(result):
    return f"Sum of numbers is: {result}"

print(sum_numbers(1, 3, 4, 8, 9))
