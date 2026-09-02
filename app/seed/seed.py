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

    # Electronics (extra)
    {"_id": "p41", "name": "USB-C Hub", "category": "Electronics", "price": 91.68},
    {"_id": "p42", "name": "Portable SSD 1TB", "category": "Electronics", "price": 9.35},
    {"_id": "p43", "name": "Webcam HD", "category": "Electronics", "price": 42.85},
    {"_id": "p44", "name": "Gaming Monitor 27in", "category": "Electronics", "price": 35.91},
    {"_id": "p45", "name": "Wireless Charger", "category": "Electronics", "price": 104.69},
    {"_id": "p46", "name": "Bluetooth Speaker", "category": "Electronics", "price": 96.68},
    {"_id": "p47", "name": "Noise Cancelling Earbuds", "category": "Electronics", "price": 125.55},
    {"_id": "p48", "name": "Smart Light Bulb", "category": "Electronics", "price": 17.65},
    {"_id": "p49", "name": "Action Camera", "category": "Electronics", "price": 62.54},
    {"_id": "p50", "name": "Drone Mini", "category": "Electronics", "price": 9.99},
    {"_id": "p51", "name": "Power Bank 20000mAh", "category": "Electronics", "price": 35.30},
    {"_id": "p52", "name": "Graphics Tablet", "category": "Electronics", "price": 73.72},
    {"_id": "p53", "name": "WiFi 6 Router", "category": "Electronics", "price": 9.56},
    {"_id": "p54", "name": "Smart Plug", "category": "Electronics", "price": 32.64},
    {"_id": "p55", "name": "Fitness Tracker Band", "category": "Electronics", "price": 93.08},
    {"_id": "p56", "name": "HDMI Cable 2m", "category": "Electronics", "price": 79.02},
    {"_id": "p57", "name": "Laptop Backpack", "category": "Electronics", "price": 35.54},
    {"_id": "p58", "name": "External Hard Drive 2TB", "category": "Electronics", "price": 84.96},
    {"_id": "p59", "name": "Wireless Charging Pad", "category": "Electronics", "price": 114.46},
    {"_id": "p60", "name": "Mini Projector", "category": "Electronics", "price": 6.87},

    # Sportswear (extra)
    {"_id": "p61", "name": "Compression Leggings", "category": "Sportswear", "price": 113.98},
    {"_id": "p62", "name": "Resistance Bands Set", "category": "Sportswear", "price": 99.55},
    {"_id": "p63", "name": "Jump Rope", "category": "Sportswear", "price": 51.59},
    {"_id": "p64", "name": "Gym Duffel Bag", "category": "Sportswear", "price": 26.83},
    {"_id": "p65", "name": "Sports Bra", "category": "Sportswear", "price": 134.27},
    {"_id": "p66", "name": "Cycling Shorts", "category": "Sportswear", "price": 51.10},
    {"_id": "p67", "name": "Swim Goggles", "category": "Sportswear", "price": 18.43},
    {"_id": "p68", "name": "Foam Roller", "category": "Sportswear", "price": 18.96},
    {"_id": "p69", "name": "Ankle Weights Set", "category": "Sportswear", "price": 119.56},
    {"_id": "p70", "name": "Sweat Towel", "category": "Sportswear", "price": 86.90},
    {"_id": "p71", "name": "Basketball", "category": "Sportswear", "price": 114.16},
    {"_id": "p72", "name": "Soccer Ball", "category": "Sportswear", "price": 103.78},
    {"_id": "p73", "name": "Tennis Racket", "category": "Sportswear", "price": 77.85},
    {"_id": "p74", "name": "Yoga Blocks Set", "category": "Sportswear", "price": 136.40},
    {"_id": "p75", "name": "Dumbbell Set 10kg", "category": "Sportswear", "price": 56.72},
    {"_id": "p76", "name": "Fitness Gloves", "category": "Sportswear", "price": 79.97},
    {"_id": "p77", "name": "Running Shorts", "category": "Sportswear", "price": 117.14},
    {"_id": "p78", "name": "Sports Cap", "category": "Sportswear", "price": 88.88},
    {"_id": "p79", "name": "Knee Support Brace", "category": "Sportswear", "price": 121.47},
    {"_id": "p80", "name": "Hiking Backpack", "category": "Sportswear", "price": 83.37},

    # Home (extra)
    {"_id": "p81", "name": "Vacuum Cleaner", "category": "Home", "price": 100.41},
    {"_id": "p82", "name": "Electric Kettle", "category": "Home", "price": 12.14},
    {"_id": "p83", "name": "Toaster", "category": "Home", "price": 36.54},
    {"_id": "p84", "name": "Bed Sheets Set", "category": "Home", "price": 44.78},
    {"_id": "p85", "name": "Throw Pillow", "category": "Home", "price": 16.69},
    {"_id": "p86", "name": "Wall Clock", "category": "Home", "price": 37.19},
    {"_id": "p87", "name": "Storage Baskets Set", "category": "Home", "price": 19.53},
    {"_id": "p88", "name": "Curtains Set", "category": "Home", "price": 43.25},
    {"_id": "p89", "name": "Cutting Board", "category": "Home", "price": 91.18},
    {"_id": "p90", "name": "Knife Set", "category": "Home", "price": 54.89},
    {"_id": "p91", "name": "Dish Rack", "category": "Home", "price": 55.60},
    {"_id": "p92", "name": "Laundry Basket", "category": "Home", "price": 34.07},
    {"_id": "p93", "name": "Scented Candle Set", "category": "Home", "price": 41.78},
    {"_id": "p94", "name": "Area Rug", "category": "Home", "price": 131.51},
    {"_id": "p95", "name": "Mattress Topper", "category": "Home", "price": 92.84},
    {"_id": "p96", "name": "Shower Curtain", "category": "Home", "price": 87.62},
    {"_id": "p97", "name": "Trash Can", "category": "Home", "price": 28.93},
    {"_id": "p98", "name": "Food Storage Containers", "category": "Home", "price": 103.70},
    {"_id": "p99", "name": "Ironing Board", "category": "Home", "price": 27.90},
    {"_id": "p100", "name": "Ceiling Fan", "category": "Home", "price": 56.85},

    # Books (extra)
    {"_id": "p101", "name": "Mystery Thriller Boxset", "category": "Books", "price": 138.60},
    {"_id": "p102", "name": "History of Rome", "category": "Books", "price": 91.76},
    {"_id": "p103", "name": "Poetry Collection", "category": "Books", "price": 80.63},
    {"_id": "p104", "name": "Self-Help Guide", "category": "Books", "price": 97.74},
    {"_id": "p105", "name": "Business Strategy Book", "category": "Books", "price": 118.94},
    {"_id": "p106", "name": "Programming 101", "category": "Books", "price": 109.98},
    {"_id": "p107", "name": "World Atlas", "category": "Books", "price": 36.69},
    {"_id": "p108", "name": "Biography Collection", "category": "Books", "price": 10.30},
    {"_id": "p109", "name": "Fantasy Trilogy Set", "category": "Books", "price": 48.27},
    {"_id": "p110", "name": "Graphic Novel Vol 1", "category": "Books", "price": 41.88},
    {"_id": "p111", "name": "Beginner's Cookbook", "category": "Books", "price": 34.27},
    {"_id": "p112", "name": "Travel Guide Europe", "category": "Books", "price": 132.35},
    {"_id": "p113", "name": "Philosophy Essentials", "category": "Books", "price": 123.43},
    {"_id": "p114", "name": "Classic Literature Set", "category": "Books", "price": 48.17},
    {"_id": "p115", "name": "Language Learning Book", "category": "Books", "price": 93.83},
    {"_id": "p116", "name": "Parenting Guide", "category": "Books", "price": 59.01},
    {"_id": "p117", "name": "Personal Finance Guide", "category": "Books", "price": 128.55},
    {"_id": "p118", "name": "Short Stories Anthology", "category": "Books", "price": 67.49},
    {"_id": "p119", "name": "True Crime Stories", "category": "Books", "price": 41.49},
    {"_id": "p120", "name": "Science Encyclopedia", "category": "Books", "price": 39.05},

    # Beauty (extra)
    {"_id": "p121", "name": "Facial Cleanser", "category": "Beauty", "price": 81.22},
    {"_id": "p122", "name": "Eye Cream", "category": "Beauty", "price": 41.21},
    {"_id": "p123", "name": "Hair Straightener", "category": "Beauty", "price": 84.33},
    {"_id": "p124", "name": "Nail Polish Set", "category": "Beauty", "price": 126.31},
    {"_id": "p125", "name": "Makeup Brush Set", "category": "Beauty", "price": 59.52},
    {"_id": "p126", "name": "Perfume 50ml", "category": "Beauty", "price": 35.39},
    {"_id": "p127", "name": "Body Lotion", "category": "Beauty", "price": 139.67},
    {"_id": "p128", "name": "Shampoo & Conditioner Set", "category": "Beauty", "price": 74.28},
    {"_id": "p129", "name": "Face Mask Pack", "category": "Beauty", "price": 18.18},
    {"_id": "p130", "name": "Hair Oil", "category": "Beauty", "price": 12.31},
    {"_id": "p131", "name": "Blush Palette", "category": "Beauty", "price": 20.69},
    {"_id": "p132", "name": "Foundation Bottle", "category": "Beauty", "price": 90.08},
    {"_id": "p133", "name": "Lip Balm Set", "category": "Beauty", "price": 112.14},
    {"_id": "p134", "name": "Hair Curling Iron", "category": "Beauty", "price": 62.57},
    {"_id": "p135", "name": "Exfoliating Scrub", "category": "Beauty", "price": 14.51},
    {"_id": "p136", "name": "Beard Care Kit", "category": "Beauty", "price": 57.14},
    {"_id": "p137", "name": "Makeup Remover", "category": "Beauty", "price": 139.48},
    {"_id": "p138", "name": "Anti-Aging Cream", "category": "Beauty", "price": 76.90},
    {"_id": "p139", "name": "Hand Cream Set", "category": "Beauty", "price": 136.12},
    {"_id": "p140", "name": "Cosmetic Organizer", "category": "Beauty", "price": 121.34},

    # Toys (extra)
    {"_id": "p141", "name": "Action Figure Set", "category": "Toys", "price": 7.54},
    {"_id": "p142", "name": "Doll House", "category": "Toys", "price": 102.58},
    {"_id": "p143", "name": "Toy Train Set", "category": "Toys", "price": 97.35},
    {"_id": "p144", "name": "Kids Educational Tablet", "category": "Toys", "price": 77.95},
    {"_id": "p145", "name": "Mega Building Bricks Set", "category": "Toys", "price": 41.75},
    {"_id": "p146", "name": "Kids Art Set", "category": "Toys", "price": 91.89},
    {"_id": "p147", "name": "Card Game Deck", "category": "Toys", "price": 20.95},
    {"_id": "p148", "name": "Water Gun", "category": "Toys", "price": 64.26},
    {"_id": "p149", "name": "Kite", "category": "Toys", "price": 66.80},
    {"_id": "p150", "name": "Slime Kit", "category": "Toys", "price": 133.81},
    {"_id": "p151", "name": "Robot Toy", "category": "Toys", "price": 123.36},
    {"_id": "p152", "name": "Toy Kitchen Set", "category": "Toys", "price": 41.29},
    {"_id": "p153", "name": "Ride-on Car", "category": "Toys", "price": 73.08},
    {"_id": "p154", "name": "Musical Toy Piano", "category": "Toys", "price": 29.94},
    {"_id": "p155", "name": "Magic Trick Set", "category": "Toys", "price": 128.29},
    {"_id": "p156", "name": "Kids Puzzle Cube", "category": "Toys", "price": 122.65},
    {"_id": "p157", "name": "Stuffed Animal Set", "category": "Toys", "price": 45.99},
    {"_id": "p158", "name": "Toy Dinosaur Set", "category": "Toys", "price": 91.62},
    {"_id": "p159", "name": "Building Crane Set", "category": "Toys", "price": 87.60},
    {"_id": "p160", "name": "Outdoor Play Tent", "category": "Toys", "price": 26.48},

    # Grocery (extra)
    {"_id": "p161", "name": "Pasta Pack", "category": "Grocery", "price": 108.18},
    {"_id": "p162", "name": "Basmati Rice 5kg", "category": "Grocery", "price": 78.28},
    {"_id": "p163", "name": "Peanut Butter", "category": "Grocery", "price": 110.34},
    {"_id": "p164", "name": "Coffee Beans 1kg", "category": "Grocery", "price": 77.07},
    {"_id": "p165", "name": "Oatmeal Pack", "category": "Grocery", "price": 6.08},
    {"_id": "p166", "name": "Mixed Nuts", "category": "Grocery", "price": 49.44},
    {"_id": "p167", "name": "Cereal Box", "category": "Grocery", "price": 8.61},
    {"_id": "p168", "name": "Maple Syrup", "category": "Grocery", "price": 130.50},
    {"_id": "p169", "name": "Coconut Oil", "category": "Grocery", "price": 123.75},
    {"_id": "p170", "name": "Protein Powder", "category": "Grocery", "price": 117.44},
    {"_id": "p171", "name": "Herbal Tea Pack", "category": "Grocery", "price": 47.21},
    {"_id": "p172", "name": "Granola Bars", "category": "Grocery", "price": 13.76},
    {"_id": "p173", "name": "Dried Fruits Mix", "category": "Grocery", "price": 123.65},
    {"_id": "p174", "name": "Quinoa 1kg", "category": "Grocery", "price": 132.89},
    {"_id": "p175", "name": "Tomato Sauce", "category": "Grocery", "price": 17.48},
    {"_id": "p176", "name": "Spice Set", "category": "Grocery", "price": 71.12},
    {"_id": "p177", "name": "Sparkling Water Pack", "category": "Grocery", "price": 15.27},
    {"_id": "p178", "name": "Cooking Vinegar", "category": "Grocery", "price": 107.92},
    {"_id": "p179", "name": "Whole Wheat Flour", "category": "Grocery", "price": 108.62},
    {"_id": "p180", "name": "Trail Mix Pack", "category": "Grocery", "price": 23.20},

    # Fashion (extra)
    {"_id": "p181", "name": "Formal Shirt", "category": "Fashion", "price": 69.69},
    {"_id": "p182", "name": "Casual T-Shirt", "category": "Fashion", "price": 79.67},
    {"_id": "p183", "name": "Chino Pants", "category": "Fashion", "price": 41.52},
    {"_id": "p184", "name": "Leather Belt", "category": "Fashion", "price": 122.91},
    {"_id": "p185", "name": "Wool Sweater", "category": "Fashion", "price": 62.70},
    {"_id": "p186", "name": "Baseball Cap", "category": "Fashion", "price": 34.38},
    {"_id": "p187", "name": "Ankle Boots", "category": "Fashion", "price": 78.27},
    {"_id": "p188", "name": "Rain Jacket", "category": "Fashion", "price": 103.81},
    {"_id": "p189", "name": "Silk Tie", "category": "Fashion", "price": 32.95},
    {"_id": "p190", "name": "Cotton Socks Pack", "category": "Fashion", "price": 47.77},
    {"_id": "p191", "name": "Handbag", "category": "Fashion", "price": 139.35},
    {"_id": "p192", "name": "Backpack Purse", "category": "Fashion", "price": 93.08},
    {"_id": "p193", "name": "Formal Blazer", "category": "Fashion", "price": 64.71},
    {"_id": "p194", "name": "Summer Dress", "category": "Fashion", "price": 75.36},
    {"_id": "p195", "name": "Denim Jeans", "category": "Fashion", "price": 22.21},
    {"_id": "p196", "name": "Polo Shirt", "category": "Fashion", "price": 36.11},
    {"_id": "p197", "name": "Woolen Gloves", "category": "Fashion", "price": 51.30},
    {"_id": "p198", "name": "Beanie Hat", "category": "Fashion", "price": 84.83},
    {"_id": "p199", "name": "Canvas Sneakers", "category": "Fashion", "price": 36.84},
    {"_id": "p200", "name": "Crossbody Bag", "category": "Fashion", "price": 35.51},
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
