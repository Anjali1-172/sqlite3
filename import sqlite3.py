import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create/connect to DB
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()


# Step 3: Insert sample data (if needed)
sample_data = [
    ("2024-01-01", "Widget A", 10, 5.0),
    ("2024-01-02", "Widget B", 7, 7.5),
    ("2024-01-03", "Widget A", 3, 5.0),
    ("2024-01-04", "Widget C", 8, 6.0),
    ("2024-01-05", "Widget B", 5, 7.5),
]

cursor.executemany("INSERT INTO sales_data(date, product, quantity, price) VALUES (?, ?, ?, ?)", sample_data)
conn.commit()

# Step 4: Query data
df = pd.read_sql_query("""
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
""", conn)

print(df)

# Step 5: Visualize
plt.figure(figsize=(8, 4))

# Bar plot: total quantity per product
plt.subplot(1, 2, 1)
plt.bar(df['product'], df['total_qty'], color='skyblue')
plt.title("Total Quantity Sold")
plt.ylabel("Quantity")
plt.xticks(rotation=45)

# Bar plot: revenue per product
plt.subplot(1, 2, 2)
plt.bar(df['product'], df['revenue'], color='orange')
plt.title("Revenue per Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

conn.close()
