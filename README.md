# Product-Scraper-for-Argentine-Retailers
Web scraper for searching EAN-coded products across multiple Argentine retail sites and exporting results to Excel.
🛒 Product Scraper for Argentine Retailers
This project is a web scraper built with Scrapy to search for products by EAN codes across multiple Argentine retail websites such as Carrefour, Jumbo, Disco, Vea, Farmacity, Mercado Libre, and more.
Given an Excel file containing EANs, the scraper performs the following:
-Searches each product on supported sites
-Extracts the product name and URL (or marks as "Not Found")
-Exports results to a new Excel file
-Useful for price comparisons, stock monitoring, and market research.

🛠 Tech Stack
-Python 3.11+
-Scrapy
-Pandas
-OpenPyXL

📂 Input Format
Upload an Excel file (.xlsx) with a column named ean containing EAN codes.

📤 Output
A new Excel file with the product name and link (or a note if not found) per retailer.
