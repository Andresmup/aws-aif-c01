import csv
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()

def get_month(date):
    return date.month

def analyze_sales(file_path):
    total_revenue = 0
    product_revenue = defaultdict(int)
    date_revenue = defaultdict(int)
    monthly_sales = defaultdict(int)

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            date = parse_date(row['date'])
            product_id = row['product_id']
            price = float(row['price'])
            units_sold = int(row['units_sold'])

            revenue = price * units_sold
            total_revenue += revenue
            product_revenue[product_id] += revenue
            date_revenue[date] += revenue
            monthly_sales[get_month(date)] += units_sold

    highest_product_revenue = max(product_revenue.items(), key=lambda x: x[1])
    highest_date_revenue = max(date_revenue.items(), key=lambda x: x[1])

    print(f"Total revenue for the year: ${total_revenue:.2f}")
    print(f"Product with the highest revenue: {highest_product_revenue[0]} (${highest_product_revenue[1]:.2f})")
    print(f"Date with the highest revenue: {highest_date_revenue[0]} (${highest_date_revenue[1]:.2f})")

    months = sorted(monthly_sales.keys())
    sales = [monthly_sales[month] for month in months]

    plt.figure(figsize=(8, 6))
    plt.bar(months, sales)
    plt.xlabel('Month')
    plt.ylabel('Units Sold')
    plt.title('Monthly Sales')
    plt.show()


analyze_sales('sales.csv')
