# Existing System: Producing XML Data

import xml.etree.ElementTree as ET
import json


class StockDataXML:
    def get_data(self):
        return """
        <stock>
            <symbol>APPLE</symbol>
            <price>185.6</price>
            <volume>15000</volume>
        </stock>
        """


# Third_part Analytics Library (Can't be modified)


class AnalyticsLibraryJson:
    def analyze(self, json_data):
        data = json.loads(json_data)
        print(f"Analyzing stock data:")
        print(f"Symbol: {data['symbol']}")
        print(f"Price: ${data['price']}")
        print(f"Volume: {data['volume']}")


# Adapter: Converts XML to JSON

class XMLToJSONAdapter:
    def __init__(self, xml_data_provider):
        self.xml_data_provider = xml_data_provider

    def get_json_data(self):
        xml_data = self.xml_data_provider.get_data()
        root = ET.fromstring(xml_data)

        # Manually convert the XML to JSON like dict
        json_dict = {child.tag: child.text for child in root}
        return json.dumps(json_dict)


# Client Code Using the Adapter

def client_code():
    # Existing XML data provider
    xml_provider = StockDataXML()

    # Adapter converts XML to JSON
    adapter = XMLToJSONAdapter(xml_provider)

    # Third-party analytics library expects JSON
    analytics = AnalyticsLibraryJson()
    analytics.analyze(adapter.get_json_data())


if __name__ == "__main__":
    client_code()
