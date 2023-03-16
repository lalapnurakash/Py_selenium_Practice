import random

# Ignore these for now. You'll use them in a sec ;)
from openpyxl import Workbook, chart
from openpyxl.chart import Reference

from p_1 import Product, Sale

products = []

# Let's create 5 products
for idx in range(1, 6):
   sales = []

# Create 5 months of sales
   for _ in range(5):
        sale = Sale(quantity=random.randrange(5, 100))
        sales.append(sale)
   product = Product(id=str(idx),
                        name="Product %s" % idx,
                      sales=sales)
products.append(product)
workbook = Workbook()
sheet = workbook.active

# Append column names first
sheet.append(["Product ID", "Product Name", "Month 1",
                  "Month 2", "Month 3", "Month 4", "Month 5"])

    # Append the data
for product in products:
 data = [product.id, product.name]
for sale in product.sales:
        data.append(sale.quantity)
        sheet.append(data)



workbook.save(filename="oop_sample.xlsx")