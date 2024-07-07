import pandas as pd


def process_hierarchy(csv_path):
    # Load the data
    df = pd.read_csv(csv_path)

    # Initialize variables
    max_depth = 0
    processed_data = []

    # Iterate through each row to build the hierarchy levels
    for _, row in df.iterrows():
        levels = row['Parent Chain'].split(' > ')
        max_depth = max(max_depth, len(levels))
        processed_row = [row['Topic']] + levels
        processed_data.append(processed_row)

    # Create a new DataFrame with dynamic columns based on the max depth
    column_names = ['Topic'] + [str(i + 1) for i in range(max_depth)]
    new_df = pd.DataFrame(processed_data, columns=column_names)

    # Fill the NaN values with empty strings
    new_df.fillna('', inplace=True)

    # Write to new CSV
    new_df.to_csv('../../data/processed/pages.csv', index=False)
    print("Processed CSV created successfully.")


# Use the function to process the hierarchy
process_hierarchy('../../data/interim/pages.csv')
