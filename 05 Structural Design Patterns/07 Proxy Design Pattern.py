# Image Viewer Code using - Proxy Pattern

from abc import ABC, abstractmethod


# Subject Interface

class Image(ABC):
    @abstractmethod
    def display(self):
        ...


# The real object (Heavy to load)

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"[RealImage] Loading from disk: {self.filename}")

    def display(self):
        print(f"[RealImage] Displaying the image: {self.filename}")


# The Proxy Object

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.realImage = None

    def display(self):
        # Load only when needed
        if self.realImage is None:
            print(f"[ProxyImage] Creating RealImage for the first time...")
            self.realImage = RealImage(self.filename)
        else:
            print(f"[proxyImage] RealImage is already loaded")
        self.realImage.display()


# Client Code

if __name__ == "__main__":
    print("Client: creating Image1")
    image1 = ProxyImage("cat_photo.jpg")

    print("\nClient: First call to display image1")
    image1.display()

    print("\nClient: Second call to display image1")
    image1.display()
