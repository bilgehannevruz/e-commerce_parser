import requests
from bs4 import BeautifulSoup as Soup


VISITED_PAGES = "./visited_pages.txt"


class Sitemap:
    def __init__(self, address: str):
        address = address.strip("/")
        self.address = address
        self.visited = open(VISITED_PAGES, "r+")


    @staticmethod
    def access_address(address: str):
        resp = requests.get(url=address)
        if resp.status_code != 200:
            raise Exception(f"Given {address} is not reachable!")
        return resp

    @staticmethod
    def is_product_url(content: str, buy_buttons: list):
        # Parse the page
        soup = Soup(markup=content, features="lxml")
        
        # Loop over expected buy buttons
        matches = []
        for button in buy_buttons:
            print(button)
            match = soup.find_all(text=button)
            print(match)
            if not match:
                continue
            
            matches.append("|".join(match))
        
        print(matches)
        # If not match, return False
        if not matches:
            return False
        
        return True

    def find_product_pages(self, content: str, product_set = set()):
        soup = Soup(markup=content, features="lxml")
        urls = soup.find_all(name= "a", href=True)
        for url in urls:
            url = url["href"]
            
            # Check if url is visited before
            if url in self.visited.read():
                print(f"Url already visited: {url}")
                continue
            
            # Add to visited list
            self.visited.write(f"{url}\n")

            # Create complete url
            url = self.address + url
            
            # Try to access to url
            try:
                resp = self.access_address(address=url)
            except Exception as e:
                print(e.args)
                continue
            
            # Is url a product url?
            print(f"Checking: {url}")
            product = self.is_product_url(content=resp.content, buy_buttons=["Sepete Ekle"])
            
            # If not, recurse
            if not product:
                self.find_product_pages(content=resp.content, product_set=product_set)
            
            # If product add to product_set
            print(f"Found product: {url}")
            print(product_set)
            product_set.add(url)
        
        return product_set
            

    
    def run(self):
        resp = self.access_address(address=self.address)
        urls = self.find_product_pages(content=resp.content)
        return urls
        