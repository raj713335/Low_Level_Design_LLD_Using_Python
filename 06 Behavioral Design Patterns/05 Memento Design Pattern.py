from typing import List


# ----------- MEMENTO -----------
class Snapshot:
    """The Memento that stores the state of the Editor."""

    def __init__(self, text: str, cursor_position: int):
        self._text = text
        self._cursor_position = cursor_position

    def get_state(self):
        """Internal state is only accessible to the Editor."""
        return self._text, self._cursor_position


# ----------- ORIGINATOR -----------
class Editor:
    """Originator that creates and restores from Snapshots."""

    def __init__(self):
        self._text = ""
        self._cursor_position = 0

    def type(self, new_text: str):
        self._text += new_text
        self._cursor_position = len(self._text)

    def get_content(self):
        return self._text

    def create_snapshot(self) -> Snapshot:
        return Snapshot(self._text, self._cursor_position)

    def restore(self, snapshot: Snapshot):
        self._text, self._cursor_position = snapshot.get_state()


# ----------- CARETAKER -----------
class History:
    """Caretaker that stores snapshots for undo functionality."""

    def __init__(self):
        self._snapshots: List[Snapshot] = []

    def save(self, snapshot: Snapshot):
        self._snapshots.append(snapshot)

    def undo(self) -> Snapshot:
        if not self._snapshots:
            print("[Undo] No more states to undo.")
            return None
        snapshot = self._snapshots.pop()
        print("[Undo] Restoring previous state.")
        return snapshot


# ----------- CLIENT CODE -----------
def main():
    editor = Editor()
    history = History()

    editor.type("Hello")
    history.save(editor.create_snapshot())

    editor.type(" World!")
    history.save(editor.create_snapshot())

    print("[Editor] Current content:", editor.get_content())  # Hello World!

    editor.type(" Let's learn Memento.")
    print("[Editor] Current content:", editor.get_content())  # Hello World! Let's learn Memento.

    # Perform undo
    snapshot = history.undo()
    if snapshot:
        editor.restore(snapshot)
        print("[Editor] After undo:", editor.get_content())  # Hello World!

    # Another undo
    snapshot = history.undo()
    if snapshot:
        editor.restore(snapshot)
        print("[Editor] After second undo:", editor.get_content())  # Hello

    snapshot = history.undo()
    if snapshot:
        editor.restore(snapshot)
        print("[Editor] After Third undo:", editor.get_content())



if __name__ == "__main__":
    main()
