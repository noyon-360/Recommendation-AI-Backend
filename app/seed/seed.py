from datetime import datetime, timedelta, timezone

from app.db.mongodb import db

# ---------------------------------------------------------------------------
# Products — spread across 8 categories, 5 items each
# ---------------------------------------------------------------------------
products = [
    {"_id": "p1", "name": "Wireless Mouse", "category": "Electronics", "price": 19.99},
    {"_id": "p2", "name": "Mechanical Keyboard", "category": "Electronics", "price": 59.99},
    {"_id": "p3", "name": "Bluetooth Headphones", "category": "Electronics", "price": 49.99},
    {"_id": "p4", "name": "Smartwatch", "category": "Electronics", "price": 129.99},
    {"_id": "p5", "name": "Laptop Stand", "category": "Electronics", "price": 22.50},

    {"_id": "p6", "name": "Running Shoes", "category": "Sportswear", "price": 45.00},
    {"_id": "p7", "name": "Yoga Mat", "category": "Sportswear", "price": 25.50},
    {"_id": "p8", "name": "Gym Gloves", "category": "Sportswear", "price": 15.00},
    {"_id": "p9", "name": "Sports Water Bottle", "category": "Sportswear", "price": 12.00},
    {"_id": "p10", "name": "Track Jacket", "category": "Sportswear", "price": 55.00},

    {"_id": "p11", "name": "Coffee Maker", "category": "Home", "price": 89.99},
    {"_id": "p12", "name": "Blender", "category": "Home", "price": 39.99},
    {"_id": "p13", "name": "Air Purifier", "category": "Home", "price": 120.00},
    {"_id": "p14", "name": "Table Lamp", "category": "Home", "price": 28.00},
    {"_id": "p15", "name": "Non-stick Pan Set", "category": "Home", "price": 65.00},

    {"_id": "p16", "name": "The Great Journey (Novel)", "category": "Books", "price": 12.99},
    {"_id": "p17", "name": "Easy Meals Cookbook", "category": "Books", "price": 15.99},
    {"_id": "p18", "name": "Atomic Habits", "category": "Books", "price": 18.50},
    {"_id": "p19", "name": "Sci-Fi Anthology", "category": "Books", "price": 14.00},
    {"_id": "p20", "name": "Kids Story Collection", "category": "Books", "price": 9.99},

    {"_id": "p21", "name": "Face Moisturizer", "category": "Beauty", "price": 14.99},
    {"_id": "p22", "name": "Vitamin C Serum", "category": "Beauty", "price": 22.00},
    {"_id": "p23", "name": "Hair Dryer", "category": "Beauty", "price": 34.99},
    {"_id": "p24", "name": "Lipstick Set", "category": "Beauty", "price": 19.99},
    {"_id": "p25", "name": "Sunscreen SPF50", "category": "Beauty", "price": 16.50},

    {"_id": "p26", "name": "Building Blocks Set", "category": "Toys", "price": 24.99},
    {"_id": "p27", "name": "Remote Control Car", "category": "Toys", "price": 39.99},
    {"_id": "p28", "name": "Puzzle 1000pcs", "category": "Toys", "price": 17.50},
    {"_id": "p29", "name": "Plush Teddy Bear", "category": "Toys", "price": 12.99},
    {"_id": "p30", "name": "Board Game Classic", "category": "Toys", "price": 29.99},

    {"_id": "p31", "name": "Organic Honey", "category": "Grocery", "price": 9.99},
    {"_id": "p32", "name": "Green Tea Pack", "category": "Grocery", "price": 6.50},
    {"_id": "p33", "name": "Almonds 500g", "category": "Grocery", "price": 11.00},
    {"_id": "p34", "name": "Olive Oil", "category": "Grocery", "price": 13.50},
    {"_id": "p35", "name": "Dark Chocolate Bar", "category": "Grocery", "price": 4.99},

    {"_id": "p36", "name": "Denim Jacket", "category": "Fashion", "price": 49.99},
    {"_id": "p37", "name": "Leather Wallet", "category": "Fashion", "price": 27.00},
    {"_id": "p38", "name": "Sunglasses", "category": "Fashion", "price": 34.00},
    {"_id": "p39", "name": "Sneakers", "category": "Fashion", "price": 59.99},
    {"_id": "p40", "name": "Winter Scarf", "category": "Fashion", "price": 18.00},
]

