# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format
sale=[]
temp=""
with open("sales.csv", "r") as file1:
    for line in file1:
        for char in line:
            if char.isdigit():
                temp+= char
        print(temp)
        num= 1#\int(temp)//100
        print(num)
        temp=""
        sale.append(num)
print(sale)

# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows