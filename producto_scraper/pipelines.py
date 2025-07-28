import openpyxl

class ProductoScraperPipeline:
    def open_spider(self, spider):
        # Creamos el libro Excel
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = "Resultados"

        # Escribimos los encabezados
        self.sheet.append(["Sitio", "Código EAN", "Nombre Producto", "URL"])

    def process_item(self, item, spider):
        # Agregamos una fila por cada ítem
        self.sheet.append([
            item.get("sitio", spider.name),
            item.get("ean", ""),
            item.get("nombre", ""),
            item.get("url", "")
        ])
        return item

    def close_spider(self, spider):
        # Guardamos el archivo Excel con nombre basado en el spider
        nombre_archivo = f"resultados_{spider.name}.xlsx"
        self.workbook.save(nombre_archivo)
        print(f"\n📁 Resultados guardados en: {nombre_archivo}")

