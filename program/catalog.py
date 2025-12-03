# catalog.py

CAKE_CATALOG = [
    {"cake_id": "C001", "name": "Bánh bông lan", "price": 120000},
    {"cake_id": "C002", "name": "Bánh kem socola", "price": 150000},
    {"cake_id": "C003", "name": "Bánh tart trái cây", "price": 180000},
    {"cake_id": "C004", "name": "Bánh crepe", "price": 110000},
    {"cake_id": "C005", "name": "Bánh mousse", "price": 200000},

    # 🎂 Thêm bánh mới
    {"cake_id": "C006", "name": "Bánh tiramisu", "price": 220000},
    {"cake_id": "C007", "name": "Bánh flan caramel", "price": 60000},
    {"cake_id": "C008", "name": "Bánh brownie", "price": 140000},
    {"cake_id": "C009", "name": "Bánh donut", "price": 25000},
    {"cake_id": "C010", "name": "Bánh macarons", "price": 180000},
    {"cake_id": "C011", "name": "Bánh croissant", "price": 35000},
    {"cake_id": "C012", "name": "Bánh cupcake", "price": 45000},
    {"cake_id": "C013", "name": "Bánh su kem", "price": 30000},
    {"cake_id": "C014", "name": "Bánh cheesecake", "price": 190000},
    {"cake_id": "C015", "name": "Bánh opera", "price": 230000},
]

def list_cakes():
    print("\n--- DANH SÁCH BÁNH ---")
    for c in CAKE_CATALOG:
        print(f"{c['cake_id']}: {c['name']} - {c['price']:,} VND")
    print("----------------------\n")

def find_cake(cake_id: str):
    for c in CAKE_CATALOG:
        if c["cake_id"] == cake_id:
            return c
    return None