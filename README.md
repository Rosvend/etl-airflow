# ETL Pipeline Data Warehouse Project

A comprehensive data engineering project implementing an end-to-end ETL pipeline for business intelligence and analytics.

## Project Overview

This project demonstrates the complete lifecycle of a data warehouse solution, from source system analysis to business intelligence queries. The implementation follows industry best practices for data warehousing and ETL processes.

## 🎯 Project Objectives

### 1. Source System Analysis
- **Dataset Identification**: Comprehensive analysis of the source dataset
- **Entity Mapping**: Documentation of columns, entities, and their relationships
- **Business Value**: Justification of data utility for analytical purposes

### 2. Data Warehouse Design
- **Schema Architecture**: Implementation of star or snowflake schema design
- **Fact Table**: Central table containing measurable business metrics
- **Dimension Tables**: Supporting tables providing context and attributes
- **Relationship Mapping**: Clear documentation of table relationships and foreign keys

### 3. ETL Process Implementation

#### Extract
- Data retrieval from source systems
- Connection management and data validation

#### Transform
- **Data Cleaning**: Handling missing values, duplicates, and inconsistencies
- **Data Enrichment**: Deriving new calculated columns
- **Data Type Conversion**: Ensuring proper data types for analysis
- **Data Integration**: Joining multiple data sources
- **Deduplication**: Removing duplicate records

#### Load
- **Dimension Loading**: Insert new records with optional update capabilities
- **Fact Table Loading**: Insert-only approach for historical data preservation
- **Data Validation**: Ensuring data integrity and consistency

### 4. Business Intelligence & Analytics

The data warehouse enables answering critical business questions through optimized queries:

- 📈 **Sales Performance**: "What are the top 5 products by sales volume?"
- 👥 **Customer Analysis**: "Which customers have the highest purchase volume this year?"
- 📅 **Trend Analysis**: "How have sales trends evolved month-over-month?"

## Project Deliverables

### Part 1: Documentation 📚
- [ ] **Dataset Description**: Comprehensive source system documentation
- [ ] **Schema Design Diagram**: Visual representation of data warehouse architecture
- [ ] **ETL Process Documentation**: Detailed workflow descriptions

### Part 2: Implementation 🔧
- [ ] **ETL Pipeline Screenshots**: Visual evidence of SSIS packages or alternative tools
- [ ] **Database Population Evidence**: Screenshots of populated fact and dimension tables
- [ ] **Data Quality Validation**: Evidence of successful data loading

### Part 3: Business Intelligence Evidence 📊
- [ ] **Query Demonstrations**: Screenshots of business question queries and results
- [ ] **Performance Metrics**: Query execution times and optimization evidence
- [ ] **Business Insights**: Analysis and interpretation of query results

## 📁 Project Structure

```
Parcial 3/
├── README.md
├── scripts/
│   └── dogs.py
├── documentation/
├── schemas/
├── screenshots/
└── queries/
```

---