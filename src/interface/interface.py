from src.parser import Parser
from src.sitemap import Sitemap


class Interface:

    @staticmethod
    def create_sitemap(address):
        sitemap = Sitemap(address=address)
        print("Sitemap has been created successfully!")
        return sitemap

    @staticmethod
    def create_parser(sitemap):
        parser = Parser(sitemap=sitemap)
        print("Parser has been created successfully!")
        return parser
    
    @staticmethod
    def run(sitemap: Sitemap, parser: Parser):
        print("Starting to find products")
        urls = sitemap.run()
        print(urls)
        return "Completely parsed the website"
