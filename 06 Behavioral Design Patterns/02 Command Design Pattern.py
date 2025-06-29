from abc import ABC, abstractmethod


# Receiver: The actual business logic
class Editor:
    def __init__(self):
        self.text = ""
        self.clipboard = ""
        self.selection = ""

    def get_selection(self):
        return self.selection

    def delete_selection(self):
        print("Deleting selection...")
        self.text = self.text.replace(self.selection, "")
        self.selection = ""

    def replace_selection(self, new_text):
        print(f"Replacing selection with: {new_text}")
        self.text = self.text.replace(self.selection, new_text)
        self.selection = new_text

    def set_selection(self, selection):
        self.selection = selection

    def __str__(self):
        return f"Text: '{self.text}' | Selection: '{self.selection}'"


# Command Interface
class Command(ABC):
    def __init__(self, editor: Editor):
        self.editor = editor
        self._backup = ""

    def save_backup(self):
        self._backup = self.editor.text

    def undo(self):
        self.editor.text = self._backup

    @abstractmethod
    def execute(self) -> bool:
        pass


# Command History
class CommandHistory:
    def __init__(self):
        self._history = []

    def push(self, command: Command):
        self._history.append(command)

    def pop(self):
        return self._history.pop() if self._history else None


# Concrete Commands
class CopyCommand(Command):
    def execute(self):
        self.editor.clipboard = self.editor.get_selection()
        print(f"Copied: '{self.editor.clipboard}'")
        return False  # No text modified


class CutCommand(Command):
    def execute(self):
        self.save_backup()
        self.editor.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True  # Text modified


class PasteCommand(Command):
    def execute(self):
        self.save_backup()
        self.editor.replace_selection(self.editor.clipboard)
        return True  # Text modified


class UndoCommand(Command):
    def __init__(self, history: CommandHistory):
        self.history = history

    def execute(self):
        command = self.history.pop()
        if command:
            print("Undoing last command...")
            command.undo()
        else:
            print("Nothing to undo.")
        return False


# Invoker
class Application:
    def __init__(self):
        self.editor = Editor()
        self.history = CommandHistory()

    def execute_command(self, command: Command):
        if command.execute():
            self.history.push(command)

    def run(self):
        self.editor.text = "Hello, World!"
        self.editor.set_selection("World")

        print("\nInitial Editor State:", self.editor)

        # CUT
        self.execute_command(CutCommand(self.editor))
        print("After Cut:", self.editor)

        # PASTE
        self.editor.set_selection("Hello")
        self.execute_command(PasteCommand(self.editor))
        print("After Paste:", self.editor)

        # COPY
        self.editor.set_selection("Hello")
        self.execute_command(CopyCommand(self.editor))
        print("After Copy (Clipboard):", self.editor.clipboard)

        # UNDO
        undo = UndoCommand(self.history)
        self.execute_command(undo)
        print("After Undo 1:", self.editor)

        self.execute_command(undo)
        print("After Undo 2:", self.editor)


if __name__ == "__main__":
    app = Application()
    app.run()
