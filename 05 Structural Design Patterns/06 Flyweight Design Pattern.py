# Flyweight

from typing import List, Dict, Tuple


class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        print(f"[Drawing] {self.name} tree at ({x}, {y})"
              f"with color {self.color} and texture {self.texture} on {canvas}")


# Flyweight Factory

class TreeFactory:
    _tree_types: Dict[Tuple[str, str, str], TreeType] = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = (name, color, texture)

        if key not in cls._tree_types:
            print(f"[Factory] Creating a new treeType: {key}")
            cls._tree_types[key] = TreeType(name, color, texture)
        else:
            print(f"[factory] Reusing existing TreeType: {key}")
        return cls._tree_types[key]


# Context

class Tree:
    def __init__(self, x, y, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas):
        self.tree_type.draw(canvas, self.x, self.y)


# Client

class Forest:
    def __init__(self):
        self.trees: List[Tree] = []

    def plant_tree(self, x, y, name, color, texture):
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, tree_type)
        self.trees.append(tree)

    def draw(self, canvas):
        for tree in self.trees:
            tree.draw(canvas)


# Demo

if __name__ == "__main__":
    forest = Forest()

    # Plant many trees but with only 2 types
    for i in range(0, 10, 2):
        forest.plant_tree(i, i + 1, "Oak", "Green", "Rough")
        forest.plant_tree(i + 1, i + 2, "Pine", "Dark green", "Smooth")

    print("\n=========Drawing Forest========")
    forest.draw("Canvas1")
