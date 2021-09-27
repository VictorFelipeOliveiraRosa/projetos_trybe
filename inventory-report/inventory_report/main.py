import sys
import os
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter


def main():
    args = sys.argv
    if len(args) < 3:
        return sys.stderr.write("Verifique os argumentos\n")
    for arg in args:
        if arg == "":
            return sys.stderr.write("Verifique os argumentos\n")
            break

    _arquivo, extensao = os.path.splitext(args[1])
    read_file = {
        ".xml": XmlImporter,
        ".json": JsonImporter,
        ".csv": CsvImporter,
    }
    instance = InventoryRefactor(read_file[extensao])
    sys.stdout.write(instance.import_data(args[1], args[2]))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
