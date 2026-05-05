def transform_data(orders, customers, products):
    merged = orders.merge( customers, on="customer_id", how="inner" )
    
    merged = merged.merge( products, on="product_id", how="inner" )
    
    merged = merged.copy()
    
    merged["revenue"] = merged["quantity"] * merged["unit_price"]
    
    merged["year"] = merged["order_date"].dt.year
    
    merged["month"] = merged["order_date"].dt.month
    
    merged["year_month"] = merged["order_date"].dt.to_period("M").astype(str)
    
    cols_to_keep = ["order_id", "customer_id", "product_id", "order_date", "country", "signup_date", "category", "product_name", "quantity", "unit_price", "revenue", "year_month"]
    
    merged = merged[cols_to_keep]
    
    merged = merged.sort_values("order_date")
    
    return merged