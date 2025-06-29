from abc import ABC, abstractmethod


# -------------------- Mediator Interface --------------------
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str):
        pass


# -------------------- Base Component --------------------
class Component:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    def set_mediator(self, mediator: Mediator):
        self._mediator = mediator


# -------------------- Concrete Components --------------------
class Button(Component):
    def click(self):
        print("[Button Clicked]")
        self._mediator.notify(self, "click")


class Checkbox(Component):
    def __init__(self, mediator=None):
        super().__init__(mediator)
        self.checked = False

    def toggle(self):
        self.checked = not self.checked
        print(f"[Checkbox Toggled] checked = {self.checked}")
        self._mediator.notify(self, "check")


class Textbox(Component):
    def __init__(self, mediator=None):
        super().__init__(mediator)
        self.visible = True
        self.content = ""

    def set_visible(self, visible: bool):
        self.visible = visible
        print(f"[Textbox] {'Shown' if visible else 'Hidden'}")

    def set_content(self, content: str):
        self.content = content


# -------------------- Concrete Mediator --------------------
class AuthenticationDialog(Mediator):
    def __init__(self):
        # Components
        self.title = "Dialog"
        self.login_checkbox = Checkbox(self)
        self.username_login = Textbox(self)
        self.password_login = Textbox(self)

        self.username_register = Textbox(self)
        self.password_register = Textbox(self)
        self.email_register = Textbox(self)

        self.ok_button = Button(self)
        self.cancel_button = Button(self)

        self.set_initial_state()

    def set_initial_state(self):
        self.title = "Login"
        self.username_login.set_visible(True)
        self.password_login.set_visible(True)

        self.username_register.set_visible(False)
        self.password_register.set_visible(False)
        self.email_register.set_visible(False)

    def notify(self, sender: object, event: str):
        if sender == self.login_checkbox and event == "check":
            if self.login_checkbox.checked:
                self.title = "Login"
                print("\n[Dialog switched to Login mode]")
                self.username_login.set_visible(True)
                self.password_login.set_visible(True)
                self.username_register.set_visible(False)
                self.password_register.set_visible(False)
                self.email_register.set_visible(False)
            else:
                self.title = "Register"
                print("\n[Dialog switched to Registration mode]")
                self.username_login.set_visible(False)
                self.password_login.set_visible(False)
                self.username_register.set_visible(True)
                self.password_register.set_visible(True)
                self.email_register.set_visible(True)

        elif sender == self.ok_button and event == "click":
            if self.login_checkbox.checked:
                print("\n[Logging in user...]")
                # In real code, validate login form
                if not self.username_login.content or not self.password_login.content:
                    print("Login failed: Missing username or password.")
                else:
                    print(f"Login success for user: {self.username_login.content}")
            else:
                print("\n[Registering new user...]")
                # In real code, validate registration form
                if not self.username_register.content or not self.password_register.content or not self.email_register.content:
                    print("Registration failed: Missing fields.")
                else:
                    print(f"User {self.username_register.content} registered with email {self.email_register.content}.")


# -------------------- Application (Client Code) --------------------
def main():
    dialog = AuthenticationDialog()

    # Toggle between login and register
    dialog.login_checkbox.toggle()  # Switch to Login
    dialog.username_login.set_content("john_doe")
    dialog.password_login.set_content("123456")
    dialog.ok_button.click()

    print("\n---\n")

    dialog.login_checkbox.toggle()  # Switch to Register
    dialog.username_register.set_content("jane_doe")
    dialog.password_register.set_content("abcdef")
    dialog.email_register.set_content("jane@example.com")
    dialog.ok_button.click()


if __name__ == "__main__":
    main()
