from abc import ABC, abstractmethod


# ---------- TEMPLATE ABSTRACT BASE CLASS ----------
class DataMiner(ABC):
    def mine(self, filepath: str) -> None:
        self.open_file(filepath)
        data = self.extract_data()
        analyzed = self.analyze_data(data)
        self.generate_report(analyzed)

    @abstractmethod
    def open_file(self, filepath: str) -> None:
        pass

    @abstractmethod
    def extract_data(self) -> list:
        pass

    def analyze_data(self, data: list) -> dict:
        print("[Analyzer] Analyzing data...")
        return {
            "total_items": len(data),
            "preview": data[:3]  # Show first 3, for example
        }

    def generate_report(self, analysis: dict) -> None:
        print("[Report] Total Items:", analysis["total_items"])
        print("[Report] Preview:", analysis["preview"])
        print("=" * 40)


# ---------- CONCRETE SUBCLASSES ----------
class CSVDataMiner(DataMiner):
    def open_file(self, filepath: str) -> None:
        print(f"[CSV] Opening CSV file: {filepath}")

    def extract_data(self) -> list:
        print("[CSV] Extracting rows from CSV")
        return ["row1", "row2", "row3", "row4"]


class DOCDataMiner(DataMiner):
    def open_file(self, filepath: str) -> None:
        print(f"[DOC] Opening DOC file: {filepath}")

    def extract_data(self) -> list:
        print("[DOC] Extracting paragraphs from DOC")
        return ["para1", "para2", "para3", "para4", "para5"]


class PDFDataMiner(DataMiner):
    def open_file(self, filepath: str) -> None:
        print(f"[PDF] Opening PDF file: {filepath}")

    def extract_data(self) -> list:
        print("[PDF] Extracting text from PDF")
        return ["text1", "text2", "text3"]


# ---------- CLIENT CODE ----------
def main():
    print("🗂 Processing CSV file:")
    miner = CSVDataMiner()
    miner.mine("file.csv")

    print("🗂 Processing DOC file:")
    miner = DOCDataMiner()
    miner.mine("file.doc")

    print("🗂 Processing PDF file:")
    miner = PDFDataMiner()
    miner.mine("file.pdf")


if __name__ == "__main__":
    main()
