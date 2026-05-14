import numpy as np
import csv

products = []
prices = []
stocks = []
sales = []

with open("Grocery_Inventory_and_Sales_Dataset.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for row in reader:
        # 商品名稱
        products.append(row["Product_Name"])

        # 去掉 "$" 轉為浮點數
        raw_price = row["Unit_Price"].replace("$", "").strip()
        prices.append(float(raw_price))

        # 取得庫存量與銷售量
        stocks.append(float(row["Stock_Quantity"]))
        sales.append(float(row["Sales_Volume"]))

# 轉為 NumPy
products = np.array(products)
prices = np.array(prices)
stocks = np.array(stocks)
sales = np.array(sales)

# 總庫存價值
total_value = stocks * prices

# 最暢銷商品
hot_index = np.argmax(sales)

# 計算 9 折後
discount_income = sales * prices * 0.9

with open("GIaSD_Fixed.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Product", "Stock", "Inventory_Value", "90_Percent_Income", "Is_Hot_Seller"])

    for i in range(len(products)):
        w.writerow([
            products[i],
            stocks[i],
            total_value[i],
            discount_income[i],
            "YES" if i == hot_index else "NO"
        ])
