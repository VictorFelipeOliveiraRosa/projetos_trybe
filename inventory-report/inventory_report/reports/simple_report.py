from datetime import date


class SimpleReport():
    def get_latest_manufacturing_date(data_list):
        latest_manufacturing_date = data_list[0]['data_de_fabricacao']
        for product in data_list:
            if (
               date.fromisoformat(product['data_de_fabricacao'])
               <
               date.fromisoformat(latest_manufacturing_date)
               ):
                latest_manufacturing_date = product['data_de_fabricacao']
        return latest_manufacturing_date

    def get_closest_expiration_date(data_list):
        closest_expiration_date = data_list[0]['data_de_validade']
        for product in data_list:
            if (
               date.today()
               <
               date.fromisoformat(product['data_de_validade'])
               <
               date.fromisoformat(closest_expiration_date)
               ):
                closest_expiration_date = product['data_de_validade']
        return closest_expiration_date

    def get_companies_products(data_list):
        companies_products = {
            product["nome_da_empresa"]: 0 for product in data_list
        }
        for product in data_list:
            companies_products[product["nome_da_empresa"]] += 1
        return companies_products

    @classmethod
    def get_company_with_most_products(cls, data_list):
        companies_products = cls.get_companies_products(data_list)
        return [
            company_name for company_name in companies_products
            if companies_products[company_name]
            == max(companies_products.values())
        ][0]

    @classmethod
    def generate(cls, data_list):
        return (
            "Data de fabricação mais antiga: "
            f"{cls.get_latest_manufacturing_date(data_list)}\n"
            "Data de validade mais próxima: "
            f"{cls.get_closest_expiration_date(data_list)}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{cls.get_company_with_most_products(data_list)}\n"
        )
