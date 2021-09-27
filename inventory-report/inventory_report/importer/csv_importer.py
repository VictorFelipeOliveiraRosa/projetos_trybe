import csv
import os
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        _arquivo, extensao = os.path.splitext(path)
        if extensao != ".csv":
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            file_reader = csv.DictReader(file)
            data_list = []
            for object in file_reader:
                data_list.append(object)
            for item in data_list:
                if "record" in item:
                    del item["record"]
            return data_list
