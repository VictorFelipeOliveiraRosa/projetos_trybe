from typing import List
from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET
import os


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str) -> List[dict]:
        _arquivo, extensao = os.path.splitext(path)
        if extensao != ".xml":
            raise ValueError("Arquivo inválido")
        arquivo = ET.parse(path)
        root = arquivo.getroot()
        filtro = "*"
        lista_dict = []
        dict_iten = dict()
        for child in root.iter(filtro):
            dict_iten[child.tag] = child.text
            if child.tag == "record":
                del dict_iten["record"]
                lista_dict.append(dict_iten.copy())
                dict_iten.clear()
        lista_dict.append(dict_iten)
        lista_dict.pop(0)
        return lista_dict
