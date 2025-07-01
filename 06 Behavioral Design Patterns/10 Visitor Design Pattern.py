from abc import ABC, abstractmethod


# ------------- ELEMENT INTERFACE -------------
class GeoNode(ABC):
    @abstractmethod
    def accept(self, visitor: 'GeoVisitor') -> None:
        ...


# ------------- CONCRETE ELEMENTS -------------
class City(GeoNode):
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def accept(self, visitor: 'GeoVisitor') -> None:
        visitor.visit_city(self)


class Industry(GeoNode):
    def __init__(self, sector: str, annual_output: float):
        self.sector = sector
        self.annual_output = annual_output

    def accept(self, visitor: 'GeoVisitor') -> None:
        visitor.visit_industry(self)


class SightSeeing(GeoNode):
    def __init__(self, name: str, rating: float):
        self.name = name
        self.rating = rating

    def accept(self, visitor: 'GeoVisitor') -> None:
        visitor.visit_sightseeing(self)


# ------------- VISITOR INTERFACE -------------
class GeoVisitor(ABC):
    @abstractmethod
    def visit_city(self, city: City) -> None:
        ...

    @abstractmethod
    def visit_industry(self, industry: Industry) -> None:
        ...

    @abstractmethod
    def visit_sightseeing(self, sight: SightSeeing) -> None:
        ...


# ------------- CONCRETE VISITOR: XML Export -------------
class XMLExportVisitor(GeoVisitor):
    def visit_city(self, city: City) -> None:
        print(f"<city><name>{city.name}</name><population>{city.population}</population></city>")

    def visit_industry(self, industry: Industry) -> None:
        print(f"<industry><sector>{industry.sector}</sector><output>{industry.annual_output}</output></industry>")

    def visit_sightseeing(self, sight: SightSeeing) -> None:
        print(f"<sight><name>{sight.name}</name><rating>{sight.rating}</rating></sight>")


# ------------- CONCRETE VISITOR: Stats Collector -------------
class StatsCollectorVisitor(GeoVisitor):
    def __init__(self):
        self.total_population = 0
        self.total_output = 0
        self.total_sights = 0

    def visit_city(self, city: City) -> None:
        self.total_population += city.population

    def visit_industry(self, industry: Industry) -> None:
        self.total_output += industry.annual_output

    def visit_sightseeing(self, sight: SightSeeing) -> None:
        self.total_sights += 1

    def report(self):
        print("---- Statistics Report ----")
        print(f"Total Population: {self.total_population}")
        print(f"Total Industry Output: {self.total_output}")
        print(f"Total Sightseeing Locations: {self.total_sights}")


# ------------- CLIENT CODE -------------
def main():
    graph = [
        City("New York", 8000000),
        Industry("Tech", 500_000_000),
        SightSeeing("Statue of Liberty", 4.9),
        City("San Francisco", 870000),
        Industry("Biotech", 300_000_000),
    ]

    print("=== Exporting to XML ===")
    xml_exporter = XMLExportVisitor()
    for node in graph:
        node.accept(xml_exporter)

    print("\n=== Collecting Stats ===")
    stats_collector = StatsCollectorVisitor()
    for node in graph:
        node.accept(stats_collector)
    stats_collector.report()


if __name__ == "__main__":
    main()
