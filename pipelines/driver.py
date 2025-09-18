#!/usr/bin/env python3
"""
ETL Pipeline Driver Script
Orchestrates the complete retail sales data warehouse ETL process
"""

import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

def run_command(command, description):
    """Execute a command with error handling"""
    print(f"\n{'='*50}")
    print(f"⏳ {description}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True, cwd=project_root)
        print(f"{description} completed successfully")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{description} failed")
        print(f"Error: {e.stderr}")
        return False

def run_etl_pipeline():
    """Execute the complete ETL pipeline"""
    start_time = datetime.now()
    print(f"Starting ETL Pipeline at {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Pipeline steps
    steps = [
        ("python etl/extract.py", "Data Extraction"),
        ("python etl/transform.py", "Data Transformation"),  
        ("python etl/load.py", "Data Loading to Staging"),
    ]
    
    success_count = 0
    for command, description in steps:
        if run_command(command, description):
            success_count += 1
        else:
            print(f"\nPipeline failed at step: {description}")
            break
    
    end_time = datetime.now()
    duration = end_time - start_time
    
    print(f"\n{'='*60}")
    if success_count == len(steps):
        print(f"🎉 ETL Pipeline completed successfully!")
        print(f"{success_count}/{len(steps)} steps completed")
        print(f"  Total duration: {duration}")
        print(f"\n Next step: Execute SQL transformations in PostgreSQL:")
        print(f"   \\i {project_root}/sql/transformations.sql")
    else:
        print(f"❌ ETL Pipeline failed")
        print(f" {success_count}/{len(steps)} steps completed")
    print(f"{'='*60}")

if __name__ == "__main__":
    run_etl_pipeline()
