"""
Script to read and process the custom Three Month Seed Quality dataset.
This script reads the Excel file and prepares it for use in AIRS-GSeed framework.
"""

try:
    import pandas as pd
    import numpy as np
    import os
    
    DATASET_PATH = '../../Custom-Dataset/Three_Month_Seed_Quality_Data.xlsx'
    
    def read_custom_dataset():
        """Read the custom three-month seed quality dataset."""
        print("Reading custom dataset from:", DATASET_PATH)
        
        # Check if file exists
        if not os.path.exists(DATASET_PATH):
            print(f"Error: Dataset file not found at {DATASET_PATH}")
            return None
        
        # Read Excel file
        df = pd.read_excel(DATASET_PATH)
        
        print(f"\nDataset loaded successfully!")
        print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"\nColumns: {df.columns.tolist()}")
        print(f"\nFirst few rows:")
        print(df.head())
        print(f"\nData types:")
        print(df.dtypes)
        print(f"\nSummary statistics:")
        print(df.describe())
        
        return df
    
    def process_for_airs_gseed(df):
        """Process the dataset to extract relevant features for AIRS-GSeed."""
        if df is None:
            return None
        
        print("\n" + "="*60)
        print("Processing data for AIRS-GSeed framework...")
        print("="*60)
        
        # Identify numeric columns for analysis
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        print(f"\nNumeric columns found: {numeric_cols}")
        
        # Identify temporal/date columns if any
        date_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
        if not date_cols:
            # Try to identify date columns by name
            date_cols = [col for col in df.columns if any(x in col.lower() 
                        for x in ['date', 'time', 'day', 'month'])]
        print(f"Date/temporal columns: {date_cols}")
        
        # Identify potential quality metrics
        quality_indicators = [col for col in df.columns if any(x in col.lower() 
                             for x in ['quality', 'health', 'germination', 'moisture', 
                                      'vigor', 'viability', 'aflatoxin', 'fungal'])]
        print(f"Quality indicators: {quality_indicators}")
        
        # Calculate basic statistics
        if numeric_cols:
            print(f"\nBasic statistics for numeric columns:")
            for col in numeric_cols[:5]:  # Show first 5
                print(f"\n{col}:")
                print(f"  Mean: {df[col].mean():.2f}")
                print(f"  Std: {df[col].std():.2f}")
                print(f"  Min: {df[col].min():.2f}")
                print(f"  Max: {df[col].max():.2f}")
        
        return {
            'dataframe': df,
            'numeric_cols': numeric_cols,
            'date_cols': date_cols,
            'quality_indicators': quality_indicators
        }
    
    if __name__ == '__main__':
        df = read_custom_dataset()
        if df is not None:
            processed_data = process_for_airs_gseed(df)
            
            # Save processed summary
            if processed_data:
                print("\n" + "="*60)
                print("Saving processed data summary...")
                df.to_csv('results/custom_dataset_summary.csv', index=False)
                print("Saved: results/custom_dataset_summary.csv")
                print("="*60)

except ImportError as e:
    print(f"Error: Required packages not installed - {e}")
    print("\nPlease install required packages:")
    print("  pip install pandas openpyxl numpy")
    print("\nOr if using a managed Python environment:")
    print("  1. Create virtual environment: python3 -m venv venv")
    print("  2. Activate it: source venv/bin/activate")
    print("  3. Install packages: pip install pandas openpyxl numpy")
