import scrapy

class ProductoItem(scrapy.Item):
    codigo = scrapy.Field()
    supermercado = scrapy.Field()
    nombre = scrapy.Field()
    url = scrapy.Field()
