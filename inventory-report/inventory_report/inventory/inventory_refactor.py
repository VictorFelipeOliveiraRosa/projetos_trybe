from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.importer.importer import Importer
from typing import Type

# from inventory_report.importer.xml_importer import XmlImporter
# from inventory_report.importer.json_importer import JsonImporter
# from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer: Type[Importer]) -> None:
        self.importer = importer
        self.data = []

    def __str__(self):
        return self.data

    def __iter__(self):
        return InventoryIterator(self.data)

    def add_products(self, data: list):
        for x in data:
            self.data.append(x)

    def import_data(self, path, type_of_report):
        report_types = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }

        data_list = self.importer.import_data(path)
        self.add_products(data_list)
        return report_types[type_of_report](data_list)
