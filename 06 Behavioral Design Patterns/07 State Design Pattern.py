from abc import ABC, abstractmethod


# -------------- STATE INTERFACE ----------------
class State(ABC):
    def __init__(self, document):
        self.document = document

    @abstractmethod
    def edit(self):
        ...

    @abstractmethod
    def publish(self, user_role: str):
        ...


# -------------- CONCRETE STATES ----------------
class DraftState(State):
    def edit(self):
        print("[Draft] You can freely edit the document.")

    def publish(self, user_role: str):
        print("[Draft] Moving to moderation.")
        self.document.change_state(ModerationState(self.document))


class ModerationState(State):
    def edit(self):
        print("[Moderation] Document is under review. Limited editing allowed.")

    def publish(self, user_role: str):
        if user_role.lower() == "admin":
            print("[Moderation] Approved by admin. Document is now published.")
            self.document.change_state(PublishedState(self.document))
        else:
            print("[Moderation] Only admins can publish from moderation.")


class PublishedState(State):
    def edit(self):
        print("[Published] Cannot edit a published document.")

    def publish(self, user_role: str):
        print("[Published] Document is already published. No action taken.")


# -------------- CONTEXT ----------------
class Document:
    def __init__(self):
        self._state: State = DraftState(self)
        print("[Document] Initialized in Draft state.")

    def change_state(self, new_state: State):
        self._state = new_state
        print(f"[Document] State changed to {self._state.__class__.__name__}.")

    def edit(self):
        self._state.edit()

    def publish(self, user_role: str):
        self._state.publish(user_role)


# -------------- CLIENT CODE ----------------
def main():
    document = Document()

    document.edit()                # Allowed
    document.publish("writer")     # Moves to Moderation

    document.edit()                # Limited edit
    document.publish("user")       # Denied (not admin)

    document.publish("admin")      # Published

    document.edit()                # Not allowed
    document.publish("admin")      # Already published


if __name__ == "__main__":
    main()
