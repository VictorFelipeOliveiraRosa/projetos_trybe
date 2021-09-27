import os

# import csv
# import json
# import xml.etree.ElementTree as ET
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


# class CsvReader:
#     def get_data(path):
#         with open(path) as file:
#             file_reader = csv.DictReader(file)
#             data_list = []
#             for object in file_reader:
#                 data_list.append(object)
#         return data_list


# class JsonReader:
#     def get_data(path):
#         with open(path) as file:
#             content = file.read()
#             data_list = json.loads(content)
#             return data_list


# class XmlReader:
#     def get_data(path: str):
#         _arquivo, extensao = os.path.splitext(path)
#         arquivo = ET.parse(path)
#         root = arquivo.getroot()
#         filtro = "*"
#         lista_dict = []
#         dict_iten = dict()
#         for child in root.iter(filtro):
#             dict_iten[child.tag] = child.text
#             if child.tag == "record":
#                 lista_dict.append(dict_iten.copy())
#                 dict_iten.clear()
#         lista_dict.append(dict_iten)
#         lista_dict.pop(0)
#         return lista_dict


class Inventory:
    def import_data(path, type_of_report):
        _file, extension = os.path.splitext(path)
        report_types = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }
        file_types = {
            ".csv": CsvImporter.import_data,
            ".json": JsonImporter.import_data,
            ".xml": XmlImporter.import_data,
        }
        data_list = file_types[extension](path)
        return report_types[type_of_report](data_list)
