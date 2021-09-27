from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate_companies_products_report(data_list):
        companies_products_data = (
            SimpleReport.get_companies_products(data_list)
        )
        companies_products_report = "Produtos estocados por empresa: \n"
        for company_products in companies_products_data:
            companies_products_report += (
                f"- {company_products}: "
                f"{companies_products_data[company_products]}\n"
            )
        return companies_products_report

    @classmethod
    def generate(cls, data_list):
        simple_report = SimpleReport.generate(data_list)
        companies_products_report = (
            cls.generate_companies_products_report(data_list)
        )
        return simple_report + "\n" + companies_products_report
