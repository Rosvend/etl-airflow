import pandas as pd
from extract import df

def clean_dataframe(df):
    """
    Cleans the input DataFrame by removing duplicates and handling missing values.

    Parameters:
    df (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
    pd.DataFrame: The cleaned DataFrame.
    """
    
    df = df.rename(columns={
        'Transaction ID': 'transaction_id',
        'Date': 'date',
        'Customer ID': 'customer_id',
        'Gender': 'gender',
        'Age': 'age',
        'Product Category': 'product_category',
        'Quantity': 'quantity',
        'Price per Unit': 'price_per_unit',
        'Total Amount': 'total_amount'
    })

    df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')
    df['transaction_id'] = pd.to_numeric(df['transaction_id'], errors='coerce')
    df['age'] = df['age'].astype('int')
    df['quantity'] = df['quantity'].astype('int')
    df['price_per_unit'] = df['price_per_unit'].astype('int')
    df['total_amount'] = df['total_amount'].astype('int')
    df['gender'] = df['gender'].astype('object')
    df['product_category'] = df['product_category'].astype('object')
    df['customer_id'] = df['customer_id'].astype('object')

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    return df

cleaned_df = clean_dataframe(df)
print(cleaned_df.info())