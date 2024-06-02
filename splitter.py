import pandas as pd
import os
from datetime import datetime

def split_file(input_file):
    # Determine the file extension
    file_extension = os.path.splitext(input_file)[1]
    
    # Read the file into a pandas DataFrame
    if file_extension == '.xlsx':
        df = pd.read_excel(input_file)
    elif file_extension == '.csv':
        df = pd.read_csv(input_file)
    else:
        raise ValueError("Unsupported file format. Please provide a .xlsx or .csv file.")
    
    # Get the current timestamp for file naming
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Split the DataFrame into chunks of 999 rows
    chunks = [df[i:i + 999] for i in range(0, df.shape[0], 999)]
    
    # Output the chunks to new files
    for idx, chunk in enumerate(chunks):
        part_number = idx + 1
        output_file = f"{timestamp}_part_{part_number}{file_extension}"
        
        if file_extension == '.xlsx':
            chunk.to_excel(output_file, index=False)
        elif file_extension == '.csv':
            chunk.to_csv(output_file, index=False)
        
        print(f"Created: {output_file}")

if __name__ == "__main__":
    input_file = input("Enter the input file path (.xlsx or .csv): ").strip()
    split_file(input_file)
