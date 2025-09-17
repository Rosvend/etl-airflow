from sqlalchemy import create_engine
from transform import cleaned_df

def load_data_staging(cleaned_df, table_name: str, conn_url: str):
    """
    Load data from a pandas DataFrame into a staging table in a SQL database.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data to be loaded.
    table_name (str): The name of the staging table in the database.
    conn_url (str): The database connection URL.

    Returns:
    None
    """
    try:
        engine = create_engine(conn_url)

        with engine.connect() as connection:
            cleaned_df.to_sql(table_name, con=connection, if_exists='append', index=False)
        print(f"Data loaded successfully into {table_name} table.")

    except Exception as e:
        print(f"An error occurred while loading data: {e}")

load_data_staging(cleaned_df, 'staging_retail_sales', 'postgresql+psycopg2://parcial3_user:UnaClav3@localhost:5432/parcial3_bodegas')