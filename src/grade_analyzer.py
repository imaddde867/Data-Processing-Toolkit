import pandas as pd

# Define a function to perform grade analysis
def analyze_grades(filepath, separator=';', header=None):
    """
    Analyzes student grades from a CSV file.

    Args:
        filepath (str): Path to the CSV file.
        separator (str): Separator used in the CSV file (default: ';').
        header (int or list-like or None): Row (0-indexed) to use as the column names, and the start of the data.  
                                            Default behavior is to infer the column names: if no names are passed the behavior is identical to `header=0` and column names are inferred from the first line of the file, if column names are passed explicitly then the behavior is identical to `header=None`.

    Returns:
        pandas.DataFrame: DataFrame containing student names and their average grades.  Returns None if there is an error reading the file.
    """
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(filepath, sep=separator, header=header)

        # Assign column names if not provided
        if header is None:
            df.columns = ['name'] + [f'grade_{i+1}' for i in range(df.shape[1]-1)]
        elif isinstance(header, int):
            df.columns = ['name'] + [f'grade_{i+1}' for i in range(df.shape[1]-1)]
        else:
            df.columns = header

        # Calculate the average grade for each student
        df['avg_grade'] = df.iloc[:, 1:].mean(axis=1)

        return df
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: CSV file '{filepath}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Could not parse CSV file '{filepath}'. Please check the file format and separator.")
        return None


# Main execution block
if __name__ == "__main__":
    filepath = 'data_sources/Grades.csv' 
    df = analyze_grades(filepath)

    if df is not None:
        # Print individual student grades and averages
        for i in df.itertuples():
            grades_str = ' '.join(map(str, i[1:-1])) # changed index from 2:12 to 1:-1 to handle variable number of grades
            print(f'Grades for {i.name}: {grades_str}')
            print(f'Average for {i.name}: {i[-1]}')

        # Print the class average
        print(f'{"*"*5}\nAverage of the class: {df["avg_grade"].mean()}')
