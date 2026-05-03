import pandas as pd
import os

def load_csv(root, file_name):
    """
    Loads a CSV file from the given root directory.

    Args:
        root (str): Base directory path
        file_name (str): Name of the file (without extension)

    Returns:
        pd.DataFrame
    """
    path = os.path.join(root, f"{file_name}.csv")
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"{path} not found")

def load_all_data(root):
    orders = load_csv(root, "orders")
    customers = load_csv(root, "customers")
    products = load_csv(root, "products")
    return {
        "orders": orders,
        "customers": customers,
        "products": products
    }