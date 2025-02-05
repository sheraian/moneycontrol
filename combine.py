import pandas as pd
import glob


def combine_csv_files(output_file='final_combined.csv'):
    # List all CSV files matching the pattern
    file_pattern = 'final_part_*.csv'
    csv_files = sorted(glob.glob(file_pattern))

    if not csv_files:
        print("No CSV files found. Please check the file names and directory.")
        return

    # Read and concatenate all CSV files, handling empty files
    df_list = []
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            if not df.empty:
                df_list.append(df)
            else:
                print(f"Skipping empty file: {file}")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if not df_list:
        print("No valid CSV data found to concatenate.")
        return

    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df.to_csv(output_file, index=False)
    print(f'Saved combined CSV file as {output_file}')


# Run the function
combine_csv_files()
