import pandas as pd

def clean_excel(input_file, output_file):
    """
    Cleans a messy Excel/CSV file by:
    - Removing completely empty rows
    - Removing duplicate rows
    - Stripping extra whitespace from text columns
    - Filling missing numeric values with 0
    - Generating a summary report grouped by first column
    """
    # Read the file (works for both .csv and .xlsx)
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
    else:
        df = pd.read_excel(input_file)

    print(f"Original data: {len(df)} rows, {len(df.columns)} columns")

    # Step 1: Remove completely empty rows
    df = df.dropna(how='all')

    # Step 2: Remove duplicate rows
    df = df.drop_duplicates()

    # Step 3: Strip whitespace from string columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    # Step 4: Fill missing numeric values with 0
    df = df.fillna({'amount': 0, 'quantity': 0, 'price': 0})

    # Step 5: Clean column names (lowercase, no spaces)
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    print(f"Cleaned data: {len(df)} rows remaining")

    # Step 6: Save cleaned data
    if output_file.endswith('.csv'):
        df.to_csv(output_file, index=False)
    else:
        df.to_excel(output_file, index=False)

    print(f"Saved cleaned file to: {output_file}")

    # Step 7: Generate summary report
    first_col = df.columns[0]
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if numeric_cols:
        summary = df.groupby(first_col)[numeric_cols].sum()
        summary_file = 'summary_report.xlsx'
        summary.to_excel(summary_file)
        print(f"Summary report saved to: {summary_file}")
        print("\nSummary preview:")
        print(summary.head())

    return df


if __name__ == "__main__":
    # Example usage — replace with your actual file names
    clean_excel("sample_data.csv", "cleaned_data.xlsx")
