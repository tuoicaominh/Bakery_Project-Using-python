# order_file.py

import csv
import os

ORDER_FILE = "data/order.txt"

def ensure():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(ORDER_FILE):
        open(ORDER_FILE, "w").close()

def order_to_row(o):
    return [
        o["order_id"], o["username"], o["cake_id"], o["cake_name"],
        o["quantity"], o.get("notes", ""), o.get("status", "pending")
    ]

def row_to_order(row):
    return {
        "order_id": row[0],
        "username": row[1],
        "cake_id": row[2],
        "cake_name": row[3],
        "quantity": int(row[4]),
        "notes": row[5],
        "status": row[6],
    }

def load_orders():
    ensure()
    orders = []
    with open(ORDER_FILE, "r", encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                orders.append(row_to_order(row))
    return orders

def write_orders(orders):
    with open(ORDER_FILE, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for o in orders:
            writer.writerow(order_to_row(o))

def append_order(order):
    with open(ORDER_FILE, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(order_to_row(order))