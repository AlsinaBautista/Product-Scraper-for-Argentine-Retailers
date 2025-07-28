import scrapy
import pandas as pd
from scrapy_playwright.page import PageMethod

class CarrefourSpider(scrapy.Spider):
    name = "carrefour"

    def start_requests(self):
        df = pd.read_excel("skus_club.xlsx")  # <- Cambiá por el archivo con tus SKUs
        codigos = df["codigo"].astype(str).tolist()

        for codigo in codigos:
            url = f"https://www.carrefour.com.ar/{codigo}?_q={codigo}&map=ft"
            yield scrapy.Request(
                url=url,
                meta={
                    "playwright": True,
                    "playwright_page_methods": [PageMethod("wait_for_timeout", 2000)],
                    "codigo": codigo,
                },
                callback=self.parse
            )

    def parse(self, response):
        codigo = response.meta["codigo"]

        # Buscar el primer link de producto
        link = response.css("a.vtex-product-summary-2-x-clearLink::attr(href)").get()

        if link:
            full_url = response.urljoin(link)
            nombre = response.css("span.vtex-product-summary-2-x-productBrand::text").get()
            yield {
                "codigo": codigo,
                "nombre": nombre if nombre else "Nombre no encontrado",
                "url": full_url
            }
        else:
            yield {
                "codigo": codigo,
                "nombre": "No encontrado",
                "url": "No encontrado"
            }
