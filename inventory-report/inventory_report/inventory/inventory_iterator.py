from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, product) -> None:
        self.list_product = product
        self.contador = -1

    def __next__(self):
        self.contador += 1
        try:
            return self.list_product[self.contador]
        except IndexError:
            raise StopIteration()
