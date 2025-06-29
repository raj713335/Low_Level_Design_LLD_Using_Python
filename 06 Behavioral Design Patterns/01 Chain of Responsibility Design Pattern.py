from abc import ABC, abstractmethod

# Request object that holds user and requested daya

class Request:
    def __init__(self, username, password, role, data):
        self.username = username
        self.password = password
        self.role = role
        self.data = data

# Abstract Handler
class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Request):
        pass

# Concreate Handler 1: Authentication
class AuthHandler(Handler):
    def handle(self, request: Request):
        print("[AuthHandler] Checking authentication...")
        if request.username == "john" and request.password == "1234":
            print("Authenticated")
            if self._next_handler:
                return self._next_handler.handle(request)
        else:
            print("Authentication failed")
            return "Access Denied: Invalid Credentials"



# Concrete Handler 2: Authorization
class RoleHandler(Handler):
    def handle(self, request: Request):
        print("[RoleHandler] Checking role...")
        if request.role == "admin" or request.role == "user":
            print(f"Authorized as {request.role}")
            if self._next_handler:
                return self._next_handler.handle(request)
        else:
            print("Authorization failed")
            return "Access Denied: Unauthorized Role"


# Concrete Handler 3: Validation
class ValidationHandler(Handler):
    def handle(self, request: Request):
        print("[ValidationHandler] Validating request data...")
        if "item" in request.data and "quantity" in request.data:
            print("Request data is valid")
            if self._next_handler:
                return self._next_handler.handle(request)
        else:
            print("Invalid request data")
            return "Bad Request: Missing order details"

# Final Handler: Order Handler
class OrderHandler(Handler):
    def handle(self, request: Request):
        print(f"[OrderHandler] Processing order...")
        return f"Order Placed for {request.data['quantity']} x {request.data['item']} by {request.username}"

# Client Code

if __name__ == "__main__":
    auth = AuthHandler()
    role = RoleHandler()
    validate = ValidationHandler()
    order = OrderHandler()

    auth.set_next(role).set_next(role).set_next(validate).set_next(order)

    # Request Valid
    # Request 1: Valid
    print("\n--- Request 1: Valid Order ---")
    request1 = Request("john", "1234", "admin", {"item": "Laptop", "quantity": 2})
    response1 = auth.handle(request1)
    print("Response:", response1)

    # Request 2: Invalid password
    print("\n--- Request 2: Invalid Credentials ---")
    request2 = Request("john", "wrong", "admin", {"item": "Laptop", "quantity": 2})
    response2 = auth.handle(request2)
    print("Response:", response2)

    # Request 3: Unauthorized Role
    print("\n--- Request 3: Unauthorized Role ---")
    request3 = Request("john", "1234", "guest", {"item": "Laptop", "quantity": 2})
    response3 = auth.handle(request3)
    print("Response:", response3)

    # Request 4: Missing Data
    print("\n--- Request 4: Missing Order Data ---")
    request4 = Request("john", "1234", "user", {"item": "Mouse"})
    response4 = auth.handle(request4)
    print("Response:", response4)