# ---------------------------------------------------------------------------
# Users — each has favorite categories + favorite items (explicit taste signal)
# ---------------------------------------------------------------------------
users = [
    {"_id": "u1", "name": "Alice", "age": 25, "favorite_categories": ["Electronics", "Books"], "favorite_items": ["p1", "p2", "p18"]},
    {"_id": "u2", "name": "Bob", "age": 31, "favorite_categories": ["Sportswear"], "favorite_items": ["p6", "p7"]},
    {"_id": "u3", "name": "Charlie", "age": 28, "favorite_categories": ["Home"], "favorite_items": ["p11", "p13"]},
    {"_id": "u4", "name": "Diana", "age": 22, "favorite_categories": ["Books", "Toys"], "favorite_items": ["p17", "p26"]},
    {"_id": "u5", "name": "Ethan", "age": 35, "favorite_categories": ["Electronics"], "favorite_items": ["p3", "p4"]},
    {"_id": "u6", "name": "Fiona", "age": 27, "favorite_categories": ["Beauty"], "favorite_items": ["p21", "p23"]},
    {"_id": "u7", "name": "George", "age": 40, "favorite_categories": ["Grocery"], "favorite_items": ["p31", "p33"]},
    {"_id": "u8", "name": "Hannah", "age": 24, "favorite_categories": ["Fashion"], "favorite_items": ["p36", "p38"]},
    {"_id": "u9", "name": "Ivan", "age": 33, "favorite_categories": ["Sportswear", "Fashion"], "favorite_items": ["p8", "p37"]},
    {"_id": "u10", "name": "Julia", "age": 29, "favorite_categories": ["Home", "Beauty"], "favorite_items": ["p12", "p22"]},
]


def days_ago(n):
    return datetime.now(timezone.utc) - timedelta(days=n)


