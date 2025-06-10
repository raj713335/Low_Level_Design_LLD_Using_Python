from abc import ABC, abstractmethod
import copy

# Prototype Interface

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        ...

# Concreate Prototype

class Cell(Prototype):
    def __init__(self, dna: str, cell_type: str, age: int):
        self.dna = dna
        self.cell_type = cell_type
        self.age = age
        self.organelles = ["nucleus", 'mitochondria', "ribosome"]

    def clone(self):
        return copy.deepcopy(self)

    def mutate(self, new_dna):
        self.dna = new_dna

    def __str__(self):
        return f"Cell(type={self.cell_type}, dna={self.dna}, age={self.age}, organelles={self.organelles})"

# Client Code

if __name__ == "__main__":
    # Original Prototype

    original_cell = Cell(dna="ATGC", cell_type="stem", age=1)
    print("Original: ", original_cell)

    # Cloning the prototype

    clone1 = original_cell.clone()
    clone1.age += 1
    clone1.mutate("ATGA")
    print("Clone 1: ", clone1)

    clone2 = original_cell.clone()
    clone2.organelles.append("chloroplast")
    print("Clone 2:", clone2)

    print("Original after Cloning: ", original_cell)