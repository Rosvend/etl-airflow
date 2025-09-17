import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file and return it as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The extracted data as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path,sep=';')
        return data
    except Exception as e:
            print(f"An error occurred while extracting data: {e}")
            return pd.DataFrame()

df = extract_data('data/raw/retail_sales_dataset.csv')
print(df.sample(5))