# ---------------------------------------------------------------------------
# Interactions — browsing/purchase/rating history per user.
# Mostly within the user's favorite categories, plus a few outside items so
# there's signal for both "more of the same" and "occasional exploration".
# ---------------------------------------------------------------------------
interactions = [
    # Alice (Electronics, Books)
    {"user_id": "u1", "product_id": "p1", "action": "purchase", "rating": 5, "timestamp": days_ago(20)},
    {"user_id": "u1", "product_id": "p2", "action": "purchase", "rating": 4, "timestamp": days_ago(18)},
    {"user_id": "u1", "product_id": "p5", "action": "view", "rating": None, "timestamp": days_ago(15)},
    {"user_id": "u1", "product_id": "p18", "action": "purchase", "rating": 5, "timestamp": days_ago(10)},
    {"user_id": "u1", "product_id": "p16", "action": "view", "rating": None, "timestamp": days_ago(8)},
    {"user_id": "u1", "product_id": "p3", "action": "view", "rating": None, "timestamp": days_ago(5)},
    {"user_id": "u1", "product_id": "p31", "action": "purchase", "rating": 3, "timestamp": days_ago(2)},

    # Bob (Sportswear)
    {"user_id": "u2", "product_id": "p6", "action": "purchase", "rating": 5, "timestamp": days_ago(22)},
    {"user_id": "u2", "product_id": "p7", "action": "purchase", "rating": 4, "timestamp": days_ago(19)},
    {"user_id": "u2", "product_id": "p9", "action": "view", "rating": None, "timestamp": days_ago(14)},
    {"user_id": "u2", "product_id": "p10", "action": "purchase", "rating": 4, "timestamp": days_ago(9)},
    {"user_id": "u2", "product_id": "p1", "action": "view", "rating": None, "timestamp": days_ago(6)},
    {"user_id": "u2", "product_id": "p8", "action": "rate", "rating": 3, "timestamp": days_ago(3)},

    # Charlie (Home)
    {"user_id": "u3", "product_id": "p11", "action": "purchase", "rating": 4, "timestamp": days_ago(25)},
    {"user_id": "u3", "product_id": "p13", "action": "purchase", "rating": 5, "timestamp": days_ago(21)},
    {"user_id": "u3", "product_id": "p14", "action": "view", "rating": None, "timestamp": days_ago(16)},
    {"user_id": "u3", "product_id": "p15", "action": "purchase", "rating": 4, "timestamp": days_ago(11)},
    {"user_id": "u3", "product_id": "p17", "action": "view", "rating": None, "timestamp": days_ago(7)},
    {"user_id": "u3", "product_id": "p12", "action": "rate", "rating": 5, "timestamp": days_ago(4)},

    # Diana (Books, Toys)
    {"user_id": "u4", "product_id": "p17", "action": "purchase", "rating": 5, "timestamp": days_ago(23)},
    {"user_id": "u4", "product_id": "p20", "action": "purchase", "rating": 4, "timestamp": days_ago(20)},
    {"user_id": "u4", "product_id": "p26", "action": "purchase", "rating": 5, "timestamp": days_ago(13)},
    {"user_id": "u4", "product_id": "p29", "action": "view", "rating": None, "timestamp": days_ago(10)},
    {"user_id": "u4", "product_id": "p19", "action": "view", "rating": None, "timestamp": days_ago(6)},
    {"user_id": "u4", "product_id": "p28", "action": "rate", "rating": 4, "timestamp": days_ago(2)},

    # Ethan (Electronics)
    {"user_id": "u5", "product_id": "p3", "action": "purchase", "rating": 5, "timestamp": days_ago(24)},
    {"user_id": "u5", "product_id": "p4", "action": "purchase", "rating": 4, "timestamp": days_ago(17)},
    {"user_id": "u5", "product_id": "p2", "action": "view", "rating": None, "timestamp": days_ago(12)},
    {"user_id": "u5", "product_id": "p5", "action": "purchase", "rating": 3, "timestamp": days_ago(8)},
    {"user_id": "u5", "product_id": "p36", "action": "view", "rating": None, "timestamp": days_ago(5)},

    # Fiona (Beauty)
    {"user_id": "u6", "product_id": "p21", "action": "purchase", "rating": 5, "timestamp": days_ago(19)},
    {"user_id": "u6", "product_id": "p23", "action": "purchase", "rating": 4, "timestamp": days_ago(15)},
    {"user_id": "u6", "product_id": "p24", "action": "view", "rating": None, "timestamp": days_ago(11)},
    {"user_id": "u6", "product_id": "p25", "action": "purchase", "rating": 5, "timestamp": days_ago(7)},
    {"user_id": "u6", "product_id": "p38", "action": "view", "rating": None, "timestamp": days_ago(3)},

    # George (Grocery)
    {"user_id": "u7", "product_id": "p31", "action": "purchase", "rating": 5, "timestamp": days_ago(26)},
    {"user_id": "u7", "product_id": "p33", "action": "purchase", "rating": 4, "timestamp": days_ago(20)},
    {"user_id": "u7", "product_id": "p34", "action": "purchase", "rating": 4, "timestamp": days_ago(14)},
    {"user_id": "u7", "product_id": "p35", "action": "view", "rating": None, "timestamp": days_ago(9)},
    {"user_id": "u7", "product_id": "p32", "action": "rate", "rating": 3, "timestamp": days_ago(4)},

    # Hannah (Fashion)
    {"user_id": "u8", "product_id": "p36", "action": "purchase", "rating": 5, "timestamp": days_ago(21)},
    {"user_id": "u8", "product_id": "p38", "action": "purchase", "rating": 4, "timestamp": days_ago(16)},
    {"user_id": "u8", "product_id": "p39", "action": "view", "rating": None, "timestamp": days_ago(12)},
    {"user_id": "u8", "product_id": "p40", "action": "purchase", "rating": 5, "timestamp": days_ago(6)},
    {"user_id": "u8", "product_id": "p22", "action": "view", "rating": None, "timestamp": days_ago(2)},

    # Ivan (Sportswear, Fashion)
    {"user_id": "u9", "product_id": "p8", "action": "purchase", "rating": 4, "timestamp": days_ago(18)},
    {"user_id": "u9", "product_id": "p37", "action": "purchase", "rating": 5, "timestamp": days_ago(14)},
    {"user_id": "u9", "product_id": "p10", "action": "view", "rating": None, "timestamp": days_ago(9)},
    {"user_id": "u9", "product_id": "p39", "action": "purchase", "rating": 4, "timestamp": days_ago(5)},
    {"user_id": "u9", "product_id": "p6", "action": "rate", "rating": 5, "timestamp": days_ago(1)},

    # Julia (Home, Beauty)
    {"user_id": "u10", "product_id": "p12", "action": "purchase", "rating": 5, "timestamp": days_ago(17)},
    {"user_id": "u10", "product_id": "p22", "action": "purchase", "rating": 4, "timestamp": days_ago(13)},
    {"user_id": "u10", "product_id": "p14", "action": "view", "rating": None, "timestamp": days_ago(10)},
    {"user_id": "u10", "product_id": "p25", "action": "purchase", "rating": 5, "timestamp": days_ago(6)},
    {"user_id": "u10", "product_id": "p11", "action": "rate", "rating": 4, "timestamp": days_ago(3)},
]


def seed():
    db.users.delete_many({})
    db.products.delete_many({})
    db.interactions.delete_many({})

    db.users.insert_many(users)
    db.products.insert_many(products)
    db.interactions.insert_many(interactions)

    print(f"Inserted {len(users)} users")
    print(f"Inserted {len(products)} products")
    print(f"Inserted {len(interactions)} interactions")


if __name__ == "__main__":
    seed()
