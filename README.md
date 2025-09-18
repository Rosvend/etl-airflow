# Retail Sales Data Warehouse ETL Pipeline

This project demonstrates a complete data warehouse solution built around retail sales data, implementing a star schema design with automated ETL processes. The solution transforms raw transactional data into a structured analytical environment optimized for business intelligence queries.

## Dataset Description

**Source**: Retail Sales Dataset (`retail_sales_dataset.csv`)
- **Records**: 1,000+ transaction records
- **Timeframe**: 2023 retail transactions
- **Format**: CSV with semicolon delimiter

**Data Structure**:
- `Transaction ID`: Unique transaction identifier
- `Date`: Transaction date (DD/MM/YYYY format)
- `Customer ID`: Customer identifier (CUST001-CUSTXXX)
- `Gender`: Customer gender (Male/Female)
- `Age`: Customer age
- `Product Category`: Product classification (Beauty, Clothing, Electronics)
- `Quantity`: Items purchased
- `Price per Unit`: Unit price
- `Total Amount`: Transaction total

## Data Warehouse Architecture

### Star Schema Design
The implementation follows a **star schema** pattern optimized for analytical queries:

**Fact Table**:
- `fact_sales`: Central table containing sales metrics and foreign keys

**Dimension Tables**:
- `dim_customers`: Customer demographics and attributes
- `dim_products`: Product category information
- `dim_date`: Date hierarchy for temporal analysis

**Staging Table**:
- `staging_retail_sales`: Temporary storage for data transformation

## ETL Pipeline Implementation

### Extract (`etl/extract.py`)
- Reads CSV data using pandas with proper delimiter handling
- Implements error handling for file operations
- Returns structured DataFrame for downstream processing

### Transform (`etl/transform.py`)
- **Column Standardization**: Renames columns to snake_case convention
- **Data Type Conversion**: Ensures proper data types for all fields
- **Date Parsing**: Converts date strings to datetime objects
- **Data Cleaning**: Removes duplicates and handles missing values
- **Data Validation**: Maintains data integrity throughout transformation

### Load (`etl/load.py`)
- Uses SQLAlchemy for database connectivity
- Implements staging table approach for data loading
- Provides error handling and transaction management
- Supports PostgreSQL database backend

## 🛠️ Technology Stack

- **Python 3.13+**: Core programming language
- **pandas**: Data manipulation and analysis
- **SQLAlchemy**: Database ORM and connection management
- **psycopg2**: PostgreSQL database adapter
- **PostgreSQL**: Data warehouse database
- **UV**: Modern Python package management

## 📁 Project Structure

```
Parcial 3 - Bodegas/
├── README.md                     # Project documentation
├── pyproject.toml               # Python project configuration
├── uv.lock                      # Dependency lock file
│
├── data/
│   ├── raw/
│   │   └── retail_sales_dataset.csv    # Source dataset
│   └── processed/                       # Transformed data outputs
│
├── docs/
│   └── Star schema diagram.png         # Data warehouse schema diagram
│
├── etl/
│   ├── extract.py                      # Data extraction module
│   ├── transform.py                    # Data transformation module
│   └── load.py                         # Data loading module
│
├── pipelines/
│   ├── driver.py                       # Simple ETL orchestration script
│   └── airflow_dag.py                  # Apache Airflow DAG definition
│
└── sql/
    ├── create_tables.sql               # Database schema definitions
    ├── transformations.sql             # Data transformation queries
    └── queries.sql                     # Business intelligence queries
```

## 🚀 Getting Started

### Prerequisites
- Python 3.13+
- PostgreSQL database
- UV package manager

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```

### Database Setup
1. Create PostgreSQL database: `parcial3_bodegas`
2. Run table creation script:
   ```sql
   \i sql/create_tables.sql
   ```

### Running the ETL Pipeline

#### Option 1: Manual Execution
1. **Extract**: Run `python etl/extract.py`
2. **Transform**: Run `python etl/transform.py`
3. **Load**: Run `python etl/load.py`
4. **Transform Data**: Execute `sql/transformations.sql` in PostgreSQL

#### Option 2: Orchestrated Pipeline (Recommended)
Run the complete pipeline with the driver script:
```bash
python pipelines/driver.py
```

#### Option 3: Apache Airflow (Production)
For production-ready scheduling and monitoring:

1. **Install Airflow dependencies**:
   ```bash
   uv sync --extra airflow
   ```

2. **Setup Airflow**:
   ```bash
   bash setup_airflow.sh
   ```

3. **Start Airflow services**:
   ```bash
   # Terminal 1 - Scheduler
   export AIRFLOW_HOME=$(pwd)/airflow
   airflow scheduler
   
   # Terminal 2 - Webserver  
   airflow webserver --port 8080
   ```

4. **Access Airflow UI**: http://localhost:8080 (admin/admin)