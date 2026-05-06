from load import load_all_data
from clean import clean_all_data
from transform import transform_data
from aggregate import create_aggregations


def main():
    # 1. Load
    root_path = "../data/raw"
    data = load_all_data(root_path)

    orders = data["orders"]
    customers = data["customers"]
    products = data["products"]

    # 2. Clean
    orders, customers, products = clean_all_data(
        orders, customers, products
    )

    # 3. Transform
    merged = transform_data(orders, customers, products)

    # 4. Aggregate
    monthly_revenue, category_revenue, customer_summary = create_aggregations(merged)
    
    output_path = "../data/processed"
    
    monthly_revenue.to_csv(f"{output_path}/monthly_revenue.csv", index=False, sep=";", decimal=",")
    category_revenue.to_csv(f"{output_path}/category_revenue.csv", index=False, sep=";", decimal=",")
    customer_summary.to_csv(f"{output_path}/customer_summary.csv", index=False, sep=";", decimal=",")
    
    # Final table to use in Power BI Dashboard
    merged.to_csv(f"{output_path}/merged_data.csv", index=False, sep=";", decimal=",")

if __name__ == "__main__":
    main()