import pandas as pd

def create_aggregations(merged):
    merged = merged.copy()
    
    monthly_revenue = merged.groupby("year_month", as_index=False).agg(
        total_orders=("order_id", "count"),
        total_revenue=("revenue", "sum"),
        avg_order_value=("revenue", "mean")
    )

    category_revenue = merged.groupby("category", as_index=False).agg(
        total_revenue=("revenue", "sum"),
        total_quantity=("quantity", "sum")
    )

    customer_summary = merged.groupby("customer_id", as_index=False).agg(
        total_orders=("order_id", "count"),
        total_revenue=("revenue", "sum"),
        avg_order_value=("revenue", "mean")
    )
    
    monthly_revenue = monthly_revenue.reset_index(drop=True)
    category_revenue = category_revenue.reset_index(drop=True)
    customer_summary = customer_summary.reset_index(drop=True)
    
    monthly_revenue["total_revenue"] = monthly_revenue["total_revenue"].round(2)
    category_revenue["total_revenue"] = category_revenue["total_revenue"].round(2)
    customer_summary["total_revenue"] = customer_summary["total_revenue"].round(2)
    
    monthly_revenue = monthly_revenue.sort_values("year_month")
    category_revenue = category_revenue.sort_values("total_revenue", ascending=False)
    customer_summary = customer_summary.sort_values("total_revenue", ascending=False)
    
    monthly_revenue["avg_order_value"] = monthly_revenue["avg_order_value"].round(2)
    customer_summary["avg_order_value"] = customer_summary["avg_order_value"].round(2)

    return monthly_revenue, category_revenue, customer_summary