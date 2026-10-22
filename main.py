
import pandas as pd

categories = pd.DataFrame({
    "category_id": [1, 2, 3],
    "category_name": [
        "Electronics", "Clothing", "Home & Kitchen"
    ]
})

products = pd.DataFrame({
    "product_id": [1, 2, 3, 4, 5, 6, 7],
    "product_name": [
        "Laptop Dell XPS", "iPhone 15",
        "Wireless Mouse", "T-Shirt Cotton",
        "Jeans Slim Fit", "Coffee Maker", "Air Fryer"
    ],
    "price": [1500, 1000, 25, 20, 50, 80, 120],
    "category_id": [1, 1, 1, 2, 2, 3, 3]
})


customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5],
    "customer_name": [
        "Nguyen Van A", "Tran Thi B",
        "Le Van C", "Pham Thi D", "Hoang Van E"
    ],
    "city": ["Ha Noi", "HCM", "Da Nang", "Ha Noi", "HCM"]
})

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7],
    "customer_id": [1, 2, 3, 1, 4, 5, 2],
    "order_date": pd.to_datetime([
        "2026-09-01", "2026-09-02", "2026-09-03",
        "2026-09-05", "2026-09-10", "2026-09-12",
        "2026-09-15"
    ]),
    "status": [
        "Completed", "Completed", "Cancelled",
        "Completed", "Completed", "Pending", "Completed"
    ]
})


order_details = pd.DataFrame({
    "order_id": [1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7],
    "product_id": [1, 3, 2, 4, 5, 3, 6, 7, 1, 2, 5],
    "quantity": [1, 2, 1, 3, 2, 5, 1, 2, 1, 2, 1],
    "unit_price": [
        1500, 25, 1000, 20, 50, 25,
        80, 120, 1500, 1000, 50
    ]
})

print("DANH SÁCH SẢN PHẨM:")
print(products.to_string(index=False))
