import pandas as pd

def clean_orders(orders):
    if orders is None or orders.empty:
        raise ValueError("Table is empty or non-existent")
    
    orders = orders.copy()
    
    initial_rows = orders.shape[0]
    
    required_columns = ["order_id", "customer_id", "product_id", "order_date", "quantity", "unit_price", "status"]
    existing_columns = set(orders.columns)
    not_present = []
    
    for col in required_columns:    
        if col not in existing_columns:
            not_present.append(col)
    
    if len(not_present) >= 1:
        raise KeyError(f"Missing following columns from table: {not_present}")
    
    orders["order_date"] = pd.to_datetime(orders["order_date"], errors="coerce")
    orders = orders.dropna(subset=["order_date"])
    
    orders["quantity"] = pd.to_numeric(orders["quantity"], errors="coerce")
    orders = orders[orders["quantity"] > 0]
    
    orders["unit_price"] = pd.to_numeric(orders["unit_price"], errors="coerce")
    orders = orders[orders["unit_price"] > 0]
    
    orders["status"] = orders["status"].str.lower().str.strip()
    valid_statuses = ["completed", "cancelled", "returned"]
    orders = orders[orders["status"].isin(valid_statuses)]
    
    orders = orders.dropna(subset=["order_id", "customer_id", "product_id"])

    orders["order_id"] = orders["order_id"].astype(str).str.strip()
    orders["customer_id"] = orders["customer_id"].astype(str).str.strip()
    orders["product_id"] = orders["product_id"].astype(str).str.strip()
   
    orders = orders.drop_duplicates(subset=["order_id"])
    
    orders = orders.drop(columns="unit_price")
    
    final_rows = orders.shape[0]
    
    print(f"Removed {initial_rows - final_rows} rows from orders")
    
    return orders

def clean_customers(customers):
    if customers is None or customers.empty:
        raise ValueError("Table is empty or non-existent")
    
    customers = customers.copy()
    
    required_columns = ["customer_id", "country", "signup_date"]
    existing_columns = set(customers.columns)
    not_present = []
    
    for col in required_columns:    
        if col not in existing_columns:
            not_present.append(col)
    
    if len(not_present) >= 1:
        raise KeyError(f"Missing following columns from table: {not_present}")
    
    customers = customers.dropna(subset=["customer_id"])
    
    customers["customer_id"] = customers["customer_id"].astype(str).str.strip()
    
    customers = customers.drop_duplicates(subset=["customer_id"])
    
    customers["signup_date"] = pd.to_datetime(customers["signup_date"], errors="coerce")
    
    customers["country"] = customers["country"].str.strip().str.lower()
    
    return customers

def clean_products(products):
    if products is None or products.empty:
        raise ValueError("Table is empty or non-existent")
    
    products = products.copy()
    
    required_columns = ["product_id", "category", "product_name"]
    existing_columns = set(products.columns)
    not_present = []
    
    for col in required_columns:    
        if col not in existing_columns:
            not_present.append(col)
    
    if len(not_present) >= 1:
        raise KeyError(f"Missing following columns from table: {not_present}")
        
    products = products.dropna(subset=["product_id"])
    
    products["product_id"] = products["product_id"].astype(str).str.strip()
    
    products = products.drop_duplicates(subset=["product_id"])
    
    products["category"] = products["category"].str.strip().str.lower()
    
    products["product_name"] = products["product_name"].str.strip().str.lower()
    
    return products

def validate_order_relationships(orders, customers, products):  
    initial_rows = orders.shape[0]
    
    valid_customer_ids = set(customers["customer_id"].to_list())
    valid_product_ids = set(products["product_id"].to_list())
    
    orders = orders[orders["customer_id"].isin(valid_customer_ids)]
    
    orders = orders[orders["product_id"].isin(valid_product_ids)]
    
    final_rows = orders.shape[0]
    
    print(f"Removed {initial_rows - final_rows} orders due to invalid customer/product references")
    
    return orders

def clean_all_data(orders, customers, products):
    orders = clean_orders(orders)
    customers = clean_customers(customers)
    products = clean_products(products)

    orders = validate_order_relationships(orders, customers, products)

    return orders, customers, products